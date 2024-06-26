import pygame
import random
import os
from tkinter import simpledialog
from funcoesUsadas.funcoes2 import sol,gerenciarTamanhoSol

pygame.init()

relogio = pygame.time.Clock()
icone  = pygame.image.load("Recursos/icone4.png")
iron = pygame.image.load("Recursos/euclides2.png")

fundo = pygame.image.load("Recursos/fundo2.png")
fundoStart = pygame.image.load("Recursos/fundoStart4.png")
fundoDead = pygame.image.load("Recursos/fundoDead3.png")

missel = pygame.image.load("Recursos/inimigo1.png")
missel2 = pygame.image.load("Recursos/inimigo2.png")

aguia = pygame.image.load("Recursos/aguia4.png")

tamanho = (800,600)
tela = pygame.display.set_mode( tamanho ) 
pygame.display.set_caption("Matemática e Euclides")
pygame.display.set_icon(icone)
missileSound = pygame.mixer.Sound("Recursos/gritoPassaro.mp3")
explosaoSound = pygame.mixer.Sound("Recursos/vento.wav")
fonte = pygame.font.SysFont("comicsans",28)
fonteStart = pygame.font.SysFont("comicsans",55)
fonteMorte = pygame.font.SysFont("arial",120)
pygame.mixer.music.load("Recursos/matSound.mp3")



branco = (255,255,255)
preto = (0, 0 ,0 )



  


def movimentarAguia(posicaoXAguia, direita):
    if direita:
        if posicaoXAguia < 800:  
            posicaoXAguia += 5
        else:
            direita = False
    else:
        if posicaoXAguia > 0:
            posicaoXAguia -= 10
        else:
            direita = True
    
    return posicaoXAguia, direita




def jogar(nome):
    pygame.mixer.Sound.play(missileSound)
    pygame.mixer.music.play(-1)
    posicaoXPersona = 0
    posicaoYPersona = 750
    movimentoXPersona  = 0
    movimentoYPersona  = 0
    posicaoXMissel = 400
    posicaoYMissel = -240
    velocidadeMissel = 1

    posicaoXMissel2 = 200
    posicaoYMissel2 = -110
    velocidadeMissel2 = 1



    posicaoXAguia = 400
    posicaoYAguia = 300
    direita = True
    pontos = 0
    larguraPersona = 210
    alturaPersona = 127
    larguaMissel  = 90
    alturaMissel  = 90

    larguaMissel2  = 50
    alturaMissel2  = 90
    larguraAguia = 127
    alturaAguia = 50
    dificuldade  = 50

    tamanhoSol = 30
    crescendo = True

    while True:
        
        if jogar == True:
          movimentarAguia(aguia)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 10
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_LEFT:
                movimentoXPersona = -10
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_RIGHT:
                movimentoXPersona = 0
            elif evento.type == pygame.KEYUP and evento.key == pygame.K_LEFT:
                movimentoXPersona = 0
            
                
        posicaoXPersona = posicaoXPersona + movimentoXPersona            
        posicaoYPersona = posicaoYPersona + movimentoYPersona            
        
        if posicaoXPersona < 0 :
            posicaoXPersona = 10
        elif posicaoXPersona >630:
            posicaoXPersona = 620
            
        if posicaoYPersona < 0 :
            posicaoYPersona = 10
        elif posicaoYPersona > 473:
            posicaoYPersona = 472
        posicaoXAguia, direita = movimentarAguia(posicaoXAguia, direita)
        tamanhoSol, crescendo = gerenciarTamanhoSol(tamanhoSol, crescendo)
        
        
            
        tela.fill(branco)
        tela.blit(fundo, (0,0) )
        #pygame.draw.circle(tela, preto, (posicaoXPersona,posicaoYPersona), 40, 0 )
        tela.blit( iron, (posicaoXPersona, posicaoYPersona) )
        tela.blit(aguia, (posicaoXAguia, posicaoYAguia))
        
        sol(tela,700,50,int(tamanhoSol))
        

        
        
        posicaoYMissel = posicaoYMissel + velocidadeMissel
        if posicaoYMissel > 600:
            posicaoYMissel = -240
            pontos = pontos + 1
            velocidadeMissel = velocidadeMissel + 1
            posicaoXMissel = random.randint(0,800)
            pygame.mixer.Sound.play(missileSound)
            
        posicaoYMissel2 = posicaoYMissel2 + velocidadeMissel2
        if posicaoYMissel2 > 700:
            posicaoYMissel2 = -240
            pontos = pontos + 1
            velocidadeMissel2 = velocidadeMissel2 + 1
            posicaoXMissel2 = random.randint(0,800)
            pygame.mixer.Sound.play(missileSound)
            
        tela.blit( missel, (posicaoXMissel, posicaoYMissel) )
        tela.blit( missel2, (posicaoXMissel2, posicaoYMissel2) )
        
        texto = fonte.render(nome+"- Pontos: "+str(pontos), True, branco)
        tela.blit(texto, (10,10))
        
        pixelsPersonaX = list(range(posicaoXPersona, posicaoXPersona+larguraPersona))
        pixelsPersonaY = list(range(posicaoYPersona, posicaoYPersona+alturaPersona))
        pixelsMisselX = list(range(posicaoXMissel, posicaoXMissel + larguaMissel))
        pixelsMisselY = list(range(posicaoYMissel, posicaoYMissel + alturaMissel))

        pixelsMisselX2 = list(range(posicaoXMissel2, posicaoXMissel2 + larguaMissel2))
        pixelsMisselY2 = list(range(posicaoYMissel2, posicaoYMissel2 + alturaMissel2))
        
        #print( len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )   )
        if  len( list( set(pixelsMisselY).intersection(set(pixelsPersonaY))) ) > dificuldade:
            if len( list( set(pixelsMisselX).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                dead(nome, pontos)
        
        if  len( list( set(pixelsMisselY2).intersection(set(pixelsPersonaY))) ) > dificuldade:
                if len( list( set(pixelsMisselX2).intersection(set(pixelsPersonaX))   ) )  > dificuldade:
                    dead(nome, pontos)
        pygame.display.update()
        relogio.tick(60)


def dead(nome, pontos):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(explosaoSound)
    
    jogadas  = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8")
        jogadas = eval(arquivo.read())
        arquivo.close()
    except:
        arquivo = open("historico.txt","w",encoding="utf-8")
        arquivo.close()
 
    jogadas[nome] = pontos   
    arquivo = open("historico.txt","w",encoding="utf-8") 
    arquivo.write(str(jogadas))
    arquivo.close()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_RETURN:
                jogar(nome)

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
        tela.fill(branco)
        tela.blit(fundoDead, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("RESTART", True, branco)
        tela.blit(textoStart, (400,482))
        textoEnter = fonte.render("Press enter to continue...", True, branco)
        tela.blit(textoEnter, (60,482))
        pygame.display.update()
        relogio.tick(60)


def ranking():
    estrelas = {}
    try:
        arquivo = open("historico.txt","r",encoding="utf-8" )
        estrelas = eval(arquivo.read())
        arquivo.close()
    except:
        pass
    
    nomes = sorted(estrelas, key=estrelas.get,reverse=True)
    print(estrelas)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    start()

        tela.fill(preto)
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        textoStart = fonteStart.render("BACK TO START", True, branco)
        tela.blit(textoStart, (330,482))
        
        
        posicaoY = 50
        for key,nome in enumerate(nomes):
            if key == 13:
                break
            textoJogador = fonte.render(nome + " - "+str(estrelas[nome]), True, branco)
            tela.blit(textoJogador, (300,posicaoY))
            posicaoY = posicaoY + 30

            
        
        pygame.display.update()
        relogio.tick(60)


def start():
    nome = simpledialog.askstring("Matemática e Euclides","Nome Completo:")
    
    
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if buttonStart.collidepoint(evento.pos):
                    jogar(nome)
                elif buttonRanking.collidepoint(evento.pos):
                    ranking()

        tela.fill(branco)
        tela.blit(fundoStart, (0,0))
        buttonStart = pygame.draw.rect(tela, preto, (35,482,750,100),0)
        buttonRanking = pygame.draw.rect(tela, preto, (10,30,120,40),0,30)
        textoRanking = fonte.render("Ranking", True, branco)
        tela.blit(textoRanking, (20,30))
        textoStart = fonteStart.render("START", True, branco)
        tela.blit(textoStart, (330,482))

        
        
        pygame.display.update()
        relogio.tick(60)

start()