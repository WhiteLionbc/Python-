import random
import pygame
from classfish import Player,Shrimp,Fish2,Fish3
from pygame.locals import *
from sys import exit

def fish_game():
    pygame.init()
    # 创建一个窗口
    screen = pygame.display.set_mode((1000, 700),0,0)
    
    pygame.display.set_caption("Fish")
    #读取背景
    background = pygame.image.load("images/sea.jpg")
    leval=0
    pl=Player(leval)
    fishs=pl.fishs
    enemys=[]
    pygame.mouse.set_visible(False) 
    point = 0
    ec = 0
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                # 接收到退出时间后退出程序
                pygame.quit()
                exit()
      
         # 将背景图画上去        
        screen.blit(background, (0, 0))
        
        #敌人刷新位置随机,种类随机
        points=(-80,random.randrange(0,500))
        enemy_name=[Shrimp(points),Fish2(points),Fish3(points)]
        
        #玩家分数
        score_font = pygame.font.Font(None, 36)
        score_text = score_font.render('score: '+str(point), True, (0, 0, 0))
        text_rect = score_text.get_rect()
        text_rect.topleft = [800, 50]
        screen.blit(score_text, text_rect)
        
        
        
#        游戏难度设定，不同等级的玩家面对的敌人不同
        if leval <= 2:
            if ec%170 == 0:
                enemys.append(enemy_name[random.randrange(1)])
            elif ec%180==0:
                enemys.append(enemy_name[random.randrange(2)])
            elif ec%350==0:
                enemys.append(enemy_name[2])
                
        if leval >2:
            if ec%250 == 0:
                enemys.append(enemy_name[random.randrange(1)])
            elif ec%230==0:
                enemys.append(enemy_name[random.randrange(2)])
            elif ec%350==0:
                enemys.append(enemy_name[2])
                
        ec = ec + 1 #频率控制
        
        #碰撞效果处理
        for e in enemys:
            if pygame.sprite.collide_rect_ratio(0.8)(pl, e):#更改碰撞体积
                    #遇到虾
                    if e.id==0 and leval >=0 :
                        e.alive= False
                        point=point +1
                    else:
                        pass
                        
                    #遇到鱼
                    if e.id==1 and leval >1:
                        e.alive= False
                        point=point +2
                    elif e.id==leval:
                        pass
                    elif e.id > leval:
                        pl.alive=False
                    
                    #遇到大鱼
                    if e.id==2 and leval >2:
                        e.alive= False
                        point=point + 3
                    else:
                       pass
        #玩家状态判断
        if pl.alive:
            screen.blit(fishs[leval], pl.rect)
        else:
            break
      
        
        #画出敌人        
        for e in enemys:
            if e.alive:
                screen.blit(e.image, e.rect)
                if e.rect.right < 1000:
                    e.move()
                else:
                    enemys.remove(e)
            else:
                enemys.remove(e)
                    
           

        
            
        
        
        #分数决定玩家等级
        if point == 10 + 20*leval :
            if leval < 3:
                leval = leval + 1
            else:
                pass
           
            
        
    
        #玩家移动 
        keyState = pygame.key.get_pressed()
        
        if keyState[K_UP] or keyState[K_w]:
            pl.moveUp()
        elif keyState[K_DOWN] or keyState[K_s]:
            pl.moveDown()
        elif keyState[K_LEFT] or keyState[K_a]:
            pl.moveLeft()
        elif keyState[K_RIGHT] or keyState[K_d]:
            pl.moveRight()
        

        pygame.display.update()
    
    
    
    game_over = pygame.image.load("images/gameover.png")
        # 游戏 Game Over 后显示最终得分
    font = pygame.font.SysFont("SimHei", 32)
    text = font.render('最终得分: '+ str(point), True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    text1 = font.render('点击空白处退出 ',True, (255, 0, 0))
    text1_rect = text.get_rect()
    text1_rect.centerx = screen.get_rect().centerx-24
    text1_rect.centery = screen.get_rect().centery + 96
    screen.blit(game_over, (0, 0))
    screen.blit(text, text_rect)
    screen.blit(text1,text1_rect)
    pygame.mouse.set_visible(True) 
    # 显示得分并处理游戏退出
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                exit()
        pygame.display.update()
    
if __name__=='__main__':
    fish_game()
