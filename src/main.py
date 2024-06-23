from random import randint

from controller import RobotController


def get_live_robot_cords():
    # get the current position of the robot using
    # the geolocation device.
    # call to robot api/sdk for live co-ordinates
    return (randint(0, 10), randint(0, 10))


if __name__ == "__main__":
    rc = RobotController(get_live_robot_cords)
    print("-------START-------")
    rc.start()
    print("-------END-------")
