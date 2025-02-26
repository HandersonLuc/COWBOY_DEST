from PPlay.window import *
from PPlay.sprite import *
from PPlay.animation import *
from PPlay.gameimage import *
from PPlay.collision import *
import math
import random
import datetime

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
borda = 15.5 # animacao

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

cowboy_death = Sprite("assets/cowboy_death_spritesheet.png",6)
cowboy_death.set_total_duration(2000)

enemy_right = Sprite("assets/enemy_right.png",4)
enemy_right.set_total_duration(1000)

enemy_left = Sprite("assets/enemy_left.png",4)
enemy_left.set_total_duration(1000)

enemy_jump_left = Sprite("assets/enemy_jump_left.png")
enemy_jump_right = Sprite("assets/enemy_jump_right.png")

tiro = Sprite("assets/tiro.png",1)

#Info
hearts = GameImage("assets/hearts5.png")
hearts.x = 10
hearts.y = 10

bullets = GameImage("assets/bullets6.png")
bullets.x = window.width - bullets.width - 5
bullets.y = window.height - bullets.height - 5

def Spawners ():
    lado = random.choice(['topo', 'baixo', 'esquerda', 'direita'])
    if lado == 'topo':
        return (random.randint(0, window.width), -40)  # Posição no topo
    elif lado == 'baixo':
        return (random.randint(0, window.width), window.height)  # Posição na base
    elif lado == 'esquerda':
        return (-40, random.randint(0, window.height))  # Posição na esquerda
    elif lado == 'direita':
        return (window.width, random.randint(0, window.height))  # Posição na direita

def spawn(inimigos):
    spawner_position = Spawners()
    inimigos.append([spawner_position[0], spawner_position[1]])

def colisaoInimigo(inimigos,i):
    if (((inimigos[i][0] + enemy_right.width - borda) >= cactus1.x) and ((inimigos[i][0] + borda) <= (cactus1.x + cactus1.width)) and ((inimigos[i][1] + enemy_right.height - borda) >= cactus1.y) and ((inimigos[i][1] + borda) <= (cactus1.y + cactus1.height))):
        return True
    elif (((inimigos[i][0] + enemy_right.width - borda) >= cactus4.x) and ((inimigos[i][0] + borda) <= (cactus4.x + cactus4.width)) and ((inimigos[i][1] + enemy_right.height - borda) >= cactus4.y) and ((inimigos[i][1] + borda) <= (cactus4.y + cactus4.height))):
        return True
    elif (((inimigos[i][0] + enemy_right.width - borda) >= rock1.x) and ((inimigos[i][0] + borda) <= (rock1.x + rock1.width)) and ((inimigos[i][1] + enemy_right.height - borda) >= rock1.y) and ((inimigos[i][1] + borda) <= (rock1.y + rock1.height))):
        return True
    elif (((inimigos[i][0] + enemy_right.width - borda) >= sand.x) and ((inimigos[i][0] + borda) <= (sand.x + sand.width)) and ((inimigos[i][1] + enemy_right.height - borda) >= sand.y) and ((inimigos[i][1] + borda) <= (sand.y + sand.height))):
        return True
    elif (((inimigos[i][0] + enemy_right.width - borda) >= bigRock.x) and ((inimigos[i][0] + borda) <= (bigRock.x + bigRock.width)) and ((inimigos[i][1] + enemy_right.height - borda) >= bigRock.y) and ((inimigos[i][1] + borda) <= (bigRock.y + bigRock.height))):
        return True
    return False

def inputNome(arquivo,pontos):
    arquivo.write(input("Digite o seu nome (sem espaço): "))
    arquivo.write(" ")
    arquivo.write(str(pontos))
    arquivo.write(" ")
    arquivo.write(str(datetime.date.today()))
    arquivo.write("\n")
    arquivo.close()
    return True

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
    
def desenharInfo(vidas,municao,score):
    if vidas > 0:
        if vidas == 5:
            hearts = GameImage("assets/hearts5.png")
        elif vidas == 4:
            hearts = GameImage("assets/hearts4.png")
        elif vidas == 3:
            hearts = GameImage("assets/hearts3.png")
        elif vidas == 2:
            hearts = GameImage("assets/hearts2.png")
        elif vidas == 1:
            hearts = GameImage("assets/hearts1.png")
        hearts.x = 10
        hearts.y = 10
        hearts.draw()
    
    if municao > 0:
        if municao == 6:
            bullets = GameImage("assets/bullets6.png")
        elif municao == 5:
            bullets = GameImage("assets/bullets5.png")
        elif municao == 4:
            bullets = GameImage("assets/bullets4.png")
        elif municao == 3:
            bullets = GameImage("assets/bullets3.png")
        elif municao == 2:
            bullets = GameImage("assets/bullets2.png")
        elif municao == 1:
            bullets = GameImage("assets/bullets1.png")
        bullets.x = window.width - bullets.width - 5
        bullets.y = window.height - bullets.height - 5
        bullets.draw()
    
    window.draw_text("SCORE: ", window.width - 200, 10, 30, [255,255,255],"Poppins",False,False)
    window.draw_text(str(score), window.width - 110, 10, 30, [255,255,255],"Poppins",False,False)
    
def calculaTempo(tempo,controle):
    tempo += window.delta_time()
    if(tempo>=1):
        controle = False
        tempo = 0
    return tempo, controle

def colisaoCowboy():
    if ((cowboy.x + cowboy.width - borda) >= cactus1.x) and ((cowboy.x + borda) <= (cactus1.x + cactus1.width)) and ((cowboy.y + cowboy.height) >= cactus1.y) and (cowboy.y <= (cactus1.y + cactus1.height)):
        return True
    elif ((cowboy.x + cowboy.width - borda) >= cactus4.x) and ((cowboy.x + borda) <= (cactus4.x + cactus4.width)) and ((cowboy.y + cowboy.height) >= cactus4.y) and (cowboy.y <= (cactus4.y + cactus4.height)):
        return True
    elif ((cowboy.x + cowboy.width - borda) >= rock1.x) and ((cowboy.x + borda) <= (rock1.x + rock1.width)) and ((cowboy.y + cowboy.height) >= rock1.y) and (cowboy.y <= (rock1.y + rock1.height)):
        return True
    elif ((cowboy.x + cowboy.width - borda) >= sand.x) and ((cowboy.x + borda) <= (sand.x + sand.width)) and ((cowboy.y + cowboy.height) >= sand.y) and (cowboy.y <= (sand.y + sand.height)):
        return True
    elif ((cowboy.x + cowboy.width - borda) >= bigRock.x) and ((cowboy.x + borda) <= (bigRock.x + bigRock.width)) and ((cowboy.y + cowboy.height) >= bigRock.y) and (cowboy.y <= (bigRock.y + bigRock.height)):
        return True
    return False

def movimentoCowboy(atirou,municao,recarregou,posicao,invencivel,morreu,vidas,tempoPiscar):
    piscar = False
    # Piscar
    if invencivel == True and vidas != 0:
        if (tempoPiscar < 0.125 or (tempoPiscar > 0.25 and tempoPiscar <= 0.375) or (tempoPiscar > 0.5 and tempoPiscar <= 0.625) or (tempoPiscar > 0.75 and tempoPiscar <= 0.875) or (tempoPiscar > 1)):
            piscar = True
    
    if(atirou == True and municao<6):
        cowboy_attack_down.x = cowboy.x
        cowboy_attack_down.y = cowboy.y
        cowboy_attack_down.move_key_x(0.1)
        if invencivel == False or piscar == True:
            cowboy_attack_down.draw()
        cowboy_attack_down.update()
    
    elif(recarregou==True):
        cowboy_reload_down.x = cowboy.x
        cowboy_reload_down.y = cowboy.y
        cowboy_reload_down.move_key_x(0.1)
        if invencivel == False or piscar == True:
            cowboy_reload_down.draw()
        cowboy_reload_down.update()
    
    elif(keyboard.key_pressed("d")):
        cowboy_right.x = cowboy.x
        cowboy_right.y = cowboy.y
        cowboy_right.move_key_x(0.1)
        if invencivel == False or piscar == True:
            cowboy_right.draw()
        cowboy_right.update()
        if not colisaoCowboy():
            posicao[0] = cowboy.x
            posicao[1] = cowboy.y
            if((cowboy.x+cowboy.width-borda)<1000):
                cowboy.x += 100 * window.delta_time()
        else:
            cowboy.x = posicao[0]
            cowboy.y = posicao[1]
        
    elif(keyboard.key_pressed("a")):
        cowboy_left.x = cowboy.x
        cowboy_left.y = cowboy.y
        cowboy_left.move_key_x(0.1)
        if invencivel == False or piscar == True:
            cowboy_left.draw()
        cowboy_left.update()
        if not colisaoCowboy():
            posicao[0] = cowboy.x
            posicao[1] = cowboy.y
            if((cowboy.x+borda)>0):
                cowboy.x -= 100 * window.delta_time()
        else:
            cowboy.x = posicao[0]
            cowboy.y = posicao[1]
        
    elif(keyboard.key_pressed("w")):
        cowboy_up.x = cowboy.x
        cowboy_up.y = cowboy.y
        cowboy_up.move_key_x(0.1)
        if invencivel == False or piscar == True:
            cowboy_up.draw()
        cowboy_up.update()
        if not colisaoCowboy():
            posicao[0] = cowboy.x
            posicao[1] = cowboy.y
            if(cowboy.y>0):
                cowboy.y -= 100 * window.delta_time()
        else:
            cowboy.x = posicao[0]
            cowboy.y = posicao[1]
        
    elif(keyboard.key_pressed("s")):
        cowboy_down.x = cowboy.x
        cowboy_down.y = cowboy.y
        cowboy_down.move_key_x(0.1)
        if invencivel == False or piscar == True:
            cowboy_down.draw()
        cowboy_down.update()
        if not colisaoCowboy():
            posicao[0] = cowboy.x
            posicao[1] = cowboy.y
            if((cowboy.y+cowboy.height)<600):
                cowboy.y += 100 * window.delta_time()
        else:
            cowboy.x = posicao[0]
            cowboy.y = posicao[1]
        
    elif (invencivel == False or piscar == True) and morreu == False:
        cowboy.draw()

def atirar(tiros,atirou,municao,tirosRemover,inimigos,score):
    if(atirou==False):
        # Atirou
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
        
        # Desenha e incrementa
        tiro.draw()
        tiros[i][0] += math.cos(tiros[i][2]) * 200 * window.delta_time()
        tiros[i][1] += math.sin(tiros[i][2]) * 200 * window.delta_time()
            
        # Colisão cenário
        if Collision.collided_perfect(tiro,cactus1) or Collision.collided_perfect(tiro,cactus4) or Collision.collided_perfect(tiro,rock1) or Collision.collided_perfect(tiro,sand) or Collision.collided_perfect(tiro,bigRock):
            tirosRemover.append(i)
        # Saiu da tela
        elif(tiro.x<0 or tiro.x>1000 or tiro.y<0 or tiro.y>600):
            tirosRemover.append(i)
        # Colisão inimigo
        else:
            for j in range(len(inimigos)-1, -1, -1):
                # print(f"inimigo {inimigos[j]} colide com bala {tiro.x}, {tiro.y}")
                if ((tiro.x + tiro.width) >= (inimigos[j][0] + borda)) and (tiro.x <= (inimigos[j][0] + enemy_right.width - borda)) and ((tiro.y + tiro.height) >= (inimigos[j][1] + borda)) and (tiro.y <= (inimigos[j][1] + enemy_right.height - borda)):
                    tirosRemover.append(i)
                    inimigos.remove(inimigos[j])
                    score += 1
                    break
                    
    # Atualizar lista
    for i in range(len(tirosRemover)-1,-1,-1):
        if tirosRemover[i] < len(tiros):
            tiros.remove(tiros[tirosRemover[i]])
    
    return atirou, municao, score

def jogo():
    
    arquivo = open('ranking.txt','a')
    
    cowboy.x = window.width/2 - cowboy.width/2
    cowboy.y = window.height/2 - cowboy.height/2
    posicao = [cowboy.x,cowboy.y]
    
    invencivel = False
    tempoPiscar = 0
    morreu = False
    cronometro = 0
    
    vidas = 5
    score = 0
    
    municao = 6
    recarregou = False
    tempoRecarga = 0
    
    tiros = []
    atirou = True
    tempoEspera = 0
    
    tirosRemover = []
    
    inimigos = [] # [[x,y]]
    colidiuInimigo = False
    tempoColisao = 0
    
    # fazer os inimigos aparecerem um de cada vez em cada onda
    wave = 0
    inimigos_na_wave = 1
    tempo_spawn = 0
    frequencia = 10

    inimigosRemover = []
    
    window.delay(300)
    
    while True:
        
        window.set_title("Cowboy Destroyers")
        
        #Voltar para menu
        if keyboard.key_pressed("esc"):
            window.set_background_color([0,0,0])
            break
        
        window.set_background_color([232,198,91])
        
        desenharCenario()
        
        #Animação inimigo
        for i in range(len(inimigos)):
            # Colisão cowboy e inimigo
            if(colidiuInimigo == False) and (invencivel == False):
                if ((cowboy.x + cowboy.width - borda) >= (inimigos[i][0] + borda)) and ((cowboy.x + borda) <= (inimigos[i][0] + enemy_right.width - borda)) and ((cowboy.y + cowboy.height) >= (inimigos[i][1] + borda)) and (cowboy.y <= (inimigos[i][1] + enemy_right.height - borda)):
                    vidas -= 1
                    colidiuInimigo = True
                    invencivel = True
                    tempoPiscar = 0
                    # Remover inimigo
                    inimigosRemover.append(i)
            if(colidiuInimigo == True):
                tempoColisao, colidiuInimigo = calculaTempo(tempoColisao, colidiuInimigo)
                
            colidiu = False
            for j in range(0,i):
                if inimigos[i][0] + enemy_right.width >= inimigos[j][0] and inimigos[i][0] <= inimigos[j][0] + enemy_right.width:
                    colidiu = True
                    break
            
            # Movimentação inimigo eixo X
            if (inimigos[i][0] + enemy_right.width - borda) < (cowboy.x + borda + cowboy.width/2):
                if colisaoInimigo(inimigos,i):
                    enemy_jump_right.x = inimigos[i][0]
                    enemy_jump_right.y = inimigos[i][1]
                    enemy_jump_right.draw()
                else:
                    enemy_right.x = inimigos[i][0]
                    enemy_right.y = inimigos[i][1]
                    enemy_right.move_key_x(0.1)
                    enemy_right.draw()
                    enemy_right.update()
                if not colidiu:
                    inimigos[i][0] += 20 * window.delta_time()
            else:
                if colisaoInimigo(inimigos,i):
                    enemy_jump_left.x = inimigos[i][0]
                    enemy_jump_left.y = inimigos[i][1]
                    enemy_jump_left.draw()
                else:
                    enemy_left.x = inimigos[i][0]
                    enemy_left.y = inimigos[i][1]
                    enemy_left.move_key_x(0.1)
                    enemy_left.draw()
                    enemy_left.update()
                if inimigos[i][0] > cowboy.x:
                    if not colidiu:
                        inimigos[i][0] -= 20 * window.delta_time()
            
            # eixo Y
            if inimigos[i][1] < cowboy.y:
                inimigos[i][1] += 20 * window.delta_time()
            else:
                inimigos[i][1] -= 20 * window.delta_time()
        
        # Atualizar lista
        for i in range(len(inimigosRemover),0,-1):
            inimigos.remove(inimigos[inimigosRemover[i-1]])
        inimigosRemover = []
        
        # Reset inimigos
        if tempo_spawn >= frequencia:
            if len(inimigos) < 50:
                wave += 1
                inimigos_na_wave += 1
                for _ in range(inimigos_na_wave):
                    spawn(inimigos)
                tempo_spawn = 0
                frequencia -= 0.01 * score

        tempo_spawn += window.delta_time()
        """if tempo_spawn >= intervalo and len(inimigos) < inimigos_na_wave:
            spawn(inimigos, score)
            tempo_spawn = 0"""
        
        #Atirar
        atirou, municao, score = atirar(tiros,atirou,municao,tirosRemover,inimigos,score)
        tirosRemover = []
        if(atirou==True):
            tempoEspera, atirou = calculaTempo(tempoEspera,atirou)
        
        #Recarregar
        if(keyboard.key_pressed("r")):
            municao = 6
            recarregou = True    
        if(recarregou==True):
            tempoRecarga, recarregou = calculaTempo(tempoRecarga, recarregou)
        
        movimentoCowboy(atirou,municao,recarregou,posicao,invencivel,morreu,vidas,tempoPiscar)
        
        tempoPiscar += window.delta_time()
        if tempoPiscar >= 2:
            invencivel = False
        
        # Perdeu
        if vidas == 0:
            morreu = True
            cowboy_death.x = cowboy.x
            cowboy_death.y = cowboy.y
            cowboy_death.move_key_x(0.1)
            cowboy_death.draw()
            cowboy_death.update()
            cronometro += window.delta_time()
            if cronometro > 1:
                if inputNome(arquivo,score):
                    break

        desenharInfo(vidas,municao,score)
        
        window.update()
    
    return False