#!/usr/bin/env python
from __future__ import division
import rospy
from std_msgs.msg import Float64
import time
import math
import Adafruit_PCA9685

FREQUENCY = 60
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(FREQUENCY)

def set_pwm_usec(channel, pulse_us):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= FREQUENCY
    pulse_length //= 4096     # 12 bits of resolution
    pulse_us //= pulse_length
    pwm.set_pwm(channel, 0, pulse_us)

def steering(value):
    maxpulse = 1220
    minpulse = 1780
    diff = maxpulse - minpulse
    current_pulse = int((value + 1) * 0.5 * diff + minpulse)
    set_pwm_usec(0, current_pulse)

def throttle(value):
    stop = 1500
    slow_forward = 1600
    full_forward = 2000
    slow_backward = 1300
    full_backward = 1000
    if (value > 0.01):
        set_pwm_usec(1, int(value * (full_forward-slow_forward) + slow_forward))
    elif (value < -0.01):
        set_pwm_usec(1, int((-value) * (full_backward-slow_backward) + slow_backward))
    else:
        set_pwm_usec(1, int(stop))

def listener():
    set_pwm_usec(1, 1500)
    set_pwm_usec(0, 1500)
    time.sleep(3)

    rospy.init_node('point1_control')

    def steering_callback(msg):
        steering(msg.data)
    rospy.Subscriber('/vision/control_suggestion/steering', Float64, steering_callback)

    def throttle_callback(msg):
        throttle(msg.data)
    rospy.Subscriber('/vision/control_suggestion/throttle', Float64, throttle_callback)

    print ('spinning')
    rospy.spin()
    print ('after spinning')


if __name__=="__main__":
    listener()

