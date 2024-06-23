from shapely.geometry import Polygon, LineString, Point, MultiPoint, MultiLineString
from shapely.affinity import scale
from typing import List


class Map:

    def __init__(self) -> None:
        pass

    def _get_coordinates(self) -> List:
        """
        This function gets the boundary coordinates of the
        selected area using selenioum from google maps.
        """
        # Define polygon boundary coordinates using latitude and longitude
        polygon_coords = [
            (43.935763, -78.734302),  # Bottom-left
            (43.935871, -78.733749),  # Bottom-right
            (43.936303, -78.733910),  # Top-right
            (43.936211, -78.734543),
        ]
        return polygon_coords

    # def _zigzag_path(self, cords: List) -> List[List]:
    #     """
    #     This fucntion generates the best fit zigzag path
    #     inside the selected area.
    #     """
    def generate_boundary_paths(polygon_coords, num_boundary_layers, shrink_factor):
        polygon = Polygon(polygon_coords)
        paths = []
        current_polygon = polygon

        for i in range(num_boundary_layers):
            exterior_coords = current_polygon.exterior.coords[
                :-1
            ]  # Exclude the repeated last point
            paths.append(exterior_coords)
            current_polygon = scale(
                current_polygon,
                xfact=shrink_factor,
                yfact=shrink_factor,
                origin="center",
            )

        return paths

    def generate_zigzag_path_with_boundaries(
        polygon_coords, interval, num_boundary_layers, shrink_factor
    ):
        boundary_paths = generate_boundary_paths(
            polygon_coords, num_boundary_layers, shrink_factor
        )
        polygon = Polygon(polygon_coords)
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
                        points.extend([Point(coord) for coord in linestring.coords])

                points = sorted(points, key=lambda p: p.x)
                if direction == -1:
                    points.reverse()
                for point in points:
                    path.append((point.x, point.y))
            y += interval
            direction *= -1

        return path
        # return [
        #     [(0, 0), (0, 100)],
        #     [(0, 100), (100, 10)],
        #     [(100, 10), (0, 10)],
        #     [(0, 10), (0, 20)],
        #     [(0, 20), (100, 20)],
        # ]

    def get_path(self):
        cords = self._get_coordinates()
        interval = 0.00005  # Adjust the interval to match the latitude and longitude scale
        num_boundary_layers = 3
        shrink_factor = 0.95  # Adjust the shrink factor as necessary
        zigzag_path = self.generate_zigzag_path_with_boundaries(
            cords, interval, num_boundary_layers, shrink_factor
        )
        return zigzag_path
