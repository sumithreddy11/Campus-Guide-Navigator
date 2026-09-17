# Campus Guide Navigator

A GPS-based campus navigation system developed to help users locate and navigate between different destinations within a campus.

## Overview

The Campus Guide Navigator uses a **Raspberry Pi as the main processing unit** and an **Arduino as the motor-control unit**.

The Raspberry Pi handles the high-level navigation logic, processes GPS information, maintains the campus location data, and determines the required movement. The Arduino receives movement commands from the Raspberry Pi through serial communication and controls the motors accordingly.

## System Architecture


<img width="1800" height="3465" alt="NEO-8M GPS Navigation Logic-2026-09-17-171625" src="https://github.com/user-attachments/assets/3dcdd5c2-7633-40af-a3aa-1fe1a02c02a6" />


## Key Features

* GPS-based location detection
* Predefined campus locations and coordinates
* Distance calculation between the current position and campus locations
* Detection of the user's current campus location
* Raspberry Pi-based navigation logic
* Serial communication between Raspberry Pi and Arduino
* Arduino-based motor control
* Modular separation between navigation and motor-control layers
* Testing and debugging of hardware and software components

## System Components

### Raspberry Pi

The Raspberry Pi 8-GB RAM acts as the **high-level controller** of the system.

Responsibilities include:

* Processing GPS information
* Maintaining campus location data
* Determining the current location
* Handling navigation decisions
* Sending movement commands to the Arduino

### Arduino

The Arduino acts as the **low-level motor controller**.

It receives commands from the Raspberry Pi through serial communication and converts them into motor-control signals.

Example commands include:

```text
FORWARD
BACKWARD
LEFT
RIGHT
STOP
```

### GPS Module

A **NEO-8M GPS module** is used to obtain the current latitude and longitude of the navigation system.

The GPS coordinates are compared with predefined campus locations to determine the current location and proximity to destinations.

## Software Structure

```text
raspberry_pi/
├── main.py
├── gps.py
├── campus_map.py
├── navigation.py
└── serial_controller.py

arduino/
└── motor_controller/
    └── motor_controller.ino
```

### Raspberry Pi Modules

**`main.py`**

Coordinates the overall system and connects the GPS, navigation, and Arduino communication modules.

**`gps.py`**

Handles GPS data acquisition and processing.

**`campus_map.py`**

Contains the predefined campus locations and their geographical coordinates.

**`navigation.py`**

Contains the location and navigation-related logic, including distance calculations.

**`serial_controller.py`**

Handles serial communication between the Raspberry Pi and Arduino.

### Arduino

**`motor_controller.ino`**

Receives commands from the Raspberry Pi and controls the motors through the motor driver.

## Technologies Used

* Python
* C/C++
* Raspberry Pi 4B 8-GB RAM
* Arduino
* NEO-8M GPS
* Location Scripting
* Serial Communication
* Motor Driver Calibrator


## Development Approach

The system was developed through multiple stages:

1. Requirement understanding
2. System architecture planning
3. Task division within the team
4. GPS and location testing
5. Navigation logic development
6. Raspberry Pi–Arduino communication
7. Motor-control implementation
8. System testing and debugging
9. Refinement based on test results
10. Documentation

## Team Collaboration

The project was developed collaboratively as a team. We discussed requirements, shared implementation approaches, divided tasks, communicated progress, and reviewed different solutions during the development cycles.

Working through these cycles helped us understand different perspectives, identify problems earlier, and improve the overall system based on feedback from one another.

## Key Learnings

Through this project, I gained practical experience in:

* Requirement analysis
* Embedded system development
* Hardware-software integration
* Serial communication
* GPS interfacing
* Debugging
* Testing
* Task tracking
* Documentation
* Team collaboration
* Problem-solving
* Understanding dependencies between different system components

One of the important lessons was understanding how a larger system can be divided into different layers, with the Raspberry Pi handling high-level processing and the Arduino handling low-level motor control.

## Project Status
Further improvements can include enhanced route planning, more robust GPS handling, improved navigation accuracy, and additional feedback mechanisms between the navigation and motor-control layers. Open Contributions are welcomed.
