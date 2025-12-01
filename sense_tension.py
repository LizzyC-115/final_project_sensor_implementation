from machine import Pin
import time
from hx711 import HX711
from picozero import pico_led

# -----------------------------
# Setup HX711 pins
# -----------------------------
DT_PIN = Pin(15, Pin.IN)   # DOUT
SCK_PIN = Pin(14, Pin.OUT) # SCK

hx = HX711(SCK_PIN, DT_PIN)
hx.set_scale(1000)   # initial scale factor (calibrate later)
hx.tare()            # tare the scale

print("Tare done. Start weighing...\n")

# -----------------------------
# Main loop
# -----------------------------
try:
#     pico_led.blink()
    while True:
        weight = hx.get_units()
        print("Weight: {:.2f} g".format(weight))
        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nStopped by user.")




