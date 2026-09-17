
from campus_map import CAMPUS_LOCATIONS
from gps import GPSReader
from navigation import find_current_location
from serial_controller import MotorController


def main():

    print("======================================")
    print(" CAMPUS GUIDE NAVIGATOR")
    print(" Raspberry Pi Navigation System")
    print("======================================")

    gps = GPSReader(
        port="/dev/ttyUSB0",
        baudrate=9600
    )

    motor = MotorController(
        port="/dev/ttyACM0",
        baudrate=115200
    )

    try:

        while True:

            latitude, longitude = gps.read_data()

            print()
            print("GPS Position:")
            print("Latitude :", latitude)
            print("Longitude:", longitude)

            location, distance = find_current_location(
                latitude,
                longitude,
                CAMPUS_LOCATIONS
            )

            print(
                "Nearest location:",
                location
            )

            print(
                "Distance:",
                round(distance, 2),
                "meters"
            )

            # Example control logic
            if distance <= CAMPUS_LOCATIONS[location]["radius"]:

                print(
                    "Arrived at:",
                    location
                )

                motor.stop()

            else:

                # Temporary demonstration command
                motor.forward()

    except KeyboardInterrupt:

        print("\nNavigation stopped.")

    finally:

        motor.stop()
        motor.close()
        gps.close()


if __name__ == "__main__":
    main()
