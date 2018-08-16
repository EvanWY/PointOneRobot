# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import math
from tqdm import tqdm

# Import the PCA9685 module.
import Adafruit_PCA9685


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

FREQUENCY = 120

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(FREQUENCY)

# Helper function to make setting a servo pulse width simpler.
def pulse(channel, pulse_us):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= FREQUENCY
    pulse_length //= 4096     # 12 bits of resolution
    pulse_us //= pulse_length
    pwm.set_pwm(channel, 0, pulse_us)

def steering(value):
    maxpulse = 1780
    minpulse = 1200
    diff = maxpulse - minpulse
    current_pulse = int((value + 1) * 0.5 * diff + minpulse)
    pulse(0, current_pulse)

def duration(channel, dur, pulse1, pulse2):
    pulse(channel, pulse1)
    time.sleep(dur)
    pulse(channel, pulse2)

pulse(1, 1500)
pulse(0, 1500)

if __name__=="__main__":
    time.sleep(3)

    while True:
        steering(0.9*math.sin(time.time()*10))
        if (time.time() // 2 == 0):
            pulse(1, 1700)
        else:
            pulse(1, 1500)
        time.sleep(0.001)


