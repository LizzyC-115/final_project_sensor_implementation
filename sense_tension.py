"""
Used by Raspberry Pi Pico W to read load cell data.
"""
from machine import Pin
import time
from hx711 import HX711


DT_PIN = Pin(15, Pin.IN)   # DOUT
SCK_PIN = Pin(14, Pin.OUT) # SCK
BUFFER = 5                 # Threshold to send command

def retrieve(dt_pin, sck_pin, buffer):
    hx = HX711(sck_pin, dt_pin)
    hx.set_scale(1000)   # initial scale factor (calibrate later)
    hx.tare()            # tare the scale

    print("Tare done. Start weighing...\n")


    try: 
        weight = hx.get_units()
        print("Weight: {:.2f} g".format(weight))
        
        if weight < -buffer:
            print("[TURN LEFT]")
        
        elif weight > buffer:
            print("[TURN RIGHT]")
            
        else:
            print("SEND NO COMMANDS")

    time.sleep(0.2)
            
    except Exception as e:
        print(f"Error reading sensor: {e}")





