import pygame
pygame.init()
LARGURA_JANELA = 600
ALTURA_JANELA = 500
TAMANHO_BOLA = 30
LARGURA_JOGADOR = 20
ALTURA_JOGADOR = 150
VELOCIDADE_JOGADOR = 7
VELOCIDADE_BOLAX = 7
VELOCIDADE_BOLAY = 4
BRANCO = (255,255,255)
PRETO = (0,0,0)
def moverJogador1(jogador,tecla,altura_janela):
    base_superior = 0
    base_inferior = altura_janela
    if tecla['cima1'] and jogador['objRect'].top > base_superior:
        jogador['objRect'].y -= jogador['vel']
    if tecla['baixo1'] and jogador['objRect'].bottom < base_inferior:
        jogador ['objRect'].y += jogador['vel']
def moverJogador2(jogador2,teclas,altura_janela):
    base_superior = 0
    base_inferior = altura_janela
    if teclas['cima2'] and jogador2['objRect'].top > base_superior:
        jogador2['objRect'].y -= jogador2['vel']
    if teclas['baixo2'] and jogador2['objRect'].bottom < base_inferior:
        jogador2['objRect'].y += jogador2['vel']
def moverBola(bola,dim_janela):
    base_esquerda = 0
    base_superior = 0
    base_direita = dim_janela[0]
    base_inferior = dim_janela[1]
    if bola['objRect'].left < base_esquerda or bola['objRect'].right > base_direita:
        bola['objRect'][0] = LARGURA_JANELA/2
        bola['objRect'][1] = ALTURA_JANELA/2
    if bola['objRect'].top < base_superior or bola['objRect'].bottom > base_inferior:
        bola['velY'] = -bola['velY']
    bola['objRect'].x -= bola['velX']
    bola['objRect'].y -= bola['velY']
bola = {'objRect':pygame.Rect(LARGURA_JANELA/2,ALTURA_JANELA/2,TAMANHO_BOLA,TAMANHO_BOLA),'cor':BRANCO,'velX':VELOCIDADE_BOLAX,'velY':VELOCIDADE_BOLAY}
teclas = {'cima1':False,'cima2':False,'baixo1':False,'baixo2':False}
jogador1 = {'objRect':pygame.Rect(20,150,LARGURA_JOGADOR,ALTURA_JOGADOR),'cor':BRANCO,'vel':VELOCIDADE_JOGADOR}
jogador2 = {'objRect':pygame.Rect(560,150,LARGURA_JOGADOR,ALTURA_JOGADOR),'cor':BRANCO,'vel':VELOCIDADE_JOGADOR}
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('PyPong')
relogio = pygame.time.Clock()
deve_continuar = True
while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                teclas['cima2'] = True
            if evento.key == pygame.K_DOWN:
                teclas['baixo2'] = True
            if evento.key == pygame.K_w:
                teclas['cima1'] = True
            if evento.key == pygame.K_s:
                teclas['baixo1'] = True
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_UP:
                teclas['cima2'] = False
            if evento.key == pygame.K_DOWN:
                teclas['baixo2'] = False
            if evento.key == pygame.K_w:
                teclas['cima1'] = False
            if evento.key == pygame.K_s:
                teclas['baixo1'] = False
    bateu = jogador1['objRect'].colliderect(bola['objRect'])
    bateu2 = jogador2['objRect'].colliderect(bola['objRect'])
    if bateu or bateu2:
        bola['velX'] = -bola['velX']
        bola['velY'] = bola['velY']
    moverJogador2(jogador2,teclas,ALTURA_JANELA)
    moverJogador1(jogador1,teclas,ALTURA_JANELA)
    moverBola(bola,(LARGURA_JANELA,ALTURA_JANELA))
    janela.fill(PRETO)
    pygame.draw.rect(janela,jogador2['cor'],jogador2['objRect'])
    pygame.draw.rect(janela,jogador1['cor'],jogador1['objRect'])
    pygame.draw.rect(janela,bola['cor'],bola['objRect'])
    pygame.display.update()
    relogio.tick(30)