#encoding = utf-8


import math
from .point import Point

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


