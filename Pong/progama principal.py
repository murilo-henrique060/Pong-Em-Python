import pygame
pygame.init()

LARGURA_JANELA = 600
ALTURA_JANELA = 500
TAMANHO_BOLA = 30
VELOCIDADE_BOLAX = 6
VELOCIDADE_BOLAY = 3
BRANCO = (255,255,255)
PRETO = (0,0,0)

def moverBola(bola,dim_janela):
    base_esquerda = 0
    base_superior = 0
    base_direita = dim_janela[0]
    base_inferior = dim_janela[1]
    if bola['objRect'].left < base_esquerda or bola['objRect'].right > base_direita:
        bola['velX'] = -bola['velX']
    if bola['objRect'].top < base_superior or bola['objRect'].bottom > base_inferior:
        bola['velY'] = -bola['velY']
    bola['objRect'].x += bola['velX']
    bola['objRect'].y += bola['velY']
bola = {'objRect':pygame.Rect(LARGURA_JANELA/2,ALTURA_JANELA/2,TAMANHO_BOLA,TAMANHO_BOLA),'cor':BRANCO,'velX':VELOCIDADE_BOLAX,'velY':VELOCIDADE_BOLAY}

janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('PyPong')

relogio = pygame.time.Clock()

deve_continuar = True

while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
    moverBola(bola,(LARGURA_JANELA,ALTURA_JANELA))
    janela.fill(PRETO)
    pygame.draw.rect(janela,bola['cor'],bola['objRect'])
    pygame.display.update()
    relogio.tick(30)