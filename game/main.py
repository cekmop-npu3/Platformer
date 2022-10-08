import pygame,math
import ctypes, sys
from check_class import Hero,Object,Arrow,FPS,Background


pygame.init()
pygame.mixer.init()
window=pygame.display.set_mode((1920,1080))
display=pygame.display.Info()
dictionary={'idleright':[pygame.image.load(f'character_1/idle/warrior_Idle_{i+1}.png').convert_alpha() for i in range(6)],'idleleft':[pygame.image.load(f'character_1/idle/warrior_Idle_l_{i+1}.png').convert_alpha() for i in range(6)],
            'runright':[pygame.image.load(f'character_1/run/warrior_run_{i+1}.png').convert_alpha() for i in range(8)],'runleft':[pygame.image.load(f'character_1/run/warrior_run_l_{i+1}.png').convert_alpha() for i in range(8)],'jumpright':
            [pygame.image.load(f'character_1/jump/warrior_jump_{i+1}.png').convert_alpha() for i in range(3)],'jumpleft':[pygame.image.load(f'character_1/jump/warrior_jump_l_{i+1}.png').convert_alpha() for i in range(3)],'attackright':
            [pygame.image.load(f'character_1/attack/warrior_attack_{i+1}.png').convert_alpha() for i in range(9)],'attackleft':[pygame.image.load(f'character_1/attack/warrior_attack_l_{i+1}.png').convert_alpha() for i in range(9)],
            'fallright':[pygame.image.load(f'character_1/fall/warrior_fall_{i+1}.png').convert_alpha() for i in range(3)],'fallleft':[pygame.image.load(f'character_1/fall/warrior_fall_l_{i+1}.png').convert_alpha() for i in range(3)],
            'climbright':[pygame.image.load(f'character_1/climb/Warrior-Ladder-Grab_{i+1}.png').convert_alpha() for i in range(8)],'climbleft':[pygame.image.load(f'character_1/climb/Warrior-Ladder-Grab_{i+1}.png').convert_alpha() for i in range(8)],
            'climbidleright':[pygame.image.load(f'character_1/climb/Warrior-Ladder-Grab_1.png').convert_alpha()],'climbidleleft':[pygame.image.load(f'character_1/climb/Warrior-Ladder-Grab_1.png').convert_alpha()]}
dictionary2={'idleright':[pygame.image.load(f'character_2/idle/idle_1.png').convert_alpha()],'idleleft':[pygame.image.load(f'character_2/idle/idle_l_1.png').convert_alpha()],
             'runright':[pygame.image.load(f'character_2/run/run_{i+1}.png').convert_alpha() for i in range(8)],'runleft':[pygame.image.load(f'character_2/run/run_l_{i+1}.png').convert_alpha() for i in range(8)],
             'jumpright':[pygame.image.load(f'character_2/jump/jump_{i+1}.png').convert_alpha() for i in range(4)],'jumpleft':[pygame.image.load(f'character_2/jump/jump_l_{i+1}.png').convert_alpha() for i in range(4)],
             'fallright':[pygame.image.load(f'character_2/fall/fall_{i+1}.png').convert_alpha() for i in range(4)],'fallleft':[pygame.image.load(f'character_2/fall/fall_l_{i+1}.png').convert_alpha() for i in range(4)],
             'climbright':[pygame.image.load(f'character_2/idle/idle_1.png').convert_alpha() ],'climbleft':[pygame.image.load(f'character_2/idle/idle_l_1.png').convert_alpha()],
             'climbidleright':[pygame.image.load(f'character_2/idle/idle_1.png').convert_alpha()],'climbidleleft':[pygame.image.load(f'character_2/idle/idle_l_1.png').convert_alpha()],
             'attackright':[pygame.image.load(f'character_2/normal_attack/attack_{i+1}.png').convert_alpha() for i in range(11)],'attackleft':[pygame.image.load(f'character_2/normal_attack/attack_l_{i+1}.png').convert_alpha() for i in range(11)],
             'attack2right': [pygame.image.load(f'character_2/high_attack/attack_{i+1}.png').convert_alpha() for i in range(13)],'attack2left': [pygame.image.load(f'character_2/high_attack/attack_l_{i+1}.png').convert_alpha() for i in range(13)]}

# background
bg_images=[[pygame.image.load(f'background/animation/layer_1/{i+1}.png').convert_alpha() for i in range(45)],[pygame.image.load(f'background/animation/layer_2/{i+1}.png').convert_alpha() for i in range(45)],
           [pygame.image.load(f'background/animation/layer_3/{i+1}.png').convert_alpha() for i in range(45)],pygame.image.load(f'background/animation/layer_4/1.png').convert_alpha()]

bg_rect=[]
for i in range(2):
    bg_rect.append([Background(window,'background/animation/layer_1/1.png',3840*i-600,1080),Background(window,'background/animation/layer_2/1.png',3840*i-600,1080),Background(window,'background/animation/layer_3/1.png',3840*i-600,1080),
    pygame.image.load(f'background/animation/layer_4/1.png').convert_alpha().get_rect(x=3840*i-600,y=0)])
# background

blocks={'1':[pygame.image.load('tiles/grass_1.png').convert_alpha(),[]],'2':[pygame.image.load('tiles/grass_2.png').convert_alpha(),[]],'3':[pygame.image.load('tiles/cutted_ground1.png').convert_alpha(),[]],
        '4':[pygame.image.load('tiles/ground_4.png').convert_alpha(),[]],'5':[pygame.image.load('tiles/ground_6.png').convert_alpha(),[]],'6':[pygame.image.load('tiles/ground_7.png').convert_alpha(),[]],
        '7':[pygame.image.load('tiles/ground_5.png').convert_alpha(),[]],'8':[pygame.image.load('tiles/ground_2.png').convert_alpha(),[]],'9':[pygame.image.load('tiles/ground_1.png').convert_alpha(),[]],
        '!':[pygame.image.load('tiles/grass_ground1.png').convert_alpha(),[]],'?':[pygame.image.load('tiles/grass_ground2.png').convert_alpha(),[]],'&':[pygame.image.load('tiles/grass_3.png').convert_alpha(),[]],
        '%':[pygame.image.load('tiles/ground_hole1.png').convert_alpha(),[]],'@':[pygame.image.load('tiles/ground_hole2.png').convert_alpha(),[]],'^':[pygame.image.load('tiles/cutted_ground2.png').convert_alpha(),[]],
        'g':[pygame.image.load('tiles/ground_8.png').convert_alpha(),[]],'j':[pygame.image.load('tiles/ground_hole3.png').convert_alpha(),[]],
        'w':[pygame.image.load('tiles/under_root.png').convert_alpha(),[]],'<':[pygame.image.load('tiles/bridge1.png').convert_alpha(),[]],'-':[pygame.image.load('tiles/bridge2.png').convert_alpha(),[]],
        '>':[pygame.image.load('tiles/bridge3.png').convert_alpha(),[]],'k':[pygame.image.load('tiles/ground_3.png').convert_alpha(),[]],'n':[pygame.image.load('tiles/destroyed_grass1.png').convert_alpha(),[]],}
enviroment={'y':[pygame.image.load('enviroment/tree2.png').convert_alpha(),[]],'t':[pygame.image.load('enviroment/tree1.png').convert_alpha(),[]],
            'q':[pygame.image.load('tiles/root.png').convert_alpha(),[]],'a':[pygame.image.load('enviroment/grass1.png').convert_alpha(),[]],'b':[pygame.image.load('enviroment/grass2.png').convert_alpha(),[]],
            'c':[pygame.image.load('enviroment/grass3.png').convert_alpha(),[]],'d':[pygame.image.load('enviroment/tree3.png').convert_alpha(),[]],'D':[pygame.image.load('enviroment/tree4.png').convert_alpha(),[]]}

# variables
hero_choose='knight'
house=[pygame.image.load(f'house/house_{i+1}.png').convert_alpha() for i in range(6)]
house_rect=[]
fire=[pygame.image.load(f'fire/fire_{i+1}.png').convert_alpha() for i in range(8)]
fire_rect=[]
ladder_image=pygame.image.load('enviroment/ladder.png').convert_alpha()
ladder=[]
matrix=[]
row=[]
shoot=False
cursor_image=pygame.image.load('scope.png').convert_alpha()
hero=Hero(window,display,'character_1/idle/warrior_Idle_1.png',display.current_w//2-70,display.current_h//2-60)
fps=FPS(window)
arrows=[]
options=True
# variables

def listener():
    global hero,matrix,shoot,hero_choose
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                exit()
            if event.key==pygame.K_SPACE: hero.up=True
            if event.key==pygame.K_s:
                if matrix[(hero.center[1]+121)//60][(hero.center[0]+75)//60]=='<' or matrix[(hero.center[1]+121)//60][(hero.center[0]+75)//60]=='-' \
                or matrix[(hero.center[1]+121)//60][(hero.center[0]+75)//60]=='>': hero.bridge=True
            if event.key==pygame.K_e:
                for g in ladder:
                    if hero.rect.colliderect(g): hero.ladder=True
            if event.key==pygame.K_1:
                hero_choose='knight'
            if event.key==pygame.K_2:
                hero_choose='archer'
        if event.type==pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                if list(pygame.mouse.get_pos())[0]>hero.x+70: hero.last_dir='right'
                else:hero.last_dir='left'
                if hero_choose=='archer':
                    if int(math.degrees(math.asin((hero.y-60 - list(pygame.mouse.get_pos())[1]) /((hero.x+70 - list(pygame.mouse.get_pos())[0]) ** 2 + (hero.y-60 - list(pygame.mouse.get_pos())[1]) ** 2) ** 0.5)))>30 and \
                       int(math.degrees(math.asin((hero.y - 60 - list(pygame.mouse.get_pos())[1]) / ((hero.x + 70 - list(pygame.mouse.get_pos())[0]) ** 2 + (hero.y - 60 - list(pygame.mouse.get_pos())[1]) ** 2) ** 0.5)))<150:
                        hero.battle2=True
                    else: hero.battle=True
                    if not hero.ladder:shoot=True
                else:
                    if not hero.ladder:hero.battle=True


def check():
    global hero,shoot
    if not hero.battle and not hero.battle2:
        arrows.append([Arrow(window, hero.x + 70, hero.y - 90, 0), list(pygame.mouse.get_pos())])
        shoot=False


def animation():
    global hero,dictionary,center,blocks,matrix,enviroment,hero_choose,arrows,bg_rect
    keys=pygame.key.get_pressed()
    if not hero.ladder:
        if hero.up:hero.key.append('jump')
        if hero.f:hero.key.append('fall')
        if hero.battle: hero.key.append('attack')
        if hero.battle2: hero.key.append('attack2')
    if keys[pygame.K_w]:
        if not hero.ladder:hero.key.append('idle')
        else:
            hero.key.append('climb')
            hero.climb(3, blocks, enviroment,matrix,ladder,house_rect,arrows,fire_rect)
    elif keys[pygame.K_s]:
        if not hero.ladder:hero.key.append('idle')
        else:
            hero.key.append('climb')
            hero.climb(-3, blocks, enviroment,matrix,ladder,house_rect,arrows,fire_rect)
    elif keys[pygame.K_d]:
        if not hero.ladder:hero.key.append('run')
        else:hero.key.append('climbidle')
        if not hero.battle and not hero.battle2: hero.move(matrix,5,blocks,enviroment,ladder,house_rect,arrows,fire_rect,bg_rect)
        hero.last_dir = 'right'
    elif keys[pygame.K_a]:
        if not hero.ladder:hero.key.append('run')
        else:hero.key.append('climbidle')
        if not hero.battle and not hero.battle2: hero.move(matrix, -5,blocks,enviroment,ladder,house_rect,arrows,fire_rect,bg_rect)
        hero.last_dir='left'
    else:
        if not hero.ladder and hero.on_ground:hero.key.append('idle')
        elif hero.ladder and not hero.on_ground:hero.key.append('climbidle')
        else:hero.key.append('jump')
    if hero.condition[0]!=hero.key[0]+hero.last_dir:
        hero.counter=0
        hero.condition.clear()
        hero.condition.append(hero.key[0]+hero.last_dir)
    hero.key.clear()
    for i in ladder:window.blit(ladder_image,i)
    for i in house_rect: i.animation(house, 8)
    for i in fire_rect: i.animation(fire, 6)
    if hero_choose=='knight': hero.animation(dictionary[hero.condition[0]],6)
    else: hero.animation(dictionary2[hero.condition[0]],6)


# map build
with open('maps/map_1.txt') as file:
    for f in file:
        for i in f.strip():row.append(str(i))
        matrix.append(row)
        row=[]
# map build

# check for tiles
for x in range(120):
    for y in range(40):
        for key in blocks.keys():
            if matrix[y][x]==key:blocks[key][1].append(blocks[key][0].get_rect(bottomleft=(x * 60, y * 60-60)))
        for key in enviroment.keys():
            if matrix[y][x]==key:enviroment[key][1].append(enviroment[key][0].get_rect(bottomleft=(x * 60, y * 60-60)))
        if matrix[y][x]=='l':ladder.append(ladder_image.get_rect(bottomleft=(x * 60, y * 60-60)))
        if matrix[y][x]=='h':house_rect.append(Object(window,'house/house_1.png',x*60,y * 60-60+5))
        if matrix[y][x]=='f':fire_rect.append(Object(window,'fire/fire_1.png',x*60,y * 60-60+5))
# check for tiles

clock=pygame.time.Clock()
if ctypes.windll.shell32.IsUserAnAdmin():
    while True:
        listener()
        window.fill((255,255,255))


        for i in bg_rect:
            for g in range(3):
                i[g].animation(bg_images[g],50)
            window.blit(bg_images[3],i[3])


        hero.correct_pos(ladder,blocks,enviroment,house_rect,arrows,fire_rect)


        if not hero.ladder:
            hero.fall(matrix,blocks,enviroment,ladder,house_rect,arrows,fire_rect)
            hero.jump(matrix,blocks,enviroment,ladder,house_rect,arrows,fire_rect)


        animation()


        for i in blocks.values():
            for g in i[1]:
                if i[1]!=[]:window.blit(i[0],g)


        if shoot and hero_choose=='archer':check()
        for i in arrows:i[0].shot(i[1])


        for i in blocks.values():
            for g in i[1]:
                for i in arrows:
                    if i[0].rect.colliderect(g):
                        i[0].end=True
                        if len(arrows)>5: arrows.pop(0)


        for i in enviroment.values():
            for g in i[1]:
                if i[1]!=[]: window.blit(i[0],g)


        pygame.mouse.set_visible(False)
        cursor_rect = cursor_image.get_rect(center=pygame.mouse.get_pos())
        window.blit(cursor_image, cursor_rect)
        fps.draw(clock.get_fps())
        pygame.display.update()
        clock.tick(70)
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
