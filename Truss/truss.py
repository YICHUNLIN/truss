# coding=utf-8


import random
import configparser
from .member import Member
from .node import Node
from .point import Point

# 一組桁架

class Truss(object):
    infile = ""
    outfile = ""
    conf = ""
    # 所有節點
    nodes = []
    # 所有桿件
    members = []
    # 檔案類型 ini or txt
    filetypeIsini = True
    def __init__(self, conf = "config.ini"):
        self.conf = conf
        self.getConfig()

    def getConfig(self):
        try:
            # 讀設定檔
            config=configparser.ConfigParser()
            config.read(self.conf)
            if config['conf']['filetype'] == "ini":
                self.infile = config['inifile']['filein']
                self.outfile = config['inifile']['fileout']
                self.filetypeIsini = True
            elif config['conf']['filetype'] == "txt":
                self.infile = config['txtfile']['filein']
                self.outfile = config['txtfile']['fileout']
                self.filetypeIsini = False

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
            print("File txt exception")

    # 從 ini 讀資料
    def getTrussFromini(self):
        try:
            inifile=configparser.ConfigParser()
            inifile.read(self.infile)
            ininodesTitles = inifile.options('nodes')
            inimembersTitles = inifile.options('members')
            for nn in ininodesTitles:
                anode = inifile['nodes'][nn]
                arr = anode.split(",")
                self.addnode(Node(Point(float(arr[0]),float(arr[1])),nn))
                #print(anode)

            for mm in inimembersTitles:
                amember = inifile['members'][mm]
                arr = amember.split(',')
                ns = self.getNodeByName(arr[0])
                ne = self.getNodeByName(arr[1])
                self.addmember(Member(ns,ne,mm,float(arr[2]),float(arr[3])))
            print(self.nodes)
            print(self.members)
        except:
            print("File ini exception")

    # 讀資料切換
    def getTruss(self):
        if self.filetypeIsini:
            self.getTrussFromini()
        else:
            self.getTrussFromFile()

    # 將趕件寫入檔案
    def writeMemberToFile(self):
        try:
            f = open(self.outfile, "w")
            for m in self.members:
                f.write("%s,L %.5lf,A %.5lf,E*A/L %.5lf\n" % (m.name, m.length, m.area, m.eal))
            f.close()
        except:
            print("File exception")

    def writeMembertoini(self):
        f = open(self.outfile, "w")
        cf = configparser.ConfigParser()
        cf.add_section('MemberResult')
        for m in self.members:
            cf.set('MemberResult',m.name,"L %.5lf,A %.5lf,E*A/L %.5lf" % (m.length, m.area, m.eal ))
        cf.write(f)
        f.close()

    # 寫資料切換
    def setMemberToFile(self):
        if self.filetypeIsini:
            self.writeMembertoini()
        else:
            self.writeMemberToFile()
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

