import pygame

def sol(tela,posX,posY,tamanhoSol):
    amarelo = (255, 204, 0)
    pygame.draw.circle(tela,amarelo, (posX,posY),tamanhoSol)
    


def gerenciarTamanhoSol(tamanhoSol, crescendo):
    if crescendo:
        tamanhoSol += 1
        if tamanhoSol >= 100:
            crescendo = False
    else:
        tamanhoSol -= 1
        if tamanhoSol <= 80:
            crescendo = True
    
    return tamanhoSol, crescendo
    