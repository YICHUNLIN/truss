#encoding = utf-8


class Point(object):
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x = x
        self.y = y
    def ps(self):
        print("(%.2lf, %.2lf)" % (self.x, self.y))