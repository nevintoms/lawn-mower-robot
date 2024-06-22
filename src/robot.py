class Robot:

    def __init__(self, get_live_robot_cords) -> None:
        self.get_live_robot_cords = get_live_robot_cords

    @property
    def curr_cords(self):
        return self.get_live_robot_cords()

    def _get_angle(self, cords):
        """
        Gets the angle between current position of the robot
        and the given cordiantes.
        """
        return 90

    def _turn(self, angle):
        if angle == 0:
            return
        print("Turned 90 degrees")

    def _move(self, cords):
        if self.curr_cords == cords:
            return
        print(f"Reached {cords}")

    def move(self, cords):
        angle = self._get_angle(cords)
        self._turn(angle)
        self._move(cords)
