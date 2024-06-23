from location import Map
from robot import Robot
from visualise import Visualise


class RobotController:

    def __init__(self, get_live_robot_cords) -> None:
        self.map = Map()
        self.robot = Robot(get_live_robot_cords)
        self.viz = Visualise()

    def run_robot(self, zigzag_path):
        for cords in zigzag_path:
            start, end = cords
            self.robot.move(end)

    def start(self):
        zigzag_path, cords = self.map.get_path_with_cords()
        self.viz.plot(zigzag_path, cords)

        # start_cords = zigzag_path[0][0]
        # # move robot to start cords
        # self.robot.move(start_cords)
        # self.run_robot(zigzag_path)
