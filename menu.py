from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.sprite import *
from PPlay.sound import *
from ranking import *

window = Window(1000,600)
mouse = Window.get_mouse()
keyboard = Window.get_keyboard()

menu1 = GameImage("assets/menu1.png")
jogar = GameImage("assets/jogar.png")
intrucoes = GameImage("assets/intrucoes.png")
botaoRanking = GameImage("assets/ranking.png")
sair = GameImage("assets/sair.png")

menu2 = GameImage("assets/menu2.png")
jogar2 = GameImage("assets/jogar2.png")

musica = Sound("sounds/Too Late To Save The Town.ogg")

def menuInstructions():
     while True:
          menu2.draw()
          
          #Voltar para menu
          if keyboard.key_pressed("esc"):
               window.set_background_color([0,0,0])
               break
          
          #Jogar
          if Mouse.is_over_area(mouse,[346,442],[646,512]):
               jogar2.draw()
               if Mouse.is_button_pressed(mouse,1):
                    break
          
          window.update()
     
     return

def menu():
     while True:
          musica.play()
          musica.set_repeat(True)
          window.set_title("Menu Cowboy Destroyers")
          menu1.draw()
          
          #Sair
          if Mouse.is_over_area(mouse,[346,493],[646,664]):
               sair.draw()
               if Mouse.is_button_pressed(mouse,1):
                    window.close()
          
          #Jogar
          if Mouse.is_over_area(mouse,[346,219],[646,289]):
               jogar.draw()
               if Mouse.is_button_pressed(mouse,1):
                    break
          
          #Instruções
          if Mouse.is_over_area(mouse,[346,310],[646,380]):
               intrucoes.draw()
               if Mouse.is_button_pressed(mouse,1):
                    menuInstructions()
                    break
          
          # Ranking 
          if Mouse.is_over_area(mouse,[346,402],[646,472]):
               botaoRanking.draw()
               if Mouse.is_button_pressed(mouse,1):
                    ranking()
          
          window.update()
     
     return True
