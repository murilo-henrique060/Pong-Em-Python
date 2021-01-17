import pygame, time
pygame.init()

#Bola
TAMANHO_BOLA = 30
VELOCIDADEX = 8
VELOCIDADEY = 4

#JANELA
LARGURA_JANELA = 700
ALTURA_JANELA = 600

#Jogador
LARGURA_JOGADOR = 30
ALTURA_JOGADOR = 150
VELOCIDADE = 6

#Cores
BRANCO = (255,255,255)
PRETO = (0,0,0)

def pressionartecla(evento,tecla,teclas,nometecla):
    if evento.key == tecla:
        teclas[nometecla] = True

def soltartecla(evento,tecla,teclas,nometecla):
    if evento.key == tecla:
        teclas[nometecla] = False

class Jogador(pygame.sprite.Sprite):

    def __init__(self,posx):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([LARGURA_JOGADOR,ALTURA_JOGADOR])
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect[0] = posx
        self.rect[1] = ALTURA_JANELA/2 - ALTURA_JOGADOR/2
        self.vel = VELOCIDADE

    def mover(self,teclas,grupo):
        if grupo == 1:
            if teclas['cima'] and self.rect.top > 0:
                self.rect[1] -= VELOCIDADE
            if teclas['baixo'] and self.rect.bottom < ALTURA_JANELA:
                self.rect[1] += VELOCIDADE
        if grupo == 2:
            if teclas['cima2'] and self.rect.top > 0:
                self.rect[1] -= VELOCIDADE
            if teclas['baixo2'] and self.rect.bottom < ALTURA_JANELA:
                self.rect[1] += VELOCIDADE

class Bola(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([TAMANHO_BOLA,TAMANHO_BOLA])
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect[0] = LARGURA_JANELA/2
        self.rect[1] = ALTURA_JANELA/2
        self.velx = VELOCIDADEX
        self.vely = VELOCIDADEY

    def mover(self,Jogador1,Jogador2,cont):
        if self.rect.colliderect(Jogador1) and self.rect.left >= 50  or self.rect.colliderect(Jogador2) and self.rect.right <= 650:
            print('if1')
            self.velx = - self.velx
        elif self.rect.colliderect(Jogador1) and self.rect.left < 50 and cont == 0 or self.rect.colliderect(Jogador2) and self.rect.right > 650:
            print('else1')
            if self.rect[1] + 30 <= Jogador1.rect[1] + 70:
                print('if2')
                if self.vely < 0:
                    print('if3')
                    self.vely = 1.2 * self.vely
                elif self.vely > 0:
                    print('else3')
                    self.vely = - self.vely
            elif self.rect[1] >= Jogador1.rect[1] + 80:
                print('else2')
                if self.vely < 0:
                    print('if3')
                    self.vely = - self.vely
                elif self.vely > 0:
                    print('else3')
                    self.vely = 1.2 * self.vely
        if self.rect.left < 0 or self.rect.right > LARGURA_JANELA:
            self.vely = VELOCIDADEY
            self.velx = - self.velx
            self.rect[0] = LARGURA_JANELA/2
            self.rect[1] = ALTURA_JANELA/2
        if self.rect.top < 0 or self.rect.bottom > ALTURA_JANELA:
            self.vely = - self.vely
        self.rect[0] += self.velx
        self.rect[1] += self.vely
janela = pygame.display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
pygame.display.set_caption('PyPong')

bola_grupo = pygame.sprite.Group()
bola = Bola()
bola_grupo.add(bola)

jogador_grupo = pygame.sprite.Group()
jogador1 = Jogador(30)
jogador2 = Jogador(640)
jogador_grupo.add(jogador1,jogador2)

teclas = {'cima':False,'baixo':False,'cima2':False,'baixo2':False}

cont = 0

relogio = pygame.time.Clock()

deve_continuar = True

while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

        if evento.type == pygame.KEYDOWN:
            pressionartecla(evento,pygame.K_w,teclas,'cima')
            pressionartecla(evento,pygame.K_s,teclas,'baixo')
            pressionartecla(evento,pygame.K_UP,teclas,'cima2')
            pressionartecla(evento,pygame.K_DOWN,teclas,'baixo2')

        if evento.type == pygame.KEYUP:
            soltartecla(evento,pygame.K_w,teclas,'cima')
            soltartecla(evento,pygame.K_s,teclas,'baixo')
            soltartecla(evento,pygame.K_UP,teclas,'cima2')
            soltartecla(evento,pygame.K_DOWN,teclas,'baixo2')

    janela.fill(PRETO)

    jogador1.mover(teclas,1)
    jogador2.mover(teclas,2)
    jogador_grupo.update()
    jogador_grupo.draw(janela)

    bola_grupo.update()
    bola_grupo.draw(janela)
    bola.mover(jogador1,jogador2,cont)

    if bola.rect.colliderect(jogador1) and bola.rect.left < 50 or bola.rect.colliderect(jogador2) and bola.rect.left < 650:
        cont += 1
    else:
        cont = 0

    pygame.display.update()

    relogio.tick(30)