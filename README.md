# Walk Pupper — Sensor-Driven Leash Control

Walk Pupper is a mobile robot designed to mimic the behavior of a dog being guided on a leash. This repository contains the sensor-based leash-tension control system, enabling the robot to autonomously walk forward while responding to directional pulls from a user.

# Project Overview

Creating robots that can react in real time to user input and environmental forces is a fundamental challenge in robotics. Walk Pupper explores this space through a simple but expressive interaction model: leash tension.

This implementation allows Pupper to:

- Walk forward autonomously.

- Detect external forces applied via a leash.

- Interpret tension direction (left/right, forward/backward).

- Convert those forces into steering commands.

No reinforcement-learning components are included in this repository.

# Hardware Setup
Components

Pupper robot

- Two tension sensors (5 kg load cells)

- One aligned with the x-axis

- One aligned with the y-axis

- Rope/leash attached to the tension sensor mount

# Schematic
The system uses two orthogonal load cells to detect the vector of applied external force. Combined, they allow Pupper to sense:

- Positive/negative force on the x-axis → turn left/right
- Positive/negative force on the y-axis → influence forward/backward mov


# Pipeline
Raspberry Pi Pico W (sense_tension.py) -> Raspberry Pi 4 (read_data.py) -> Pupper

