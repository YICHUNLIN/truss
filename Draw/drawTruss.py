#encoding = utf-8

from Truss.point import Point
from .shape import Shape
from .line import Line
from .circle import Circle
from Truss.truss import Truss
from tkinter import *
from .rectangle import Rectangle
from .triangle import Triangle
# 畫 桁架
class DrawTruss(object):

    shapes = []
    # 桁架 放大倍率。節點大小
    def __init__(self,truss, scale = 100, nodeSize = 10, linewid = 2):
        self.truss = truss
        self.cartori = Point(50,650)
        self.scale = scale
        self.nodeSize = nodeSize
        self.linewid = linewid

    # 初始化 畫布
    def initCanvas(self,root):
        self.root = root
        #self.root.geometry("1000x1000")
        self.canvas = Canvas(self.root)
        self.canvas['width'] = 1000
        self.canvas['height'] = 1000
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.drop)
        self.canvas.bind('<Motion>', self.motion)
        self.isDrop = False



    # 產生形狀
    def createShapes(self):
        # 從 桿件產生
        for m in self.truss.members:
            sp = self.locationTranslation(m.startNode.point)
            ep = self.locationTranslation(m.endNode.point)
            self.shapes.append(Line(self.canvas, sp, ep, m.name, size = int(m.area*1000)))
        # 從 節點產生
        for n in self.truss.nodes:
            target = n.point
            screenPoint = self.locationTranslation(target)
            self.shapes.append(Circle(self.canvas, screenPoint, screenPoint, n.name, size = 12))
        # test
        #self.shapes.append(Rectangle(self.canvas,Point(100,100),Point(140,120),""))
        #self.shapes.append(Triangle(self.canvas,Point(200,200),Point(200,230),"",size = 25))

    # 座標轉換  轉 螢幕座標
    def locationTranslation(self, target):
        return Point( self.cartori.x + target.x  * self.scale, self.cartori.y - target.y * self.scale)

    # 畫圖
    def drawShapes(self):
        self.createShapes()
        for shape in self.shapes:
            shape.draw()
        #self.root.mainloop()

    def drop(self, event):
        #print("drop shape")
        if self.isDrop:
            self.isDrop = False
        else:
            self.isDrop = True
        for s in self.shapes:
            s.touch(event)
            break

    def motion(self, event):
        if self.isDrop:
            for s in self.shapes:
                s.motion(event)
                break
                
    def clearCanvas(self):
        self.canvas.delete("all")
    '''
    1. 點Node
    2. 移動滑鼠
    3. 放開滑鼠
    '''
