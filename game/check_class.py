import pygame,math
pygame.init()
class Hero:
    def __init__(self,window,display,path,x,y):
        self.window=window
        self.path=path
        self.x=x
        self.y=y
        self.last_dir = 'right'
        self.counter=0
        self.up=False
        self.f=False
        self.on_ground=False
        self.battle=False
        self.battle2=False
        self.bridge=False
        self.ladder=False
        self.climb_check=0
        self.key=[]
        self.condition=['idleright']
        self.center=[display.current_w//2-70,display.current_h//2-60]
        self.center_hero=[display.current_w//2,display.current_h//2+120]
        self.v = 20
        self.v2 = 0
        self.g = 1
    def animation(self,tuple,speed):
        self.count=len(tuple)*speed
        if self.counter<self.count:
            self.image=tuple[self.counter//speed]
            self.counter+=1
        else:
            self.counter=0
            if self.battle:self.battle=False
            if self.battle2:self.battle2=False
        self.rect=self.image.get_rect(bottomleft=(self.x,self.y))
        self.window.blit(self.image,self.rect)
    def move(self,matrix,speed,blocks,enviroment,ladder,house_rect,arrows,fire_rect,bg_rect):
        if not self.ladder:
            if speed>0:
                if matrix[self.center[1] // 60][(self.center[0] + 95) // 60] not in blocks.keys() and matrix[(self.center[1] + 60) // 60][(self.center[0] + 95) // 60] not in blocks.keys()\
                        and matrix[(self.center[1] + 119) // 60][(self.center[0] + 95) // 60] not in blocks.keys():
                    self.center[0]+=5
                    if abs(self.x+50+5-self.center_hero[0])<200:self.x += 5
                    else:
                        for i in blocks.values():
                            for g in i[1]:
                                if i[1] != []:g.x-=5
                        for i in enviroment.values():
                            for g in i[1]:
                                if i[1] != []:g.x-=5
                        for i in ladder:i.x-=5
                        for i in house_rect: i.x-=5
                        for i in fire_rect: i.x -= 5
                        for i in arrows: i[0].x-=5
                        for i in bg_rect:
                            for g in range(len(i)):
                                i[g].x-=g+1
            else:
                if matrix[self.center[1] // 60][(self.center[0]+5) // 60] not in blocks.keys() and matrix[(self.center[1] + 60) // 60][(self.center[0]+5) // 60] not in blocks.keys() \
                        and matrix[(self.center[1] + 119) // 60][(self.center[0]+5) // 60] not in blocks.keys():
                    self.center[0] -= 5
                    if abs(self.x+50-5-self.center_hero[0])<200:self.x -= 5
                    else:
                        for i in blocks.values():
                            for g in i[1]:
                                if i[1] != []:g.x+=5
                        for i in enviroment.values():
                            for g in i[1]:
                                if i[1] != []:g.x+=5
                        for i in ladder: i.x += 5
                        for i in house_rect: i.x += 5
                        for i in fire_rect: i.x += 5
                        for i in arrows: i[0].x+=5
                        for i in bg_rect:
                            for g in range(len(i)):
                                i[g].x+=g+1
    def fall(self,matrix,blocks,enviroment,ladder,house_rect,arrows,fire_rect):
        if not self.up:
            self.on_ground=False
            self.v2 += self.g
            if self.bridge or matrix[(self.center[1] + self.v2 + 120) // 60][(self.center[0]+10) // 60] not in blocks.keys() and matrix[(self.center[1] + self.v2 + 120) // 60][(self.center[0] + 90) // 60] not in blocks.keys() and \
                    matrix[(self.center[1] + self.v2 + 120) // 60][(self.center[0] + 35) // 60] not in blocks.keys() and matrix[(self.center[1] + self.v2 + 120) // 60][(self.center[0] + 65) // 60] not in blocks.keys():
                self.f=True

                self.center[1]+=self.v2
                if abs(self.y +60 + self.v2 - self.center_hero[1]) < 150:self.y += self.v2
                else:
                    for i in blocks.values():
                        for g in i[1]:
                            if i[1] != []:g.y-=self.v2
                    for i in enviroment.values():
                        for g in i[1]:
                            if i[1] != []:g.y-=self.v2
                    for i in ladder: i.y -= self.v2
                    for i in house_rect: i.y -= self.v2
                    for i in fire_rect: i.y -= self.v2
                    for i in arrows: i[0].y -= self.v2
                if matrix[self.center[1] // 60][(self.center[0]+50) // 60]=='-' or matrix[self.center[1] // 60][(self.center[0]+50) // 60]=='<' or \
                        matrix[self.center[1] // 60][(self.center[0]+50) // 60]=='>':
                    self.bridge=False
            else:
                while matrix[(self.center[1] + 120) // 60][(self.center[0]+10) // 60] not in blocks.keys() and matrix[(self.center[1] + 120) // 60][(self.center[0] + 90) // 60] not in blocks.keys() and \
                        matrix[(self.center[1]+120) // 60][(self.center[0] + 35) // 60] not in blocks.keys() and matrix[(self.center[1]+120) // 60][(self.center[0] + 65) // 60] not in blocks.keys():
                    self.f=True
                    self.bridge=False
                    self.center[1]+=1
                    if abs(self.y + 61 - self.center_hero[1]) < 150:self.y += 1
                    else:
                        for i in blocks.values():
                            for g in i[1]:
                                if i[1] != []:g.y -= 1
                        for i in enviroment.values():
                            for g in i[1]:
                                if i[1] != []:g.y -= 1
                        for i in ladder: i.y -= 1
                        for i in house_rect: i.y -= 1
                        for i in fire_rect: i.y -= 1
                        for i in arrows: i[0].y -= 1
                else:
                    self.f=False
                    self.v2 = 0
                    self.on_ground=True
    def jump(self,matrix,blocks,enviroment,ladder,house_rect,arrows,fire_rect):
        if self.up:
            self.on_ground=False
            self.f=False
            self.v-=self.g
            if self.v>0:
                if matrix[self.center[1] // 60][(self.center[0]+50) // 60]=='-' or matrix[self.center[1] // 60][(self.center[0]+50) // 60]=='<' \
                        or matrix[self.center[1] // 60][(self.center[0]+50) // 60]=='>' or \
                        matrix[self.center[1]// 60][(self.center[0] + 50) // 60] not in blocks.keys():
                    self.center[1]-=self.v
                    if abs(self.y + 60 -self.v - self.center_hero[1]) < 150:self.y -= self.v
                    else:
                        for i in blocks.values():
                            for g in i[1]:
                                if i[1] != []:g.y += self.v
                        for i in enviroment.values():
                            for g in i[1]:
                                if i[1] != []:g.y += self.v
                        for i in ladder: i.y += self.v
                        for i in house_rect: i.y += self.v
                        for i in fire_rect: i.y += self.v
                        for i in arrows: i[0].y += self.v
                else:
                    while matrix[self.center[1] // 60][(self.center[0] + 50) // 60] not in blocks.keys():
                        self.center[1]-=1
                        if abs(self.y + 61 - self.center_hero[1]) < 150:self.y -= 1
                        else:
                            for i in blocks.values():
                                for g in i[1]:
                                    if i[1] != []:g.y += 1
                            for i in enviroment.values():
                                for g in i[1]:
                                    if i[1] != []:g.y += 1
                            for i in ladder: i.y += 1
                            for i in house_rect: i.y += 1
                            for i in fire_rect: i.y += 1
                            for i in arrows: i[0].y += 1
                    else:
                        self.v = 20
                        self.up = False
                        self.v2=0
            else:
                self.up=False
                self.v2=0
                self.v=20
    def climb(self,speed,blocks,enviroment,matrix,ladder,house_rect,arrows,fire_rect):
        if self.ladder:
            self.on_ground=False
            if speed>0:self.climb_check=110
            else:self.climb_check=130
            if matrix[(self.center[1] + self.climb_check) // 60][(self.center[0]+5) // 60]=='l' or matrix[(self.center[1] + self.climb_check) // 60][(self.center[0]+30) // 60]=='l' or \
                matrix[(self.center[1] + self.climb_check) // 60][(self.center[0]+60) // 60]=='l' or matrix[(self.center[1] + self.climb_check) // 60][(self.center[0]+95) // 60]=='l':
                self.center[1]-=speed
                for i in blocks.values():
                    for g in i[1]:
                        if i[1] != []:g.y += speed
                for i in enviroment.values():
                    for g in i[1]:
                        if i[1] != []:g.y += speed
                for i in ladder:i.y+=speed
                for i in house_rect: i.y += speed
                for i in fire_rect: i.y += speed
                for i in arrows: i[0].y += speed
            else:
                self.ladder=False
                if speed>0:self.up=True
    def correct_pos(self,ladder,blocks,enviroment,house_rect,arrows,fire_rect):
        if self.ladder:
            self.on_ground=False
            for g in ladder:
                if self.rect.colliderect(g):
                    if self.x+23 > g.x and abs(self.x+23 - g.x)>1:
                        if abs(self.x + 50 - 5 - self.center_hero[0]) < 200:self.x -= 5
                        else:
                            for i in blocks.values():
                                for g in i[1]:
                                    if i[1] != []: g.x += 5
                            for i in enviroment.values():
                                for g in i[1]:
                                    if i[1] != []: g.x += 5
                            for i in ladder: i.x += 5
                            for i in house_rect: i.x += 5
                            for i in fire_rect: i.x += 5
                            for i in arrows: i[0].x += 5
                        self.center[0] -= 5
                    if self.x+23 < g.x and abs(self.x+23 - g.x)>1:
                        if abs(self.x + 50 + 5 - self.center_hero[0]) < 200:self.x += 5
                        else:
                            for i in blocks.values():
                                for g in i[1]:
                                    if i[1] != []: g.x -= 5
                            for i in enviroment.values():
                                for g in i[1]:
                                    if i[1] != []: g.x -= 5
                            for i in ladder: i.x -= 5
                            for i in house_rect: i.x -= 5
                            for i in fire_rect: i.x -= 5
                            for i in arrows: i[0].x -= 5
                        self.center[0] += 5

class Arrow:
    def __init__(self,window,x,y,angle,g=1):
        self.window=window
        self.image=pygame.image.load('arrow.png').convert_alpha()
        self.x=x
        self.y=y
        self.rect=self.image.get_rect(center=(self.x,self.y))
        self.g=g
        self.angle=angle
        self.image_angle=0
        self.start_pos=self.previous_pos=[x,y]
        self.end=False
    def shot(self,tuple):
        self.anglex=30 * math.cos(math.acos((self.start_pos[0] - tuple[0]) /((self.start_pos[0] - tuple[0]) ** 2 + (self.start_pos[1] - tuple[1]) ** 2) ** 0.5))
        self.angley=30 * math.sin(math.asin((self.start_pos[1] - tuple[1]) /((self.start_pos[0] - tuple[0]) ** 2 + (self.start_pos[1] - tuple[1]) ** 2) ** 0.5))
        if not self.end:
            self.x-=self.anglex
            self.y-=self.angley-self.g
            self.g+=0.6
            if self.angley-self.g>0:
                if ((self.previous_pos[0] - self.x) ** 2 + (self.previous_pos[1] - self.y) ** 2) ** 0.5 > 1: self.image_angle=math.acos((self.x - self.previous_pos[0]) / ((self.previous_pos[0] - self.x) ** 2 + (self.previous_pos[1] - self.y) ** 2) ** 0.5)
            else:
                if ((self.previous_pos[0] - self.x) ** 2 + (self.previous_pos[1] - self.y) ** 2) ** 0.5 > 1: self.image_angle = -1*math.acos((self.x - self.previous_pos[0]) / ((self.previous_pos[0] - self.x) ** 2 + (self.previous_pos[1] - self.y) ** 2) ** 0.5)
            self.previous_pos=[self.x,self.y]
            self.image2=pygame.transform.rotate(self.image,math.degrees(self.image_angle)).convert_alpha()
        self.rect=self.image2.get_rect(center=(self.x,self.y))
        self.window.blit(self.image2,self.rect)

class Object:
    def __init__(self,window,path,x,y):
        self.window = window
        self.path = path
        self.x = x
        self.y = y
        self.counter=0
    def animation(self,tuple,speed):
        self.count=len(tuple)*speed
        if self.counter<self.count:
            self.image=tuple[self.counter//speed]
            self.counter+=1
        else:self.counter=0
        self.rect=self.image.get_rect(bottomleft=(self.x,self.y))
        self.window.blit(self.image,self.rect)

class Background:
    def __init__(self,window,path,x,y):
        self.window = window
        self.path = path
        self.x = x
        self.y = y
        self.counter=0
        self.up=True
    def animation(self,tuple,speed):
        self.count=len(tuple)*speed
        if self.up:
            if self.counter < self.count:
                self.image=tuple[self.counter//speed]
                self.counter+=1
            else:
                self.counter=self.count-1
                self.up=False
        else:
            if self.counter > 0:
                self.image = tuple[self.counter // speed]
                self.counter -= 1
            else: self.up=True
        self.rect=self.image.get_rect(bottomleft=(self.x,self.y))
        self.window.blit(self.image,self.rect)

class Enemy:
    def __init__(self):
        pass

class FPS:
    def __init__(self, window, color = (0, 255, 0), pos = (20, 20), fontName = 'Arial', fontSize = 30):
        self.window = window
        self.color = color
        self.pos = pos
        self.font = pygame.font.SysFont(fontName, fontSize)
    def draw(self, fps):
        self.fps = str(int(fps))
        self.text = self.font.render('FPS: '+self.fps, True, pygame.Color(self.color))
        self.window.blit(self.text, self.pos)