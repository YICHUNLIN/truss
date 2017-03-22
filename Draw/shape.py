#encoding = utf-8

from tkinter import *


# 定義形狀
class Shape(object):
    def __init__(self, canvas, p1, p2, name, size = 10):
        self.p1 = p1
        self.p2 = p2
        #canvas.bind("<Button-1>", self.drop)
        #canvas.bind('<Motion>', self.motion)
        self.canvas = canvas
        self.name = name
        self.shapeLabel = None
        self.shapeShape = None
        self.isSelect = False
        self.size = size
        
    def motion(self, event):
        print("motion")

    def touch(self, event):
        print("touch %s" % self.name)