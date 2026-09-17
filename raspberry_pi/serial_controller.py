
import serial
import time


class MotorController:

    def __init__(
        self,
        port="/dev/ttyACM0",
        baudrate=115200
    ):

        self.serial = serial.Serial(
            port,
            baudrate,
            timeout=1
        )

        time.sleep(2)

    def send_command(self, command):

        command = command.upper().strip()

        self.serial.write(
            (command + "\n").encode("utf-8")
        )

        print("Arduino command:", command)

    def forward(self):
        self.send_command("FORWARD")

    def backward(self):
        self.send_command("BACKWARD")

    def left(self):
        self.send_command("LEFT")

    def right(self):
        self.send_command("RIGHT")

    def stop(self):
        self.send_command("STOP")

    def close(self):
        self.serial.close()
