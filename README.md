## MicroPython LED Library - DIYables_MicroPython_LED
This MicroPython LED library is designed for any hardware platform that supports MicroPython such as Raspberry Pi Pico, ESP32, Micro:bit... to make it easy to control LED. It is easy to use for not only beginners but also experienced users... 

It is created by DIYables to work with DIYables products, but also work with products from other brands. Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.



Features
----------------------------
* Turn on/off
* Toggle between on and off
* Fade in/out
* Blink
* Blink with the number of times
* Blink in a period of time
* Cancel the blinking or fading anytime
* Support both control modes: CTRL_ANODE and CTRL_CATHODE
* Get the on/off LED's states: LED_OFF, LED_ON
* Get the operation LED's state: LED_IDLE, LED_DELAY, LED_FADING, LED_BLINKING
* All functions are non-blocking (without using delay() function)
* Easy to use with multiple LEDs



Available Functions
----------------------------
* \_\_init\_\_(pin, mode)
* turn_on(delay_time=0)
* turn_off(delay_time=0)
* toggle(delay_time=0)
* fade(fade_from, fade_to, fade_time, delay_time=0)
* blink(on_time, off_time, delay_time=0)
* blink_with_duration(on_time, off_time, blink_time, delay_time=0)
* blink_n_times(on_time, off_time, number_of_times, delay_time=0)
* cancel()
* get_on_off()
* get_state()
* loop()



Available Examples
----------------------------
* led_blink.py
* led_fade.py
* led_on_off.py
* led_toggle.py
* led_multiple.py
* led_blink_n_times.py
* led_blink_with_duration.py
* led_array.py



Tutorials
----------------------------
* [ESP32 MicroPython - Blink LED](https://newbiely.com/tutorials/esp32-micropython/esp32-micropython-blink-led)
* [ESP32 MicroPython - Blink LED without Sleep](https://newbiely.com/tutorials/esp32-micropython/esp32-micropython-blink-led-without-sleep)
* [ESP32 MicroPython - Fade LED](https://newbiely.com/tutorials/esp32-micropython/esp32-micropython-fade-led)
* [Raspberry Pi Pico - Blink LED](https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-blink-led)
* [Raspberry Pi Pico - Blink LED without Sleep](https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-blink-led-without-sleep)
* [Raspberry Pi Pico - Fade LED](https://newbiely.com/tutorials/raspberry-pico/raspberry-pi-pico-fade-led)


References
----------------------------
* [MicroPython LED Library](https://newbiely.com/tutorials/micropython/micropython-led-library)
