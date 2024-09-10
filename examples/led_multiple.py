"""
- It is created by DIYables to work with DIYables products, but also work with products from other brands.
- Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.
"""

from DIYables_MicroPython_LED import LED, LED_DELAY, LED_BLINKING, LED_IDLE, CTRL_ANODE

# Define LED pins
PIN_LED_1 = 22 # The Raspberry Pi Pico pin connected to the LED 1 (GP22)
PIN_LED_2 = 26 # The Raspberry Pi Pico pin connected to the LED 2 (GP26)
PIN_LED_3 = 27 # The Raspberry Pi Pico pin connected to the LED 3 (GP27)

# Create LED objects that attach to the specified pins
led1 = LED(PIN_LED_1, CTRL_ANODE)
led2 = LED(PIN_LED_2, CTRL_ANODE)
led3 = LED(PIN_LED_3, CTRL_ANODE)


led1.blink(500, 500)  # 500ms ON, 500ms OFF, blink immediately
led2.blink_with_duration(100, 100, 5000)  # 100ms ON, 100ms OFF, blink for 5 seconds, blink immediately
led3.blink_n_times(250, 750, 10)  # 250ms ON, 750ms OFF, repeat 10 times, blink immediately

# Function to print the state of an LED
def print_state(state, led_name):
    if state == LED_DELAY:
        print(f"{led_name} DELAYING")
    elif state == LED_BLINKING:
        print(f"{led_name} BLINKING")
    elif state == LED_IDLE:
        print(f"{led_name} BLINK ENDED")

# Main loop
while True:
    led1.loop()  # MUST call the led1.loop() function
    led2.loop()  # MUST call the led2.loop() function
    led3.loop()  # MUST call the led3.loop() function

    # Print the state of each LED using the defined function
    print_state(led1.get_state(), "LED 1")
    print_state(led2.get_state(), "LED 2")
    print_state(led3.get_state(), "LED 3")

    # DO OTHER TASKS HERE
    # DO SOMETHING HERE


