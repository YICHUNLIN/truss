#encoding = utf-8
from Truss.truss import Truss
from Draw.drawTruss import DrawTruss
from tkinter import *
def main():
    
    t = Truss(conf="config.ini")
    #t.getTrussFromFile()
    t.getTruss()
    
    t.sortMember()
    t.components()
    #t.writeMemberToFile()
    t.setMemberToFile()
    dt = DrawTruss(t, scale = 200)
    dt.initCanvas()
    dt.drawShapes()
    
    

#-----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
