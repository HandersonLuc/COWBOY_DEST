from menu import *
from jogo import *

play = False
instructions = False

while True:
    #Chama menu até ele retornar True (botão jogar)
    if play == False:
        play = menu()
    
    else:
        #Chama o jogo até ele retornar False (esc ou morrer)
        play = jogo()