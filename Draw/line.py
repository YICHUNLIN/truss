#encoding = utf-8
# 定義線
from .shape import Shape
from Truss.point import Point
from tkinter import *
class Line(Shape):
    def __init__(self, canvas, p1, p2, name):
        super().__init__(canvas, p1, p2, name)

    def draw(self):
        print("draw line")
        self.shapeShape = self.canvas.create_line((self.p1.x, self.p1.y, self.p2.x, self.p2.y),width = 2)
        self.shapeLabel = self.canvas.create_text(self.p1.x + (self.p2.x - self.p1.x)/3, self.p1.y + (self.p2.y - self.p1.y)/3, font=("Purisa", 18), text = self.name, fill="blue")

    def touch(self, event):
        self.isSelect = False