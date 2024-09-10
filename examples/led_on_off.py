"""
- It is created by DIYables to work with DIYables products, but also work with products from other brands.
- Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.
"""

from machine import Pin
from DIYables_MicroPython_LED import LED, LED_ON, CTRL_ANODE

BUTTON_PIN = 2  # The Raspberry Pi Pico pin connected to the button (GP2)
LED_PIN = 13    # The Raspberry Pi Pico pin connected to the LED (GP13)

led = LED(LED_PIN, CTRL_ANODE)  # create an LED object that connects to LED
button = Pin(BUTTON_PIN, Pin.IN, Pin.PULL_UP)  # set up the button with an internal pull-up resistor

while True:
    led.loop()  # MUST call the led.loop() function in loop()

    button_state = button.value()

    if button_state == 0:  # Button is pressed (LOW)
        led.turn_on()       # turn on immediately
        # led.turn_on(1000) # turn on after 1 second
    else:
        led.turn_off()       # turn off immediately
        # led.turn_off(1000) # turn off after 1 second

    if led.get_on_off() == LED_ON:
        print("LED is ON")
    else:
        print("LED is OFF")

