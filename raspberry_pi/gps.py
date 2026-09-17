import serial
import time


class GPSReader:

    def __init__(self, port="/dev/ttyUSB0", baudrate=9600):

        self.serial = serial.Serial(
            port,
            baudrate,
            timeout=1
        )

        time.sleep(2)

    def read_data(self):

        while True:

            line = self.serial.readline().decode(
                "ascii",
                errors="ignore"
            ).strip()

            if line.startswith("$GPGGA") or line.startswith("$GNGGA"):

                data = line.split(",")

                if len(data) > 6 and data[2] and data[4]:

                    latitude = self.convert_coordinate(
                        data[2],
                        data[3]
                    )

                    longitude = self.convert_coordinate(
                        data[4],
                        data[5]
                    )

                    return latitude, longitude

    def convert_coordinate(self, value, direction):

        degrees = int(float(value) / 100)

        minutes = float(value) - (degrees * 100)

        coordinate = degrees + minutes / 60

        if direction in ["S", "W"]:
            coordinate = -coordinate

        return coordinate

    def close(self):

        self.serial.close()
