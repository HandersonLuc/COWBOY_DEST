from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.collision import *
import math

window = Window(1000,600)

mouse = Window.get_mouse()
keyboard = Window.get_keyboard()

#Cenário
cactus1 = Sprite("assets/cactus1.png")
cactus1.x = 600
cactus1.y = 100

cactus4 = Sprite("assets/cactus4.png")
cactus4.x = 500
cactus4.y = 450

rock1 = Sprite("assets/rock1.png")
rock1.x = 200
rock1.y = 400

bigRock = Sprite("assets/big-rock.png")
bigRock.x = 800
bigRock.y = 300

sand = Sprite("assets/sand.png")
sand.x = 250
sand.y = 100

smRock1 = GameImage("assets/sm-rock1.png")
smRock1.x = 800
smRock1.y = 100

smRock2 = GameImage("assets/sm-rock2.png")
smRock2.x = 400
smRock2.y = 150

smRock3 = GameImage("assets/sm-rock3.png")
smRock3.x = 200
smRock3.y = 430

smRock4 = GameImage("assets/sm-rock4.png")
smRock4.x = 700
smRock4.y = 510

#Personagens
cowboy = Sprite("assets/cowboy.png",1)

cowboy_right = Sprite("assets/cowboy_walk_right_spritesheet.png",4)
cowboy_right.set_total_duration(1000)
cowboy_left = Sprite("assets/cowboy_walk_left_spritesheet.png",4)
cowboy_left.set_total_duration(1000)
cowboy_up = Sprite("assets/cowboy_walk_up_spritesheet.png",4)
cowboy_up.set_total_duration(1000)
cowboy_down = Sprite("assets/cowboy_walk_down_spritesheet.png",4)
cowboy_down.set_total_duration(1000)

cowboy_attack_down = Sprite("assets/cowboy_attack_down_spritesheet.png",5)
cowboy_attack_down.set_total_duration(1000)
cowboy_reload_down = Sprite("assets/cowboy_reload_down_spritesheet.png",5)
cowboy_reload_down.set_total_duration(1000)

enemy_right = Sprite("assets/enemy_right.png",4)
enemy_right.set_total_duration(1000)
enemy_right.x = 100
enemy_right.y = 200

tiro = Sprite("assets/tiro.png",1)

#Info
hearts = GameImage("assets/hearts5.png")
hearts.x = 10
hearts.y = 10

bullets = GameImage("assets/bullets6.png")
bullets.x = window.width - bullets.width - 5
bullets.y = window.height - bullets.height - 5

def desenharCenario():
    cactus1.draw()
    cactus4.draw()
    rock1.draw()
    sand.draw()
    bigRock.draw()
    smRock1.draw()
    smRock2.draw()
    smRock3.draw()
    smRock4.draw()
    
def desenharInfo(vidas,municao):
    hearts.draw()
    bullets.draw()
    window.draw_text("SCORE: ", window.width - 200, 10, 30, [255,255,255],"Poppins",False,False)
    window.draw_text(str(0), window.width - 110, 10, 30, [255,255,255],"Poppins",False,False)
    
def calculaTempo(tempo,controle):
    tempo += window.delta_time()
    if(tempo>=1):
        controle = False
        tempo = 0
    return tempo, controle

def movimentoPlayer(atirou,municao,recarregou):
    if(atirou == True and municao<6):
            cowboy_attack_down.x = cowboy.x
            cowboy_attack_down.y = cowboy.y
            cowboy_attack_down.move_key_x(0.1)
            cowboy_attack_down.draw()
            cowboy_attack_down.update()
    
    elif(recarregou==True):
        cowboy_reload_down.x = cowboy.x
        cowboy_reload_down.y = cowboy.y
        cowboy_reload_down.move_key_x(0.1)
        cowboy_reload_down.draw()
        cowboy_reload_down.update()
    
    elif(keyboard.key_pressed("d")):
        cowboy_right.x = cowboy.x
        cowboy_right.y = cowboy.y
        cowboy_right.move_key_x(0.1)
        cowboy_right.draw()
        cowboy_right.update()
        if((cowboy.x+cowboy.width)<1000):
            cowboy.x += 100 * window.delta_time()
        
    elif(keyboard.key_pressed("a")):
        cowboy_left.x = cowboy.x
        cowboy_left.y = cowboy.y
        cowboy_left.move_key_x(0.1)
        cowboy_left.draw()
        cowboy_left.update()
        if(cowboy.x>0):
            cowboy.x -= 100 * window.delta_time()
        
    elif(keyboard.key_pressed("w")):
        cowboy_up.x = cowboy.x
        cowboy_up.y = cowboy.y
        cowboy_up.move_key_x(0.1)
        cowboy_up.draw()
        cowboy_up.update()
        if(cowboy.y>0):
            cowboy.y -= 100 * window.delta_time()
        
    elif(keyboard.key_pressed("s")):
        cowboy_down.x = cowboy.x
        cowboy_down.y = cowboy.y
        cowboy_down.move_key_x(0.1)
        cowboy_down.draw()
        cowboy_down.update()
        if((cowboy.y+cowboy.height)<600):
            cowboy.y += 100 * window.delta_time()
        
    else:
        cowboy.draw()
        
def atirar(tiros,atirou,municao):
    if(atirou==False):
        if(mouse.is_button_pressed(1)):
            atirou = True
            if(municao>0):
                municao -= 1
                clique_x = mouse.get_position()[0]
                clique_y = mouse.get_position()[1]
                m = math.atan2(clique_y-(cowboy.y+(cowboy.height/2)), clique_x-(cowboy.x+(cowboy.width/2)))
                tiros.append([cowboy.x+(cowboy.width/2),cowboy.y+(cowboy.height/2),m])
    
    for i in range(len(tiros)): 
        tiro.x = tiros[i][0]
        tiro.y = tiros[i][1]
        tiro.draw()
        tiros[i][0] += math.cos(tiros[i][2]) * 200 * window.delta_time()
        tiros[i][1] += math.sin(tiros[i][2]) * 200 * window.delta_time()
            
        if(tiro.x<0 or tiro.x>1000 or tiro.y<0 or tiro.y>600):
            tiros.remove(tiros[i])
            break
    
    return atirou, municao

def jogo():
    cowboy.x = window.width/2 - cowboy.width/2
    cowboy.y = window.height/2 - cowboy.height/2
    
    vidas = 5
    municao = 6
    recarregou = False
    tempoRecarga = 0
    
    tiros = []
    atirou = False
    tempoEspera = 0
    
    while True:
        
        window.set_title("Cowboy Destroyers")
        
        #Voltar para menu
        if keyboard.key_pressed("esc"):
            window.set_background_color([0,0,0])
            break
        
        window.set_background_color([232,198,91])
        
        desenharCenario()
        
        #Atirar
        atirou, municao = atirar(tiros,atirou,municao)
        if(atirou==True):
            tempoEspera, atirou = calculaTempo(tempoEspera,atirou)
        
        #Recarregar
        if(keyboard.key_pressed("r")):
            municao = 6
            recarregou = True    
        if(recarregou==True):
            tempoRecarga, recarregou = calculaTempo(tempoRecarga, recarregou)
        
        movimentoPlayer(atirou,municao,recarregou)
        
        #Animação inimigo
        enemy_right.move_key_x(0.1)
        enemy_right.draw()
        enemy_right.update()
        
        desenharInfo(vidas, municao)
        
        window.update()
    
    return False
