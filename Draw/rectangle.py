#encoding = utf-8

from .shape import Shape
from Truss.point import Point
from tkinter import *


class Rectangle(Shape):
	def __init__(self, canvas, p1, p2, name, size = 10):
		super().__init__(canvas, p1, p2, name, size)

	
	def draw(self):
		self.shapeShape = self.canvas.create_rectangle(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill="red")
	
