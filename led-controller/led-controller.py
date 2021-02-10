import sys
import time
import logging

from rpi_ws281x import *
from networktables import NetworkTables

logging.basicConfig(level=logging.DEBUG)

# LED strip configuration:
LED_COUNT      = 20      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

ip = "10.68.0.2"
NetworkTables.initialize(server=ip)

def valueChanged(key, value, isNew):
    if key == '/Shooter/TurretEncoder':
        if value < 0:
            colorSet(strip, Color(0,255,0))
        else:
            colorSet(strip, Color(255,0,0))

    print("valueChanged: key: '%s'; value: %s; isNew: %s" % (key, value, isNew))

def colorSet(strip, color):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

NetworkTables.addEntryListener(valueChanged)

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

colorSet(strip, Color(0, 0, 255))

while True:
    time.sleep(1000.0)
