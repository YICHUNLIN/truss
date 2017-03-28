#encoding = utf-8

from .shape import Shape
from Truss.point import Point
from tkinter import *


class Triangle(Shape):
	def __init__(self, canvas, p1, p2, name, size = 10):
		super().__init__(canvas, p1, p2, name, size)
		self.points = []
		self.points.append(p1)
		self.points.append(Point(self.p2.x+self.size, self.p2.y))
		self.points.append(Point(self.p2.x - self.size, self.p2.y))
	def draw(self):
		#self.trans(-90)
		#self.shapeShape = self.canvas.create_polygon(self.p1.x, self.p1.y, self.p2.x+self.size, self.p2.y, self.p2.x - self.size, self.p2.y,outline="black",fill="red")
		self.shapeShape = self.canvas.create_polygon(self.points[0].x,self.points[0].y,self.points[1].x,self.points[1].y,self.points[2].x,self.points[2].y,outline="black",fill="red")
		
	def trans(self,r):
		for p in self.points:
			#p.oriTrans(Point(50,650),100)
			print(p.__str__())
			p.rotate(r)
			print(p.__str__())


