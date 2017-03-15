#encoding = utf-8


from tkinter import *
from tkinter import ttk
 
class TrussDraw:

	nodes = []

	# 笛卡爾座標 0 0 在 螢幕上是 200 800
	cartesian_ori_X = 200
	cartesian_ori_Y = 800

	def __init__(self, nodes = None):
		self.nodes = nodes


	def draw(self):
		root = Tk()
		#root.geometry("1000x1000")


		canvas = Canvas(root)
		canvas.grid(column=0, row=0, sticky='nwes')
		canvas.create_line((0, 0, 100, 100))

		root.mainloop()

	#def transCoordinate(self, cartx, carty):


def main():
	lasty, lastx = 0, 0

	def xy(event):
		nonlocal lasty, lastx
		lastx = event.x
		lasty = event.y

	def addLine(event):
		nonlocal lasty, lastx
		canvas.create_line((lastx, lasty, event.x, event.y))
		lasty = event.y
		lastx = event.x


	root = Tk()
	root.columnconfigure(0, weight=1)
	root.rowconfigure(0, weight=1)

	canvas = Canvas(root)
	canvas.grid(column=0, row=0, sticky='nwes')
	canvas.bind('<Button-1>', xy)
	canvas.bind('<B1-Motion>', addLine)
	root.mainloop()
 
 
def draw():

	root = Tk()
	#root.columnconfigure(0, weight=1)
	#root.rowconfigure(0, weight=1)

	canvas = Canvas(root)
	canvas.grid(column=0, row=0, sticky='nwes')
	canvas.create_line((0, 0, 100, 100))
	#canvas.bind('<Button-1>', xy)
	#canvas.bind('<B1-Motion>', addLine)
	root.mainloop()


if __name__ == '__main__':
	td = TrussDraw()
	td.draw()