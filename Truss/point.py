#encoding = utf-8

import math

class Point(object):
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def ps(self):
        print("(%.2lf, %.2lf)" % (self.x, self.y))

    def rotate(self, theta):
    	self.x = self.x * math.cos(theta) + self.y * math.sin(theta)
    	self.y = self.x * math.sin(theta) + self.y * math.cos(theta)

    def oriTrans(self, target, scale):
    	self.x = target.x + self.x * scale
    	self.y = target.y - self.y * scale

    def __str__(self):
    	return "(%.2lf, %.2lf)" % (self.x, self.y)

#Point( self.cartori.x + target.x  * self.scale, self.cartori.y - target.y * self.scale)