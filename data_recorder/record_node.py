#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
from sensor_msgs.msg import CompressedImage

def listener():
    rospy.init_node('data_record_node')

    last_steering = 0
    last_throttle = 0

    def steering_callback(msg):
        last_steering = msg.data
    rospy.Subscriber('/control/steering', Float64, steering_callback)

    def throttle_callback(msg):
        last_throttle = msg.data
    rospy.Subscriber('/control/throttle', Float64, throttle_callback)

    def img_callback(msg):
        # save msg.data using timestampe , into records/IMG/
        # create csv records/driving_log.csv, 
        # save image filename and last_steering into csv
        pass

    rospy.Subscriber('image/compressed', CompressedImage, img_callback)

    rospy.spin()


if __name__=="__main__":
    listener()


