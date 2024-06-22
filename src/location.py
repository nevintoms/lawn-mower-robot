from typing import List


class Map:

    def __init__(self) -> None:
        pass

    def _get_coordinates(self) -> List:
        """
        This function gets the boundary coordinates of the
        selected area using selenioum from google maps.
        """
        pass

    def _zigzag_path(self, cords: List) -> List[List]:
        """
        This fucntion generates the best fit zigzag path
        inside the selected area.
        """
        return [
            [(0, 0), (0, 100)],
            [(0, 100), (100, 10)],
            [(100, 10), (0, 10)],
            [(0, 10), (0, 20)],
            [(0, 20), (100, 20)],
        ]

    def get_path(self):
        cords = self._get_coordinates()
        zigzag_path = self._zigzag_path(cords)
        return zigzag_path
