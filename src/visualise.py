import matplotlib.pyplot as plt
from shapely.geometry import Polygon

class Visualise:
    def __init__(self) -> None:
        pass

    def plot(self, zigzag_path, cords):
        # Visualize the polygon and the zigzag path
        polygon = Polygon(cords)
        x, y = polygon.exterior.xy

        # Plot the polygon
        plt.figure()
        plt.plot(x, y, 'lightgreen')
        plt.fill(x, y, 'lightgreen')

        # Plot the zigzag path
        if zigzag_path:
            path_x, path_y = zip(*zigzag_path)
            plt.plot(path_x, path_y, 'red')

        # Set plot limits and aspect ratio
        # plt.xlim(min(x)-0.0001, max(x)+0.0001)
        # plt.ylim(min(y)-0.0001, max(y)+0.0001)
        # plt.gca().set_aspect('equal', adjustable='box')
        plt.axis('off')

        # Show the plot
        plt.show()
