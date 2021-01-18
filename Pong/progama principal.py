import pygame
pygame.init()

#diretorio musica
MUSICA = 'Pong\\PongSoundBlip.wav'
MUSICA2 = 'Pong\\PongSoundBlip2.wav'
MUSICA3 = 'Pong\\PongSoundGameOver.wav'

#musica
COLISAO = pygame.mixer.Sound(MUSICA)
COLISAO2 = pygame.mixer.Sound(MUSICA2)
GAMEOVER = pygame.mixer.Sound(MUSICA3)

#Números
NUM_0 = pygame.image.load('Pong\\numero 0.png')
NUM_1 = pygame.image.load('Pong\\numero 1.png')
NUM_2 = pygame.image.load('Pong\\numero 2.png')
NUM_3 = pygame.image.load('Pong\\numero 3.png')
NUM_4 = pygame.image.load('Pong\\numero 4.png')
NUM_5 = pygame.image.load('Pong\\numero 5.png')
NUM_6 = pygame.image.load('Pong\\numero 6.png')
NUM_7 = pygame.image.load('Pong\\numero 7.png')
NUM_8 = pygame.image.load('Pong\\numero 8.png')
NUM_9 = pygame.image.load('Pong\\numero 9.png')

#Fundo
FUNDO = pygame.image.load('Pong\\Pong.png')

#Bola
TAMANHO_BOLA = 30
VELOCIDADEX = 10
VELOCIDADEY = 5

#JANELA
LARGURA_JANELA = 800
ALTURA_JANELA = 600

#Jogador
LARGURA_JOGADOR = 30
ALTURA_JOGADOR = 150
VELOCIDADE = 8

#Cores
BRANCO = (255,255,255)
PRETO = (0,0,0)

def desenhar_ponto(superficie,pontuação,posição):
    if pontuação == 0:
        superficie.blit(NUM_0,posição)
    if pontuação == 1:
        superficie.blit(NUM_1,posição)
    if pontuação == 2:
        superficie.blit(NUM_2,posição)
    if pontuação == 3:
        superficie.blit(NUM_3,posição)
    if pontuação == 4:
        superficie.blit(NUM_4,posição)
    if pontuação == 5:
        superficie.blit(NUM_5,posição)
    if pontuação == 6:
        superficie.blit(NUM_6,posição)
    if pontuação == 7:
        superficie.blit(NUM_7,posição)
    if pontuação == 8:
        superficie.blit(NUM_8,posição)
    if pontuação == 9:
        superficie.blit(NUM_9,posição)

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
        self.cont = 0
        self.cont2 = 0

    def mover(self,Jogador1,Jogador2):
        if self.rect.colliderect(Jogador1) or self.rect.colliderect(Jogador2):
            if self.cont2 == 0:
                pygame.mixer.Sound.play(COLISAO)
            self.cont2 += 1
        else:
            self.cont2 = 0
        if self.rect.colliderect(Jogador1) and self.rect.left >= 50 and self.cont == 0 or self.rect.colliderect(Jogador2) and self.rect.right <= 750 and self.cont == 0:
            self.velx = - self.velx
        elif self.rect.colliderect(Jogador1) and self.rect.left < 50 or self.rect.colliderect(Jogador2) and self.rect.right > 750:
            if self.rect.colliderect(Jogador1) and self.rect[1] + 30 <= Jogador1.rect[1] + 70 or self.rect.colliderect(Jogador2) and self.rect[1] + 30 <= Jogador2.rect[1] + 70:
                if self.vely < 0:
                    self.vely *= 1.3
                elif self.vely > 0:
                    self.vely *= -1
            elif self.rect.colliderect(Jogador1) and self.rect[1] >= Jogador1.rect[1] + 80 or self.rect.colliderect(Jogador2) and self.rect[1] >= Jogador2.rect[1] + 80:
                if self.vely < 0:
                    self.vely *= -1
                elif self.vely > 0:
                    self.vely *= 1.3
        if self.rect.colliderect(Jogador1) or self.rect.colliderect(Jogador2):
            self.cont += 1
        else:
            self.cont = 0
        if self.rect.left < 0 or self.rect.right > LARGURA_JANELA:
            pygame.mixer.Sound.play(GAMEOVER)
            self.vely = VELOCIDADEY
            self.velx = - self.velx
            self.rect[0] = LARGURA_JANELA/2
            self.rect[1] = ALTURA_JANELA/2
        if self.rect.top < 0 or self.rect.bottom > ALTURA_JANELA:
            pygame.mixer.Sound.play(COLISAO2)
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
jogador2 = Jogador(740)
jogador_grupo.add(jogador1,jogador2)

teclas = {'cima':False,'baixo':False,'cima2':False,'baixo2':False}

jogador1_pontos = 0
jogador2_pontos = 0

relogio = pygame.time.Clock()

cont = 0

deve_continuar = True
deve_iniciar = True

while deve_continuar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            deve_continuar = False

        if evento.type == pygame.KEYDOWN:
            deve_iniciar = False
            pressionartecla(evento,pygame.K_w,teclas,'cima')
            pressionartecla(evento,pygame.K_s,teclas,'baixo')
            pressionartecla(evento,pygame.K_UP,teclas,'cima2')
            pressionartecla(evento,pygame.K_DOWN,teclas,'baixo2')

        if evento.type == pygame.KEYUP:
            soltartecla(evento,pygame.K_w,teclas,'cima')
            soltartecla(evento,pygame.K_s,teclas,'baixo')
            soltartecla(evento,pygame.K_UP,teclas,'cima2')
            soltartecla(evento,pygame.K_DOWN,teclas,'baixo2')

    if deve_iniciar:
        bola.velx = 0
        bola.vely = 0
    elif cont == 0:
        bola.velx = VELOCIDADEX
        bola.vely = VELOCIDADEY
        cont += 1

    if bola.rect.left < 0:
        jogador2_pontos += 1
    elif bola.rect.right > LARGURA_JANELA:
        jogador1_pontos +=1

    if jogador1_pontos == 10 or jogador2_pontos == 10:
        deve_iniciar = True
        cont = 0
        jogador1_pontos = 0
        jogador2_pontos = 0

    janela.blit(FUNDO, (0,0))

    desenhar_ponto(janela,jogador1_pontos,(150,50))
    desenhar_ponto(janela, jogador2_pontos,(525,50))

    jogador1.mover(teclas,1)
    jogador2.mover(teclas,2)
    jogador_grupo.update()
    jogador_grupo.draw(janela)

    bola_grupo.update()
    bola_grupo.draw(janela)
    bola.mover(jogador1,jogador2)

    pygame.display.update()

    relogio.tick(40)