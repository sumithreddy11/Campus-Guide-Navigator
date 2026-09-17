
from math import radians, sin, cos, sqrt, atan2


def distance_between(lat1, lon1, lat2, lon2):

    earth_radius = 6371000

    lat1 = radians(lat1)
    lat2 = radians(lat2)

    delta_lat = radians(lat2 - lat1)
    delta_lon = radians(lon2 - lon1)

    a = (
        sin(delta_lat / 2) ** 2
        + cos(lat1)
        * cos(lat2)
        * sin(delta_lon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return earth_radius * c


def find_current_location(latitude, longitude, locations):

    nearest_location = None
    nearest_distance = float("inf")

    for name, location in locations.items():

        distance = distance_between(
            latitude,
            longitude,
            location["latitude"],
            location["longitude"]
        )

        if distance < nearest_distance:

            nearest_distance = distance
            nearest_location = name

    return nearest_location, nearest_distance


def is_inside_location(latitude, longitude, location):

    distance = distance_between(
        latitude,
        longitude,
        location["latitude"],
        location["longitude"]
    )

    return distance <= location["radius"]
