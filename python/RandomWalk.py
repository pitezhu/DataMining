#随机漫步
from random import choice

class RandomWalk():
    def __init__(self,point=5000):
        self.point=point
        self.xvalues=[0]
        self.yvalues=[0]

    def Fill_Walk(self):
        while len(self.xvalues)<self.point:
            xdir=choice([1,-1])
            xdis=choice([0,1,2,3,4])
            xstep=xdir*xdis

            ydir=choice([1,-1])
            ydis=choice([0,1,2,3,4])
            ystep=ydir*ydis
            
            if xstep==0 and ystep==0:
                continue
            next_x=self.xvalues[-1]+xstep
            next_y=self.yvalues[-1]+ystep

            self.xvalues.append(next_x)
            self.yvalues.append(next_y)

        

