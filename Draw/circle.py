#encoding = utf-8

from .shape import Shape
from Truss.point import Point
from tkinter import *

# 定義圓
class Circle(Shape):
    def __init__(self, canvas, p1, p2, name, size = 10):
        super().__init__(canvas, p1, p2, name, size)

    # 畫圓
    def draw(self):
        print("draw circle")
        self.shapeShape = self.canvas.create_oval(self.p1.x - self.size, self.p1.y - self.size, self.p2.x + self.size, self.p2.y  + self.size, fill = "red")
        self.shapeLabel = self.canvas.create_text(self.p1.x, self.p1.y, text = self.name)

    # 觸碰事件
    def touch(self, event):
        super().drop(event)
        if((self.p1.x - self.size < event.x) and (self.p1.y - self.size < event.y)) and ((self.p2.x + self.size > event.x) and (self.p2.y + self.size > event.y)):
            self.isSelect = True
        else:
            self.isSelect = False

    # 滑鼠移動事件
    def motion(self, event):
        super().motion(event)

        if self.isSelect:
            mpoint = Point(event.x, event.y)
            self.p1 = self.p2 = mpoint
            self.canvas.delete(self.shapeShape)
            self.canvas.delete(self.shapeLabel)
            self.draw()