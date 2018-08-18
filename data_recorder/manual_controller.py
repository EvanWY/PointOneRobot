#!/usr/bin/env python
import pygame, sys
import pygame.locals
import rospy
from std_msgs.msg import Float64

pygame.init()
BLACK = (0,1,0)
WIDTH = 400
HEIGHT = 300
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

windowSurface.fill(BLACK)    
pub = rospy.Publisher('/control/steering', Float64, queue_size=10)
rospy.init_node('manual_controller', anonymous=True)

while True:
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.K_1:
                pub.publish(-1)
            if event.key == pygame.K_2:
                pub.publish(-0.75)
            if event.key == pygame.K_3:
                pub.publish(-0.5)
            if event.key == pygame.K_4:
                pub.publish(-0.25)
            if event.key == pygame.K_5:
                pub.publish(0)
            if event.key == pygame.K_6:
                pub.publish(0.25)
            if event.key == pygame.K_7:
                pub.publish(0.5)
            if event.key == pygame.K_8:
                pub.publish(0.75)
            if event.key == pygame.K_9:
                pub.publish(1)
                



def talker():

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

# if __name__ == '__main__':
#     try:
#         talker()
#     except rospy.ROSInterruptException:
#         pass
