from shapely.geometry import Polygon, LineString, Point, MultiPoint, MultiLineString
from shapely.affinity import scale
from typing import List


class Map:

    def __init__(self) -> None:
        self.INTERVAL = (
            0.00005  # Adjust the interval to match the latitude and longitude scale
        )
        self.NUM_BOUNDARY_LAYERS = 3
        self.SHRINK_FACTOR = 0.95  # Adjust the shrink factor as necessary

    def _get_coordinates(self) -> List:
        """
        This function gets the boundary coordinates of the
        selected area using selenioum from google maps.
        """
        # Define polygon boundary coordinates using latitude and longitude
        polygon_cords = [
            (43.935763, -78.734302),  # Bottom-left
            (43.935871, -78.733749),  # Bottom-right
            (43.936303, -78.733910),  # Top-right
            (43.936211, -78.734543),  # Top-left
        ]
        return polygon_cords

    def generate_boundary_paths(self, polygon_cords):
        polygon = Polygon(polygon_cords)
        paths = []
        current_polygon = polygon

        for i in range(self.NUM_BOUNDARY_LAYERS):
            exterior_cords = current_polygon.exterior.coords[
                :-1
            ]  # Exclude the repeated last point
            paths.append(exterior_cords)
            current_polygon = scale(
                current_polygon,
                xfact=self.SHRINK_FACTOR,
                yfact=self.SHRINK_FACTOR,
                origin="center",
            )

        return paths

    def generate_zigzag_path_with_boundaries(self, polygon_cords):
        """
        This fucntion generates the best fit zigzag path
        inside the selected area.
        """
        boundary_paths = self.generate_boundary_paths(polygon_cords)
        polygon = Polygon(polygon_cords)
        minx, miny, maxx, maxy = polygon.bounds
        path = []

        # Add boundary paths to the main path
        for boundary_path in boundary_paths:
            path.extend(boundary_path)

        # Generate the zigzag path inside the innermost boundary path
        y = miny
        direction = 1

        while y <= maxy:
            line = LineString([(minx, y), (maxx, y)])
            intersection_points = polygon.intersection(line)
            if not intersection_points.is_empty:
                # Convert intersection result to a list of points
                if isinstance(intersection_points, (Point, MultiPoint)):
                    points = (
                        [intersection_points]
                        if isinstance(intersection_points, Point)
                        else list(intersection_points)
                    )
                elif isinstance(intersection_points, LineString):
                    points = [Point(coord) for coord in intersection_points.coords]
                elif isinstance(intersection_points, MultiLineString):
                    points = []
                    for linestring in intersection_points:
                        points.extend([Point(coord) for coord in linestring.cords])

                points = sorted(points, key=lambda p: p.x)
                if direction == -1:
                    points.reverse()
                for point in points:
                    path.append((point.x, point.y))
            y += self.INTERVAL
            direction *= -1

        return path

    def get_path_with_cords(self):
        cords = self._get_coordinates()
        zigzag_path = self.generate_zigzag_path_with_boundaries(cords)
        return zigzag_path, cords
