"""
- It is created by DIYables to work with DIYables products, but also work with products from other brands.
- Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.
"""

from DIYables_MicroPython_LED import LED, LED_BLINKING, LED_IDLE, CTRL_ANODE

# Create an LED object that attaches to pin 13
led = LED(13, CTRL_ANODE)

led.blink(250, 750)  # 250ms ON, 750ms OFF, blink immediately
# led.blink(250, 750, 1000)  # Uncomment to blink after 1 second delay

# Function to print the state of the LED
def print_state(state):
    if state == LED_BLINKING:
        print("BLINKING")
    elif state == LED_IDLE:
        print("BLINK ENDED")

# Track the previous state of the LED
previous_state = None

# Main loop
while True:
    led.loop()  # MUST call the led.loop() function in loop

    # Get the current state of the LED
    current_state = led.get_state()

    # Print the state only if it has changed
    if current_state != previous_state:
        print_state(current_state)
        previous_state = current_state  # Update the previous state

    # DO OTHER TASKS HERE
    # To stop blinking immediately, call led.cancel()
