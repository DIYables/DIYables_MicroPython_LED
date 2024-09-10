"""
- It is created by DIYables to work with DIYables products, but also work with products from other brands.
- Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.
"""

from DIYables_MicroPython_LED import LED, LED_DELAY, LED_BLINKING, LED_IDLE, CTRL_ANODE

# Define LED pins
PIN_LED_1 = 22 # The Raspberry Pi Pico pin connected to the LED 1 (GP22)
PIN_LED_2 = 26 # The Raspberry Pi Pico pin connected to the LED 2 (GP26)
PIN_LED_3 = 27 # The Raspberry Pi Pico pin connected to the LED 3 (GP27)

# Create an array of LED objects
led_array = [
    LED(PIN_LED_1, CTRL_ANODE),  # create ezLED object that attach to pin PIN_LED_1
    LED(PIN_LED_2, CTRL_ANODE),  # create ezLED object that attach to pin PIN_LED_2
    LED(PIN_LED_3, CTRL_ANODE)   # create ezLED object that attach to pin PIN_LED_3
]

led_array[0].blink(500, 500)  # 500ms ON, 500ms OFF, blink immediately
led_array[1].blink_with_duration(100, 100, 5000)  # 100ms ON, 100ms OFF, blink for 5 seconds, blink immediately
led_array[2].blink_n_times(250, 750, 10)  # 250ms ON, 750ms OFF, repeat 10 times, blink immediately

# Function to print the state of an LED
def print_state(state, led_index):
    if state == LED_DELAY:
        print(f"LED {led_index + 1} DELAYING")
    elif state == LED_BLINKING:
        print(f"LED {led_index + 1} BLINKING")
    elif state == LED_IDLE:
        print(f"LED {led_index + 1} BLINK ENDED")

# Track the previous states of the LEDs
previous_states = [None] * len(led_array)

# Main loop
while True:
    # Update each LED state
    for i, led in enumerate(led_array):
        led.loop()  # MUST call the led.loop() function in loop()

        # Get the current state of the LED
        current_state = led.get_state()

        # Print the state only if it has changed
        if current_state != previous_states[i]:
            print_state(current_state, i)
            previous_states[i] = current_state  # Update the previous state

    # DO SOMETHING HERE
