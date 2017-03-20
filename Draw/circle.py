#encoding = utf-8

from .shape import Shape
from Truss.point import Point
from tkinter import *

# 定義圓
class Circle(Shape):
    def __init__(self, canvas, p1, p2, name):
        super().__init__(canvas, p1, p2, name)

    def draw(self):
        print("draw circle")
        self.shapeShape = self.canvas.create_oval(self.p1.x - 15, self.p1.y - 15, self.p2.x + 15, self.p2.y  + 15, fill = "red")
        self.shapeLabel = self.canvas.create_text(self.p1.x, self.p1.y, text = self.name)

    def touch(self, event):
        super().drop(event)
        if((self.p1.x - 10 < event.x) and (self.p1.y - 10 < event.y)) and ((self.p2.x + 10 > event.x) and (self.p2.y + 10 > event.y)):
            self.isSelect = True
        else:
            self.isSelect = False

        
    def motion(self, event):
        super().motion(event)

        if self.isSelect:
            mpoint = Point(event.x, event.y)
            self.p1 = self.p2 = mpoint
            self.canvas.delete(self.shapeShape)
            self.canvas.delete(self.shapeLabel)
            self.draw()