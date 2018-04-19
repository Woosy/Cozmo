import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps


# Cozmo conduit tout droit
def cozmo_drive(robot: cozmo.robot.Robot):
    # Drive forwards for 150 millimeters at 50 millimeters-per-second.
    robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()

    # Turn 90 degrees to the left.
    # Note: To turn to the right, just use a negative number.
    robot.turn_in_place(degrees(90)).wait_for_completed()


cozmo.run_program(cozmo_drive)

