#encoding = utf-8
from .node import Node
from .point import Point

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
    # 始 -> 末, 名字 ,內徑, 外徑, e
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
