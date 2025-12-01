"""
Used by Pupper's Raspberry Pi 4 to read the serial outputs from the Raspberry Pi Pico W.
"""

import serial

# Update port if needed: check with `ls /dev/ttyACM*` before running
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)

while True:
    line = ser.readline().decode('utf-8').strip()
    if not line:
        continue
    
    # Try to parse numeric weight
    try:
        weight = float(line)
        print("Weight:", weight)
        if weight > 5:
            print("Robot: TURN RIGHT!")
            # Insert your motor control code here
    except ValueError:
        # Handle commands like TURN_RIGHT
        if line == "TURN_RIGHT":
            print("Robot: TURN RIGHT!")
            # Trigger motors here
