from machine import Pin, UART
import time
from hx711 import HX711

# -----------------------------
# Setup HX711 pins
# -----------------------------
DT_PIN = Pin(2, Pin.IN)   # DOUT
SCK_PIN = Pin(3, Pin.OUT) # SCK

uart = UART(0, baudrate=115200, tx=0, rx=1)
hx = HX711(SCK_PIN, DT_PIN)
hx.set_scale(1000)   # initial scale factor (calibrate later)
hx.tare()            # tare the scale

print("Tare done. Start weighing...\n")

# -----------------------------
# Main loop
# -----------------------------
try:
    while True:
        weight = hx.get_units()
        print("Weight: {:.2f} g".format(weight))
        uart.write("Weight: {:.2f} g".format(weight))
        time.sleep(0.2)

except KeyboardInterrupt:
    print("\nStopped by user.")
