"""
Hardware pipeline: Tension Sensor -> HX711 Amplifier (increase the signal) -> Raspberry Pi
"""
import gpio         # read GPIO pins
import hx711        # access amplifier, HX711
import time

DT_PIN = 5          
SCK_PIN = 6

CALIBRATION_FACTOR = 220.0  # adjust based on your measurement

hx = hx711.HX711(dout_pin=DT_PIN, pd_sck_pin=SCK_PIN)
hx.reset()
hx.tare()

print("Starting measurements...")

try:
    while True:
        raw = hx.get_weight_mean(10)
        weight = raw / CALIBRATION_FACTOR
        print(f"{weight:.2f} kg")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Stopping measurements...")




