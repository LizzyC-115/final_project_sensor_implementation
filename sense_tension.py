"""
Hardware pipeline: Tension Sensor -> HX711 Amplifier -> Raspberry Pi
"""
import gpio         # read GPIO pins
import hx711        # access amplifier, HX711
import time

DAT_PIN = 5         # connected to DAT pin from HX711       
CLK_PIN = 6         # connected to CLK pin from HX711

CALIBRATION_FACTOR = 220.0  # adjust based on measurement (how much to amplify)

hx = hx711.HX711(dout_pin=DAT_PIN, pd_sck_pin=CLK_PIN)
hx.reset()
hx.tare()           # set baseline

print("Starting measurements...")

try:
    while True:
        raw = hx.get_weight_mean(10)
        print(f"Raw weight: {raw:.2f}")
        weight = raw / CALIBRATION_FACTOR
        print(f"Calibrated Weight (kg): {weight:.2f}")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Stopping measurements...")




