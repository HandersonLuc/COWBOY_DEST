from PPlay.window import *
from PPlay.gameimage import *

largura = 1000
altura = 600
janela = Window(largura, altura)

bg = GameImage("assets/bg.png")

def ranking():
    teclado = Window.get_keyboard()
    
    arquivo = open('ranking.txt','r')
    pontuacao = []
    linhas = 0
    nomes = []
    datas = []
    
    for linha in arquivo:
        if linha[0] != ' ':
            linha = linha.split()
            if linha != []:
                linhas += 1
                pontuacao.append(int(linha[1]))
    pontuacao.sort(reverse=True)
    
    if linhas > 5:
        linhas = 5
    
    for i in range(linhas):
        arquivo.close()
        arquivo = open('ranking.txt', 'r')
        for linha in arquivo:
            if linha[0] != ' ':
                linha = linha.split()
                if linha != []:
                    if int(linha[1]) == pontuacao[i]:
                        nomes.append(linha[0])
                        data = linha[2]
                        data = data.split("-")
                        datas.append(data)
    
    arquivo.close()
    
    while True:
        bg.draw()
        if teclado.key_pressed("esc"):
            break
        
        # janela.draw_text("RANKING",435,150,40,[255,255,255],"Poppins",True,False)
        
        # Números
        janela.draw_text("1.",250,180,30,[254,229,106],"Arial",True,False)
        janela.draw_text("2.",250,230,30,[254,229,106],"Arial",True,False)
        janela.draw_text("3.",250,280,30,[254,229,106],"Arial",True,False)
        janela.draw_text("4.",250,330,30,[254,229,106],"Arial",True,False)
        janela.draw_text("5.",250,380,30,[254,229,106],"Arial",True,False)
        
        # Nomes e pontuação
        if linhas > 0:
            janela.draw_text(nomes[0],300,190,30,[255,255,255],"Poppins",False,False)
            janela.draw_text(str(pontuacao[0]),700,180,30,[255,255,255],"Arial",True,False)
            janela.draw_text(datas[0][2]+"/"+datas[0][1]+"/"+datas[0][0],480,180,30,[255,255,255],"Arial",False,False)
        if linhas > 1:
            janela.draw_text(nomes[1],300,240,30,[255,255,255],"Poppins",False,False)
            janela.draw_text(str(pontuacao[1]),700,230,30,[255,255,255],"Arial",True,False)
            janela.draw_text(datas[1][2]+"/"+datas[1][1]+"/"+datas[1][0],480,230,30,[255,255,255],"Arial",False,False)
        if linhas > 2:
            janela.draw_text(nomes[2],300,290,30,[255,255,255],"Poppins",False,False)
            janela.draw_text(str(pontuacao[2]),700,280,30,[255,255,255],"Arial",True,False)
            janela.draw_text(datas[2][2]+"/"+datas[2][1]+"/"+datas[2][0],480,280,30,[255,255,255],"Arial",False,False)
        if linhas > 3:
            janela.draw_text(nomes[3],300,340,30,[255,255,255],"Poppins",False,False)
            janela.draw_text(str(pontuacao[3]),700,330,30,[255,255,255],"Arial",True,False)
            janela.draw_text(datas[3][2]+"/"+datas[3][1]+"/"+datas[3][0],480,330,30,[255,255,255],"Arial",False,False)
        if linhas > 4:
            janela.draw_text(nomes[4],300,390,30,[255,255,255],"Poppins",False,False)
            janela.draw_text(str(pontuacao[4]),700,380,30,[255,255,255],"Arial",True,False)
            janela.draw_text(datas[4][2]+"/"+datas[4][1]+"/"+datas[4][0],480,380,30,[255,255,255],"Arial",False,False)
        
        janela.update()
