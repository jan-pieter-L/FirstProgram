from gpiozero import Button, LED
import time
from  signal import pause

button=  Button(26, bounce_time=0.05)
led_green = LED(22)
led_blue  = LED(27)
led_red   = LED(17)


leds = [ led_green, led_blue, led_red]
led_index = 0  # index of the active LED

# Ensure all LEDs start off
for led in leds:
    led.off()

def switch_led():
    global led_index
    # Turn all LEDs off
    for led in leds:
        led.off()

    # Turn on the next LED
    leds[led_index].on()

    # Move to next LED index (looping back to 0)
    led_index = (led_index + 1) % len(leds)

button.when_pressed = switch_led

pause()

