import time

import pygame
import random
import os

pygame.init()
pygame.mixer.init()
elfondo = pygame.image.load('ima/elfondo.png')
laser_sonido = pygame.mixer.Sound('Space Invaders_laser')
music = pygame.mixer.Sound('let.wav')
explosion_sonido = pygame.mixer.Sound('Space Invaders_laser')
golpe_sonido = pygame.mixer.Sound('Space Invaders_laser')
music.play()
valor = 0
explosion_list = []
for i in range(1, 5):
    explosion = pygame.image.load(f'explocion/{i}.png')
    explosion_list.append(explosion)

width = elfondo.get_width()
height = elfondo.get_height()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('fruit space')
run = True
fps = 60
clock = pygame.time.Clock()
score = 0
vida = 100
blanco = (255, 255, 255)
negro = (0, 0, 0)



def texto_puntos(frame, text, size, x, y):
    font = pygame.font.SysFont('Small Fonts', size, bold=True)
    text_frame = font.render(text, True, blanco, negro)
    text_rect = text_frame.get_rect()
    text_rect.midtop = (x, y)
    frame.blit(text_frame, text_rect)


def barra_vida(frame, x, y, nivel):
    longitud = 100
    alto = 20
    fill = int((nivel / 100) * longitud)
    border = pygame.Rect(x, y, longitud, alto)
    fill = pygame.Rect(x, y, fill, alto)
    pygame.draw.rect(frame, (255, 0, 55), fill)
    pygame.draw.rect(frame, negro, border, 4)


class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('ima/vacaok.png').convert_alpha()
        pygame.display.set_icon(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = width // 2
        self.rect.centery = height - 50
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.vida = 100



    def update(self):
        ''''''
        self.velocidad_x = 0
        self.velocidad_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.velocidad_x = -5
        if keystate[pygame.K_RIGHT]:
            self.velocidad_x = 5
        if keystate[pygame.K_DOWN]:
            self.velocidad_y = 1
        if keystate[pygame.K_UP]:
            self.velocidad_y =  -1


        self.rect.x += self.velocidad_x
        if self.rect.right > width:
            self.rect.right = width
        elif self.rect.left < 0:
            self.rect.left = 0

        self.rect.y += self.velocidad_y
        if self.rect.height > height:
            self.rect.height = height +1
        elif self.rect.height < 0 :
            self.ect.top = 0

    def disparos(self):
        bala = Balas(self.rect.centerx, self.rect.top)
        grupo_jugador.add(bala)
        grupo_balas_jugador.add(bala)
        laser_sonido.play()


class Burgers(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('ima/bburger.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10, width-50)
        for i in range(50):
            self.rect.y = random.randrange(i, (height/2)-100)

            self.velocidad_y = random.randrange(1, 20)







    def update(self):
        self.time = random.randrange(-1, pygame.time.get_ticks() // 5000)
        self.rect.x += self.time
        if self.rect.x >= width:
            self.rect.x = 0
            self.rect.y += 5

    def disparo_enemigo(self):
        bala = Balas_enemigas(self.rect.centerx, self.rect.centery)
        grupo_jugador.add(bala)

        grupo_balas_enemigas.add(bala)
        laser_sonido.play()


class Balas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        verdu= os.listdir('/home/ale_acosta/Escritorio/game env/verduras/')
        v_list = []
        verdu2 = random.choice(verdu)
        print(verdu2)

        self.image = pygame.image.load(verdu2).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocidad = -2

    def update(self):

        self.rect.y += self.velocidad
        if self.rect.bottom < 0:
            self.kill()


class Balas_enemigas(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('ima/b3.png').convert_alpha()
        #self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(1,width)
        self.rect.y = random.randrange(10)
        self.velocidad_y = 2

    def update(self):
        self.rect.y += self.velocidad_y
        if self.rect.bottom > height:
            self.kill()


class Explosion(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()
        self.image = explosion_list[0]
        img_scala = pygame.transform.scale(self.image, (20, 20))
        self.rect = img_scala.get_rect()
        self.rect.center = position
        self.time = pygame.time.get_ticks()
        self.velocidad_explo = 30
        self.frames = 0

    def update(self):
        tiempo = pygame.time.get_ticks()
        if tiempo - self.time > self.velocidad_explo:
            self.time = tiempo
            self.frames += 1
            if self.frames == len(explosion_list):
                self.kill()
            else:
                position = self.rect.center
                self.image = explosion_list[self.frames]
                self.rect = self.image.get_rect()
                self.rect.center = position

class Pollito (pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('ima/pollito1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = width // 2
        self.rect.y = height - 360

        self.velocidad_y = 0
        self.velocidad_x = 0








    def update(self):

        #self.time = random.randrange(-1, pygame.time.get_ticks() // 5000)

        if self.rect.right < width:
            self.rect.x +=2
            valor = self.rect.x

        #else:


        #self.rect.x -= 20

           # while self.rect.right < width:
            #    self.rect.x -=1
                #if self.rect.left < width:
                 #   self.rect.x +=2
             #   break




        '''
        self.rect.x += 2
        recc = self.rect.x
        if recc > width:
            self.rect.x -= 2
            self.rect.y += 5
            '''


grupo_jugador = pygame.sprite.Group()
grupo_enemigos = pygame.sprite.Group()
grupo_balas_jugador = pygame.sprite.Group()
grupo_balas_enemigas = pygame.sprite.Group()
grupo_pollito = pygame.sprite.Group()
player = Jugador()
grupo_jugador.add(player)
grupo_balas_jugador.add(player)

for x in range(9):
    enemigo = Burgers(10, 10)
    grupo_enemigos.add(enemigo)
    grupo_jugador.add(enemigo)

for x in range(2):
    pollo = Pollito(10, 10)
    grupo_pollito.add(pollo)
    grupo_jugador.add(pollo)

while run:
    clock.tick(fps)
    window.blit(elfondo, (0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.disparos()


    grupo_jugador.update()
    grupo_enemigos.update()
    grupo_balas_enemigas.update()
    grupo_balas_jugador.update()

    grupo_jugador.draw(window)


    colicion1 = pygame.sprite.groupcollide(grupo_enemigos, grupo_balas_jugador, True, True)
    for i in colicion1:
        score += 10
        enemigo= enemigo.disparo_enemigo()
        enemigo = Burgers(100, 10)
        grupo_enemigos.add(enemigo)
        grupo_jugador.add(enemigo)

        explo = Explosion(i.rect.center)
        grupo_jugador.add(explo)

    colicion2 = pygame.sprite.spritecollide(player, grupo_balas_enemigas, True)
    for j in colicion2:
        player.vida -= 10
        if player.vida <= 0:
            grupo_enemigos.add(bala)
            #run = False

            print('GAME OVER  ')
        explo1 = Explosion(j.rect.center)
        grupo_jugador.add(explo1)

    hits = pygame.sprite.spritecollide(player, grupo_enemigos, False)
    for hit in hits:
        player.vida -= 100
        enemigos = Burgers(10, 10)
        grupo_jugador.add(enemigos)
        grupo_enemigos.add(enemigos)
        if player.vida <= 0:


            run = False

    texto_puntos(window, ('   SCORE: ' + str(score) + '     '), 30, width - 85, 2)

    barra_vida(window, width - 285, 0, player.vida)

    pygame.display.flip()
pygame.quit()
