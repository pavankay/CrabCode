from pybricks.iodevices import XboxController
from pybricks.parameters import Button, Direction, Port
from pybricks.pupdevices import Motor
from pybricks.robotics import Car

# Set up all devices.
Rear_R = Motor(Port.B, Direction.COUNTERCLOCKWISE)
Rear_L = Motor(Port.F, Direction.CLOCKWISE)
Front_R = Motor(Port.A, Direction.COUNTERCLOCKWISE)
Front_L = Motor(Port.E, Direction.CLOCKWISE)
Steer_Front = Motor(Port.C, Direction.CLOCKWISE)
Steer_Back = Motor(Port.D, Direction.CLOCKWISE)
Car_Controller_Front = Car(Steer_Front, [Rear_R, Rear_L, Front_R, Front_L])
Car_Controller_Back = Car(Steer_Back, [Front_R, Front_L])
controller = XboxController()

# Initialize variables.
Mode = 0


# The main program starts here.
print('Hello, Pybricks!')
while True:
    if Button.MENU in controller.buttons.pressed():
        if Mode == 1:
            Car_Controller_Back.steer(0)
            Mode = 0
            print(Mode)
        else:
            Car_Controller_Back.steer(0)
            Mode = 1
            print(Mode)
    Car_Controller_Front.drive_power(controller.triggers()[0] - controller.triggers()[1])
    Car_Controller_Front.steer(controller.joystick_left()[0])
    if Mode == 1:
        Car_Controller_Back.drive_power(controller.triggers()[0] - controller.triggers()[1])
        Car_Controller_Back.steer(controller.joystick_left()[0])
    else:
        Car_Controller_Back.drive_power(controller.triggers()[0] - controller.triggers()[1])
        #Car_Controller_Back.steer(-1 * controller.joystick_left()[0])
