"""
- It is created by DIYables to work with DIYables products, but also work with products from other brands.
- Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.
"""

from DIYables_MicroPython_Button import Button
from DIYables_MicroPython_LED import LED, LED_ON, CTRL_ANODE

BUTTON_PIN = 2  # The Raspberry Pi Pico pin connected to the button (GP2)
LED_PIN = 13    # The Raspberry Pi Pico pin connected to the LED (GP13)

# Initialize button and LED
button = Button(BUTTON_PIN)           # create a button object that attaches to pin 7
led = LED(LED_PIN, CTRL_ANODE)   # create an LED object that attaches to pin 3

# Setup
button.set_debounce_time(50)  # set debounce time to 50ms

while True:
    button.loop()  # MUST call the loop() function for the button
    led.loop()     # MUST call the loop() function for the LED

    if button.is_pressed():
        led.toggle()  # toggle immediately
        # led.toggle(1000)  # toggle after 1 second



