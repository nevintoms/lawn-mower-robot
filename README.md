# lawn-mower-robot
This is a robotic lawn mover application.

There are 3 classes
## class Robot
This class is responsible for the motion of the robot.
## class Map
This class gets the boundary coordinates of seleted area and also deifnes the best fit path in the given location.
## class RobotController
This class controlls the robot with respect to the path details given by the class Map.

# How does it work?
The execution start from the `main.py` file, which initiates the `RobotController` class. The `RobotController` class is responsible for initiating both `Map` and `Robot` classes.

The `start` method in `RobotController` is responsible for starting the whole process. It first calls the `get_path` function in `Map` class from which the boundary coordinates of the location and the zigzag path is generated for the selected area. This zigzag path is used in the `run_robot` method to navigate the robot along the generated path. 

The `move` method in the `Robot` class is responsible for checking the angle between the current coordinate and the next coordiante. The `_turn` method turn the robot to the specified angle. The `_move` method moves the robot from current position to the given coordinates.

