"""
集成类问题处理器
1.猜拳模拟器
"""
import math
import random
from graphics import *
from fisheat import *
from class1 import caiquan,Button



def bott4use():
    try:
        fish_game()
    except SystemExit:
        pass
    
def bott3use(): # 第三个按钮的功能
    win= GraphWin("求斜边",400,400)
    text1_a=Text(Point(35,100),"请输入第一条直角边：")
    text1=Entry(Point(200,100),10)
    text2_a=Text(Point(35,200),"请输入第二条直角边：")
    text2=Entry(Point(200,200),10)
    text1_a.draw(win)
    text2_a.draw(win)
    text1.draw(win)
    text2.draw(win)
    botter=Button(win,Point(200,350),70,40,"完成")
    botter.activate()
    endText=Text(Point(200,250),"点击空白处退出")
    endText.draw(win)
    point=win.getMouse()  #用户点击的点获取
    side1,side2 =text1.getText(),text2.getText()
    if botter.clicked(point): # 判断是否点击了按钮
        text1_a.undraw()
        text2_a.undraw()
        text1.undraw()
        text2.undraw()
        botter.cachu()
        a,b=int(side1),int(side2) 
        ending = math.sqrt(a**2+b**2)  #计算结果
        text2_a=Text(Point(200,150),"斜边长为{:.2f}".format(ending)) #显示计算结果在屏幕上
        text2_a.draw(win)
        win.getMouse()
        win.close()
    else:
         win.getMouse()
         win.close()
         
         
def bott2use():
    win= GraphWin("字符串对比",400,400)
    end=[]
    text1_a=Text(Point(35,100),"第一列：")
    text1=Entry(Point(200,100),30)
    text2_a=Text(Point(35,200),"第二列：")
    text2=Entry(Point(200,200),30)
    endText=Text(Point(200,250),"点击空白处退出")
    endText.draw(win)
    text1_a.draw(win)
    text2_a.draw(win)
    text1.draw(win)
    text2.draw(win)
    botter=Button(win,Point(200,350),70,40,"完成")
    botter.activate()
    point=win.getMouse()
    if botter.clicked(point):
        text1.undraw()
        text2.undraw()
        text1_a.undraw()
        text2_a.undraw()
        botter.cachu() 
        user1=text1.getText()
        user2=text2.getText()
        if len(user1)==len(user2): #判断输入字符是否长度相等
            for i in range(len(user1)): #逐渐增大
                if user1[i]==user2[i]: #字符是否相等
                    continue
                else:
                    end.append(i+1)  #字符不相等，则记录位置
        else:
            error=Text(Point(200,200),"请确认字符数量相等")
            error.draw(win)
            win.getMouse()
            win.close()
        if end: #end如果为空则为FALSE，不为空则为TRUE
            c=map(str,end) #MAP()会根据提供的函数对指定序列做映射。将列表内的数字变为字符串
            ending=",".join(c)
            endText=Text(Point(200,200),"在第{}处有错误".format(ending))
            endText.draw(win)
            win.getMouse()
            win.close()
        else:
            endText=Text(Point(200,200),"无错误，点击空白处退出")
            endText.draw(win)
            win.getMouse()
            win.close()
    else:
        win.close()#点击空白处退出
    
       
    
    
            
    
def bott1use():
    win= GraphWin("猜拳模拟器",400,400)
    bott1 = Button(win,Point(50,50),70,40,"石头")
    bott1.activate()
    bott2 = Button(win,Point(100,100),70,40,"剪刀")
    bott2.activate()
    bott3 = Button(win,Point(150,150),70,40,"布")
    bott3.activate()
    point= win.getMouse() 
    if bott1.clicked(point): #点击石头，剪刀，布分别对应 1,2,3，初始化后在类.winer中检测
         cq=caiquan(1)
         end=cq.winer()
    elif bott2.clicked(point):
         cq=caiquan(2)
         end=cq.winer()
    elif bott3.clicked(point):
         cq=caiquan(3)
         end=cq.winer()
    else:
        pass
    
    message=Text(Point(300,300),end)
    message.draw(win)
    win.getMouse()
    win.close()
           
  
      
def main():
    try:
        while True: #无限循环以实现每次一个窗口，且由用户决定是否退出。
            win=GraphWin("功能菜单",600,600)
            Texte=Text(Point(300,300),"点击空白处退出")
            Texte.draw(win)
            bott1 = Button(win,Point(150,150),70,40,"猜拳模拟")
            bott1.activate()
            bott2 = Button(win,Point(450,450),70,40,"列表对比")
            bott2.activate()
            bott3 = Button(win,Point(150,450),140,40,"直角三角形求斜边")
            bott3.activate()
            bott4 = Button(win,Point(450,150),140,40,"大鱼吃小鱼")
            bott4.activate()
            point_user = win.getMouse()
            """
            判断点击了哪一个按钮
            """
            if bott1.clicked(point_user):
                win.close()
                bott1use()
                continue
            elif bott2.clicked(point_user):
                
                win.close()
                bott2use()
                continue
            elif bott3.clicked(point_user):
                win.close()
                bott3use()
                continue
            elif bott4.clicked(point_user):
                win.close()
                bott4use()
                continue
            else:
                break 
    except GraphicsError:
        win.close()
        
        
        
        
    win.close()
main()
    
