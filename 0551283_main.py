#encoding = utf-8
'''
Author  Vic Lin

at 2017/3/5

'''

import math
from tkinter import *
import random
import configparser

# 一個座標
class Point(object):
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def ps(self):
        print("(%.2lf, %.2lf)" % (self.x, self.y))

# 一個節點
class Node(object):
    # 結點名稱
    name = ""
    # 連接桿件
    connect = []
    def __init__(self, point , name):
        self.point = point
        self.name = name
        #print("node %s (%.2lf,%.2lf)" % (self.name, self.point.x, self.point.y))

    # 兩個結點的距離(長度)
    def distance(self,anotherNode):
        return math.sqrt((anotherNode.point.x - self.point.x)*(anotherNode.point.x - self.point.x) + (anotherNode.point.y - self.point.y)*(anotherNode.point.y - self.point.y))

    # 加入一個桿件
    def addmember(self, member):
        self.connect.append(member)



# 一個趕件
class Member(object):
    # 桿件名稱
    name = ""
    # 桿件長度
    length = 0.0
    # 桿件斷面
    area = 0.0
    # 彈性模數
    elm = 0.0
    # E*A/L
    eal = 0.0
    # 始 -> 末, 名字 ,內徑, 外徑
    def __init__(self, startnode, endnode, name, iR, oR, elm = 2.04*1000000):

        self.startNode = startnode
        self.endNode = endnode
        self.name = name
        self.calLength()
        self.area = 3.1415926 * abs((oR/2)*(oR/2) - (iR/2)*(iR/2))
        self.elm = elm
        self.eal = self.elm * self.area / self.length

    # 計算長度
    def calLength(self):
        self.length = self.startNode.distance(self.endNode)

    # 把自己加進 node
    def addSelftoNodes(self):
        self.startNode.addmember(self)
        self.endNode.addmember(self)






# 一組桁架
class Truss(object):
    infile = ""
    outfile = ""
    conf = ""
    # 所有節點
    nodes = []
    # 所有桿件
    members = []
    def __init__(self, conf = "config.ini"):
        self.conf = conf
        self.getConfig()

    def getConfig(self):
        try:
            config=configparser.ConfigParser()
            config.read(self.conf)
            self.infile = config['setting']['filein']
            self.outfile = config['setting']['fileout']
        except:
            print("Config error")

    # 加入一個節點
    def addnode(self, node):
        self.nodes.append(node)

    # 加入一個桿件
    def addmember(self, member):
        member.addSelftoNodes()
        self.members.append(member)

    # 印出所有元件
    def components(self):
        print("------Nodes------")
        for n in self.nodes:
            print("%s(%.5lf,%.5lf)" % (n.name, n.point.x, n.point.y))

        print("-----Members------")
        for m in self.members:
            print("%s - (%s,l %.5lf, a %.5lf, E*A/L %.5lf) - %s " % (m.startNode.name ,m.name, m.length, m.area, m.eal, m.endNode.name))

    # 從檔案取得桁架資訊
    def getTrussFromFile(self):
        try:
            f = open(self.infile,"r")
            while True:
                line = f.readline()
                if not line:
                    break
                arr = line.replace('\n',"").split(",")
                if  'n' in arr[0]:
                    self.addnode(Node(Point(float(arr[1]),float(arr[2])),arr[0]))
                elif( 'm' in arr[0]):
                    ns = self.getNodeByName(arr[1])
                    ne = self.getNodeByName(arr[2])
                    self.addmember(Member(ns,ne,arr[0],float(arr[3]),float(arr[4])))
            f.close()
        except:
            print("File exception")

    # 將趕件寫入檔案
    def writeMemberToFile(self):
        try:
            f = open(self.outfile, "w")
            for m in self.members:
                f.write("%s,L %.5lf,A %.5lf,E*A/L %.5lf\n" % (m.name, m.length, m.area, m.eal))
            f.close()
        except:
            print("File exception")

    # 根據名字取得節點
    def getNodeByName(self, name):
        for n in self.nodes:
            if n.name == name:
                return n
        return None

    # 排序
    def sortMember(self):
        for i in range(0, len(self.members)):
            for j in range(0, len(self.members)):
                # 去除英文字
                t1 = int(self.members[i].name.replace("m",""))
                t2 = int(self.members[j].name.replace("m",""))
                if  t1 < t2:
                    tmp = self.members[j]
                    self.members[j] = self.members[i]
                    self.members[i] = tmp    


# 定義形狀
class Shape(object):

    def __init__(self, canvas, p1, p2, name):
        self.p1 = p1
        self.p2 = p2
        self.canvas = canvas
        self.name = name

    def draw(self):
        print("draw shape")

# 定義線
class Line(Shape):
    def __init__(self, canvas, p1, p2, name):
        super().__init__(canvas, p1, p2, name)

    def draw(self):
        print("draw line")
        self.canvas.create_line((self.p1.x, self.p1.y, self.p2.x, self.p2.y),width = 2)
        self.canvas.create_text(self.p1.x + (self.p2.x - self.p1.x)/3, self.p1.y + (self.p2.y - self.p1.y)/3, font=("Purisa", 18), text = self.name, fill="blue")

# 定義圓
class Circle(Shape):
    def __init__(self, canvas, p1, p2, name):
        super().__init__(canvas, p1, p2, name)

    def draw(self):
        print("draw circle")
        self.canvas.create_oval(self.p1.x - 15, self.p1.y - 15, self.p2.x + 15, self.p2.y  + 15, fill = "red")
        self.canvas.create_text(self.p1.x, self.p1.y, text = self.name)



# 畫 桁架
class DrawTruss(object):

    shapes = []
    # 桁架 放大倍率。節點大小
    def __init__(self, truss, scale = 100, nodeSize = 15, linewid = 2):
        self.truss = truss
        self.cartori = Point(50,650)
        self.scale = scale
        self.nodeSize = nodeSize
        self.linewid = linewid

    # 初始化 畫布
    def initCanvas(self):
        self.root = Tk()
        self.root.geometry("1000x1000")
        self.canvas = Canvas(self.root)
        self.canvas['width'] = 1000
        self.canvas['height'] = 1000
        self.canvas.pack()

    # 產生形狀
    def createShapes(self):
        # 從 桿件產生
        for m in self.truss.members:
            sp = self.locationTranslation(m.startNode.point)
            ep = self.locationTranslation(m.endNode.point)
            self.shapes.append(Line(self.canvas, sp, ep, m.name))
        # 從 節點產生
        for n in self.truss.nodes:
            target = n.point
            screenPoint = self.locationTranslation(target)
            self.shapes.append(Circle(self.canvas, screenPoint, screenPoint, n.name))


    # 座標轉換  轉 螢幕座標
    def locationTranslation(self, target):
        return Point( self.cartori.x + target.x  * self.scale, self.cartori.y - target.y * self.scale)

    # 畫圖
    def drawShapes(self):
        self.createShapes()
        for shape in self.shapes:
            shape.draw()
        self.root.mainloop()

def main():
    
    t = Truss(conf="config.ini")
    t.getTrussFromFile()
    t.sortMember()
    t.components()
    t.writeMemberToFile()
    dt = DrawTruss(t, scale = 200, nodeSize = 10)
    dt.initCanvas()
    dt.drawShapes()
    
    


if __name__ == "__main__":
    main()
