from pygame import mixer,init,image,sprite,Surface,display,time,event,QUIT,KEYDOWN,KEYUP,K_w,K_s,K_UP,K_DOWN
from random import randint
init()

#diretorio musica
MUSICA = 'Pong\\PongSoundBlip.wav'
MUSICA2 = 'Pong\\PongSoundBlip2.wav'
MUSICA3 = 'Pong\\PongSoundGameOver.wav'

#musica
COLISAO = mixer.Sound(MUSICA)
COLISAO2 = mixer.Sound(MUSICA2)
GAMEOVER = mixer.Sound(MUSICA3)

#JANELA
LARGURA_JANELA = 800
ALTURA_JANELA = 600


#Números
NUM_0 = image.load('Pong\\numero 0.png')
NUM_1 = image.load('Pong\\numero 1.png')
NUM_2 = image.load('Pong\\numero 2.png')
NUM_3 = image.load('Pong\\numero 3.png')
NUM_4 = image.load('Pong\\numero 4.png')
NUM_5 = image.load('Pong\\numero 5.png')
NUM_6 = image.load('Pong\\numero 6.png')
NUM_7 = image.load('Pong\\numero 7.png')
NUM_8 = image.load('Pong\\numero 8.png')
NUM_9 = image.load('Pong\\numero 9.png')

#Fundo
FUNDO = image.load('Pong\\Pong.png')

#Bola
TAMANHO_BOLA = 10
VELOCIDADEx = randint(13,15)
multiplicadorx = randint(0,1)
if multiplicadorx == 0:
    VELOCIDADEx *= -1
VELOCIDADEy = randint(4,7)
multiplicador = randint(0,1)
if multiplicador == 0:
    VELOCIDADEy *= -1
POSy = randint(0,ALTURA_JANELA - TAMANHO_BOLA)

#Jogador
LARGURA_JOGADOR = 15
ALTURA_JOGADOR = 50
DISTANCIA_DA_BORDA = 50
VELOCIDADE = 15

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

class Jogador(sprite.Sprite):

    def __init__(self,posx):
        sprite.Sprite.__init__(self)

        self.image = Surface([LARGURA_JOGADOR,ALTURA_JOGADOR])
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

class Bola(sprite.Sprite):

    def __init__(self):
        sprite.Sprite.__init__(self)

        self.image = Surface([TAMANHO_BOLA,TAMANHO_BOLA])
        self.image.fill(BRANCO)
        self.rect = self.image.get_rect()
        self.rect[0] = LARGURA_JANELA/2
        self.rect[1] = POSy
        self.velx = VELOCIDADEx
        self.vely = VELOCIDADEy
        self.cont = 0
        self.cont2 = 0

    def mover(self,Jogador1,Jogador2,VELOCIDADEX):
        if VELOCIDADEX < 0:
            VELOCIDADEX *= -1
        if self.rect.colliderect(Jogador1) or self.rect.colliderect(Jogador2):
            if self.cont2 == 0:
                mixer.Sound.play(COLISAO)
            self.cont2 += 1
        else:
            self.cont2 = 0
        if self.rect.colliderect(Jogador1) and self.rect.left >= Jogador1.rect.right - VELOCIDADEX and self.cont == 0 or self.rect.colliderect(Jogador2) and self.rect.right <= Jogador2.rect.left + VELOCIDADEX and self.cont == 0:
            self.velx = - self.velx
        elif self.rect.colliderect(Jogador1) and self.rect.left < Jogador1.rect.right - VELOCIDADEX or self.rect.colliderect(Jogador2) and self.rect.right > Jogador2.rect.left + VELOCIDADEX:
            if self.rect.colliderect(Jogador1) and self.rect[1] + TAMANHO_BOLA <= Jogador1.rect[1] + ALTURA_JOGADOR / 2  or self.rect.colliderect(Jogador2) and self.rect[1] + TAMANHO_BOLA <= Jogador2.rect[1] + ALTURA_JOGADOR:
                if self.vely < 0:
                    self.vely *= 1.3
                elif self.vely > 0:
                    self.vely *= -1
            elif self.rect.colliderect(Jogador1) and self.rect[1] >= Jogador1.rect[1] + ALTURA_JOGADOR / 2 + 1 or self.rect.colliderect(Jogador2) and self.rect[1] >= Jogador2.rect[1] + TAMANHO_BOLA:
                if self.vely < 0:
                    self.vely *= -1
                elif self.vely > 0:
                    self.vely *= 1.3
        if self.rect.colliderect(Jogador1) or self.rect.colliderect(Jogador2):
            self.cont += 1
        else:
            self.cont = 0
        if self.rect.left < 0 or self.rect.right > LARGURA_JANELA:
            mixer.Sound.play(GAMEOVER)
            POSy = randint(0,ALTURA_JANELA - TAMANHO_BOLA)
            VELOCIDADEx = randint(13,15)
            multiplicadorx = randint(0,1)
            if multiplicadorx == 0:
                VELOCIDADEx *= -1
            VELOCIDADEy = randint(5,7)
            multiplicador = (0,1)
            if multiplicador == 0:
                VELOCIDADEy *= -1
            self.vely = VELOCIDADEy
            self.velx = VELOCIDADEx
            self.rect[0] = LARGURA_JANELA/2
            self.rect[1] = POSy
        if self.rect.top < 0 or self.rect.bottom > ALTURA_JANELA:
            mixer.Sound.play(COLISAO2)
            self.vely = - self.vely
        self.rect[0] += self.velx
        self.rect[1] += self.vely
janela = display.set_mode((LARGURA_JANELA,ALTURA_JANELA))
display.set_caption('PyPong')

bola_grupo = sprite.Group()
bola = Bola()
bola_grupo.add(bola)

jogador_grupo = sprite.Group()
jogador1 = Jogador(DISTANCIA_DA_BORDA)
jogador2 = Jogador(LARGURA_JANELA - (DISTANCIA_DA_BORDA + LARGURA_JOGADOR))
jogador_grupo.add(jogador1,jogador2)

teclas = {'cima':False,'baixo':False,'cima2':False,'baixo2':False}

jogador1_pontos = 0
jogador2_pontos = 0

relogio = time.Clock()

cont = 0

deve_continuar = True

while deve_continuar:
    for evento in event.get():
        if evento.type == QUIT:
            deve_continuar = False

        if evento.type == KEYDOWN:
            deve_iniciar = False
            pressionartecla(evento,K_w,teclas,'cima')
            pressionartecla(evento,K_s,teclas,'baixo')
            pressionartecla(evento,K_UP,teclas,'cima2')
            pressionartecla(evento,K_DOWN,teclas,'baixo2')

        if evento.type == KEYUP:
            soltartecla(evento,K_w,teclas,'cima')
            soltartecla(evento,K_s,teclas,'baixo')
            soltartecla(evento,K_UP,teclas,'cima2')
            soltartecla(evento,K_DOWN,teclas,'baixo2')

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
    desenhar_ponto(janela, jogador2_pontos,(550,50))

    jogador1.mover(teclas,1)
    jogador2.mover(teclas,2)
    jogador_grupo.update()
    jogador_grupo.draw(janela)

    bola_grupo.update()
    bola_grupo.draw(janela)
    bola.mover(jogador1,jogador2,VELOCIDADEx)

    display.update()

    relogio.tick(30)