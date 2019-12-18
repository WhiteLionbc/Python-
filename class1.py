import random
from graphics import *
class caiquan:#猜拳模拟器
    """
    猜拳类
    """
    def __init__(self,users):
          self.npc_shoushi= random.randrange(1,4)# 1石头，2剪刀，3布
          self.user= users
          
    def winer(self):     #胜利判断
         """
		 判断胜利返回结果
		 """
         if self.npc_shoushi==1 and self.user==2 :
              self.end="你输了,对方是石头"
              return self.end
         elif self.npc_shoushi==2 and self.user==3:
              self.end="你输了,对方是剪刀"
              return self.end
         elif self.npc_shoushi==3 and self.user ==1:
              self.end="你输了,对方是布"
              return self.end
         elif self.npc_shoushi==self.user:
              self.end="平局"
              return self.end
         else:
              self.end="你赢了"
              return self.end
            
    
class Button: 

    """
	一个按钮
	"""

    def __init__(self, win, center, width, height, label):
        """ 创建一个矩形按钮，例如:
        qb = Button(myWin, centerPoint, width, height, 'Quit') """ 

        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        "如果按钮被点击且点击在内部，则返回true"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "返回此按钮的标签字符串"
        return self.label.getText()

    def activate(self):
        "将此按钮设置为启用."
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        "将此按钮设置为禁用."
        self.label.setFill('darkgrey')
        self.rect.setWidth(1)
        self.active = False
        
    def cachu(self):
        "擦除按钮"
        self.rect.undraw()
        self.label.undraw()
# -*- coding: utf-8 -*-

