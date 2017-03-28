#encoding = utf-8
from Truss.truss import Truss
from Draw.drawTruss import DrawTruss
from tkinter import *



class MainClass:
    def __init__(self):
        print("Main inits")

    def getTruss(self):
        self.t = Truss(conf="config.ini")
        self.t.getTruss()
        self.t.sortMember()
        self.t.components()
        self.t.setMemberToFile()

    def getGUI(self):
        self.root = Tk()
        self.root.geometry("1000x1000")
        self.btn = Button(self.root, text ="Hello", command = self.e_helloCallBack)
        self.btn.pack()
        self.dt = DrawTruss(self.t, scale = 200)
        self.dt.initCanvas(self.root)
        #self.dt.drawShapes()
        self.root.mainloop()


    def e_helloCallBack(self):
        self.dt.drawShapes()


def main():
    mc = MainClass()
    mc.getTruss()
    mc.getGUI()

    '''
    t = Truss(conf="config.ini")
    #t.getTrussFromFile()
    t.getTruss()
    
    t.sortMember()
    t.components()
    #t.writeMemberToFile()
    t.setMemberToFile()
    root = Tk()
    root.geometry("1000x1000")
    btn = Button(root, text ="Hello", command = helloCallBack)
    btn.pack()
    dt = DrawTruss(t, scale = 200)
    dt.initCanvas(root)
    dt.drawShapes()
    root.mainloop()
    '''
def helloCallBack():
    print("xx")



#-----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
