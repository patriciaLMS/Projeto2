import pygame
tamanho = (800,600)
tela = pygame.display.set_mode( tamanho )
aguia = pygame.image.load("Recursos/aguia3.png") 
relogio = pygame.time.Clock()
def movimentarAguia (aguia):
    pygame.init()
    
    while True:
        
        pygame.display.update()  
        if direita == True:
            if aguia < 800:
                aguia = aguia + 10
            else:
                direita = False
        else:
            if aguia > 0:
                aguia = aguia - 10
            else:
                direita = True
        relogio.tick(60) #60 fps