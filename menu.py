from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.sound import *

window = Window(1000,600)
mouse = Window.get_mouse()
keyboard = Window.get_keyboard()

menu1 = GameImage("assets/menu1.png")
menu2 = GameImage("assets/menu2.png")

musica = Sound("sounds/Too Late To Save The Town.ogg")

def menuInstructions():
     while True:
          #Voltar para menu
          if keyboard.key_pressed("esc"):
               window.set_background_color([0,0,0])
               break
          #Jogar
          if Mouse.is_over_area(mouse,[346,442],[646,512]) and Mouse.is_button_pressed(mouse,1):
               break
          menu2.draw()
          window.update()

def menu():
     while True:
          musica.play()
          musica.set_repeat(True)
          window.set_title("Menu Cowboy Destroyers")
          
          #Sair
          if Mouse.is_over_area(mouse,[346,402],[646,472]) and Mouse.is_button_pressed(mouse,1):
               window.close()
          
          #Jogar
          if Mouse.is_over_area(mouse,[346,219],[646,289]) and Mouse.is_button_pressed(mouse,1):
               # window.update()
               break
               # return [True, True]
          
          #Instruções
          if Mouse.is_over_area(mouse,[346,310],[646,380]) and Mouse.is_button_pressed(mouse,1):
               # window.update()
               menuInstructions()
               break
               # return [True, False]
          
          menu1.draw()
          window.update()
     return True