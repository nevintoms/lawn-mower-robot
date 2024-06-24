import matplotlib.pyplot as plt
from shapely.geometry import Polygon
import matplotlib.animation as animation


class Visualise:
    def __init__(self) -> None:
        pass

    def plot(self, zigzag_path, cords):
        # Visualize the polygon and the zigzag path
        polygon = Polygon(cords)
        x, y = polygon.exterior.xy

        # Create the figure and axis
        fig, ax = plt.subplots()
        ax.plot(x, y, "lightgreen")
        ax.fill(x, y, "lightgreen")

        # Initialize the plot with empty lines
        (path_line,) = ax.plot([], [], "red")

        # Set plot limits and aspect ratio
        # ax.set_xlim(min(x) - 0.0001, max(x) + 0.0001)
        # ax.set_ylim(min(y) - 0.0001, max(y) + 0.0001)
        # ax.set_aspect('equal', adjustable='box')
        ax.axis("off")

        # Animation update function
        def update(frame):
            if frame == 0:
                return (path_line,)  # Nothing to plot in the first frame

            # Select points up to the current frame
            path_x, path_y = zip(*zigzag_path[: frame + 1])

            # Update the line data
            path_line.set_data(path_x, path_y)
            return (path_line,)

        # Create the animation
        ani = animation.FuncAnimation(
            fig, update, frames=len(zigzag_path), interval=100, blit=True
        )

        # Show the plot
        plt.show()
