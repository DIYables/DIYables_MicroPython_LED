"""
This MicroPython library is designed for any hardware plaform that supports MicroPython such as Raspberry Pi Pico, ESP32, Micro:bit... to make it easy to use to control LED.

It is created by DIYables to work with DIYables products, but also work with products from other brands. Please consider purchasing products from [DIYables Store on Amazon](https://amazon.com/diyables) from to support our work.

Product Link:
Product Link:
- LED Kit: https://diyables.io/products/led-kit
- Sensor Kit: https://diyables.io/products/sensor-kit


Copyright (c) 2024, DIYables.io. All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

- Redistributions of source code must retain the above copyright
  notice, this list of conditions and the following disclaimer.

- Redistributions in binary form must reproduce the above copyright
  notice, this list of conditions and the following disclaimer in the
  documentation and/or other materials provided with the distribution.

- Neither the name of the DIYables.io nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY DIYABLES.IO "AS IS" AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL DIYABLES.IO BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""

from machine import Pin, PWM
import time

# Constants
CTRL_ANODE = 0
CTRL_CATHODE = 1
LED_OFF = 0
LED_ON = 1

LED_MODE_OFF = 0
LED_MODE_ON = 1
LED_MODE_TOGGLE = 2
LED_MODE_FADE = 3
LED_MODE_BLINK_FOREVER = 4
LED_MODE_BLINK_PERIOD = 5
LED_MODE_BLINK_NUM_TIME = 6

LED_STATE_IDLE = 0
LED_STATE_DELAY = 1
LED_STATE_ON_OFF = 2
LED_STATE_FADE = 3
LED_STATE_BLINK = 4

LED_IDLE = 0
LED_DELAY = 1
LED_FADING = 2
LED_BLINKING = 3

class LED:
    def __init__(self, pin, mode):
        self.led_pin_num = pin
        self.ctrl_mode = mode
        self.led_mode = LED_MODE_OFF
        self.led_state = LED_STATE_IDLE
        self.output_state = LED_OFF
        self.brightness = 0
        self.is_pwm_mode = False  # Track if the pin is in PWM mode
        self.led_pin = Pin(self.led_pin_num, Pin.OUT)  # Set pin to digital output mode

        self.fade_from = 0
        self.fade_to = 0
        self.fade_time = 0
        self.blink_on_time = 0
        self.blink_off_time = 0
        self.blink_time_period = 0
        self.blink_number_of_times = 0
        self.delay_time = 0
        self.last_time = 0
        self.blink_timer = 0
        self.blink_counter = 0

    def set_blink(self, on_time, off_time, delay_time):
        self.blink_on_time = on_time
        self.blink_off_time = off_time
        self.delay_time = delay_time
        self.last_time = time.ticks_ms()

    def update_analog(self):
        # Switch to PWM mode if not already in it
        if not self.is_pwm_mode:
            self.led_pin = PWM(Pin(self.led_pin_num))  # Initialize PWM
            self.led_pin.freq(1000)  # Set PWM frequency
            self.is_pwm_mode = True

        # Set the PWM duty cycle based on control mode
        if self.ctrl_mode == CTRL_ANODE:
            self.led_pin.duty_u16(int(self.brightness * 65535 / 255))
        else:
            self.led_pin.duty_u16(int((255 - self.brightness) * 65535 / 255))

    def update_digital(self):
        # Switch to digital mode if currently in PWM mode
        if self.is_pwm_mode:
            self.led_pin.deinit()  # Disable PWM
            self.led_pin = Pin(self.led_pin_num, Pin.OUT)  # Set pin to digital output mode
            self.is_pwm_mode = False

        # Determine the digital state based on control mode
        state = (self.output_state == LED_OFF) ^ (self.ctrl_mode == CTRL_CATHODE)

        # Set the pin value to either high or low
        self.led_pin.value(0 if state else 1)  # Turn off or fully on

    def turn_on(self, delay_time=0):
        self.delay_time = delay_time
        self.led_mode = LED_MODE_ON
        self.led_state = LED_STATE_DELAY if delay_time > 0 else LED_STATE_ON_OFF
        self.last_time = time.ticks_ms()
        self.loop()

    def turn_off(self, delay_time=0):
        self.delay_time = delay_time
        self.led_mode = LED_MODE_OFF
        self.led_state = LED_STATE_DELAY if delay_time > 0 else LED_STATE_ON_OFF
        self.last_time = time.ticks_ms()
        self.loop()

    def toggle(self, delay_time=0):
        self.delay_time = delay_time
        self.led_mode = LED_MODE_TOGGLE
        self.led_state = LED_STATE_DELAY if delay_time > 0 else LED_STATE_ON_OFF
        self.last_time = time.ticks_ms()
        self.loop()

    def fade(self, fade_from, fade_to, fade_time, delay_time=0):
        self.fade_from = fade_from
        self.fade_to = fade_to
        self.fade_time = fade_time
        self.delay_time = delay_time
        self.led_mode = LED_MODE_FADE
        self.last_time = time.ticks_ms()
        self.led_state = LED_STATE_DELAY if delay_time > 0 else LED_STATE_FADE
        self.loop()

    def blink(self, on_time, off_time, delay_time=0):
        self.set_blink(on_time, off_time, delay_time)
        self.led_mode = LED_MODE_BLINK_FOREVER
        if self.led_state == LED_STATE_IDLE:
            self.led_state = LED_STATE_DELAY if delay_time > 0 else LED_STATE_BLINK
            self.output_state = LED_ON
            self.last_time = time.ticks_ms()
        self.loop()

    def blink_with_duration(self, on_time, off_time, blink_time, delay_time=0):
        self.set_blink(on_time, off_time, delay_time)
        self.blink_time_period = blink_time
        self.led_mode = LED_MODE_BLINK_PERIOD
        if self.led_state == LED_STATE_IDLE:
            self.led_state = LED_STATE_DELAY if delay_time > 0 else LED_STATE_BLINK
            self.output_state = LED_ON
            self.last_time = time.ticks_ms()
            self.blink_timer = time.ticks_ms()
        self.loop()

    def blink_n_times(self, on_time, off_time, number_of_times, delay_time=0):
        self.set_blink(on_time, off_time, delay_time)
        self.blink_number_of_times = number_of_times
        self.led_mode = LED_MODE_BLINK_NUM_TIME
        if self.led_state == LED_STATE_IDLE:
            self.led_state = LED_STATE_DELAY if delay_time > 0 else LED_STATE_BLINK
            self.output_state = LED_ON
            self.last_time = time.ticks_ms()
            self.blink_counter = 1
        self.loop()

    def cancel(self):
        self.turn_off()

    def get_on_off(self):
        return self.output_state

    def get_state(self):
        if self.led_state == LED_STATE_DELAY:
            return LED_DELAY
        elif self.led_state == LED_STATE_FADE:
            return LED_FADING
        elif self.led_state == LED_STATE_BLINK:
            return LED_BLINKING
        else:
            return LED_IDLE

    def loop(self):
        if self.led_state == LED_STATE_IDLE:
            return

        if self.led_state == LED_STATE_DELAY:
            if time.ticks_diff(time.ticks_ms(), self.last_time) >= self.delay_time:
                if self.led_mode in (LED_MODE_OFF, LED_MODE_ON, LED_MODE_TOGGLE):
                    self.led_state = LED_STATE_ON_OFF
                elif self.led_mode == LED_MODE_FADE:
                    self.led_state = LED_STATE_FADE
                elif self.led_mode in (LED_MODE_BLINK_FOREVER, LED_MODE_BLINK_PERIOD, LED_MODE_BLINK_NUM_TIME):
                    self.led_state = LED_STATE_BLINK
                    self.output_state = LED_ON
                self.last_time = time.ticks_ms()

        if self.led_state == LED_STATE_ON_OFF:
            if self.led_mode == LED_MODE_OFF:
                self.output_state = LED_OFF
            elif self.led_mode == LED_MODE_ON:
                self.output_state = LED_ON
            elif self.led_mode == LED_MODE_TOGGLE:
                self.output_state = LED_OFF if self.output_state == LED_ON else LED_ON
            self.led_state = LED_STATE_IDLE

        if self.led_state == LED_STATE_FADE:
            progress = time.ticks_diff(time.ticks_ms(), self.last_time)
            if progress <= self.fade_time:
                self.brightness = int((progress * (self.fade_to - self.fade_from)) / self.fade_time) + self.fade_from
            else:
                self.led_state = LED_STATE_IDLE
                self.output_state = LED_OFF

        if self.led_state == LED_STATE_BLINK:
            if self.output_state == LED_OFF and time.ticks_diff(time.ticks_ms(), self.last_time) >= self.blink_off_time:
                self.output_state = LED_ON
                self.last_time = time.ticks_ms()
                self.blink_counter += 1
            elif self.output_state == LED_ON and time.ticks_diff(time.ticks_ms(), self.last_time) >= self.blink_on_time:
                self.output_state = LED_OFF
                self.last_time = time.ticks_ms()
                self.blink_counter += 1

            if self.led_mode == LED_MODE_BLINK_PERIOD:
                if time.ticks_diff(time.ticks_ms(), self.blink_timer) >= self.blink_time_period:
                    self.output_state = LED_OFF
                    self.led_state = LED_STATE_IDLE
            elif self.led_mode == LED_MODE_BLINK_NUM_TIME:
                if self.blink_counter >= 2 * self.blink_number_of_times:
                    self.output_state = LED_OFF
                    self.led_state = LED_STATE_IDLE

        if self.led_state == LED_STATE_FADE:
            self.update_analog()
        else:
            self.update_digital()
