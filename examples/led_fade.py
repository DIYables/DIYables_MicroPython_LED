"""
- It is created by DIYables to work with DIYables products, but also work with products from other brands.
- Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.
"""

from DIYables_MicroPython_LED import LED, CTRL_ANODE, LED_IDLE

led = LED(13, CTRL_ANODE)  # create an LED object that attaches to pin 13
is_faded_in = False

while True:
    led.loop()  # MUST call the led.loop() function in loop()

    if led.get_state() == LED_IDLE:
        if not is_faded_in:
            print("FADING IN")
            led.fade(0, 255, 3000)         # fade in from 0 to 255 in 3000ms, fade immediately
            # led.fade(0, 255, 3000, 1000) # fade in from 0 to 255 in 3000ms, fade after 1 second
            is_faded_in = True
        else:
            print("FADING OUT")
            led.fade(255, 0, 3000)          # fade out from 255 to 0 in 3000ms, fade immediately
            # led.fade(255, 0, 3000, 1000)  # fade out from 255 to 0 in 3000ms, fade after 1 second
            is_faded_in = False
