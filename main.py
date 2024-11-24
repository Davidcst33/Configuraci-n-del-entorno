import pygame
import random

# Inicialización de Pygame
pygame.init()

# Definir colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Tamaño de la pantalla
ANCHO = 600
ALTO = 400
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Atari Pong")

# Configuración de la paleta
paleta_ancho = 15
paleta_alto = 90

# Clase para la pelota
class Pelota:
    def __init__(self):
        self.x = ANCHO // 2
        self.y = ALTO // 2
        self.radio = 10
        self.vel_x = random.choice([-5, 5])
        self.vel_y = random.choice([-5, 5])

    def mover(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def dibujar(self):
        pygame.draw.circle(pantalla, BLANCO, (self.x, self.y), self.radio)

    def rebote(self):
        if self.y <= 0 or self.y >= ALTO:
            self.vel_y = -self.vel_y

# Clase para la paleta
class Paleta:
    def __init__(self, x):
        self.x = x
        self.y = ALTO // 2 - paleta_alto // 2
        self.velocidad = 6

    def mover(self, keys):
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidad
        if keys[pygame.K_DOWN] and self.y < ALTO - paleta_alto:
            self.y += self.velocidad

    def dibujar(self):
        pygame.draw.rect(pantalla, BLANCO, (self.x, self.y, paleta_ancho, paleta_alto))

# Función principal del juego
def juego():
    reloj = pygame.time.Clock()
    pelota = Pelota()
    paleta_izquierda = Paleta(30)
    paleta_derecha = Paleta(ANCHO - 30 - paleta_ancho)

    # Bucle principal del juego
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        paleta_izquierda.mover(keys)
        paleta_derecha.mover(keys)

        pelota.mover()
        pelota.rebote()

        pantalla.fill(NEGRO)

        # Dibujar los objetos
        paleta_izquierda.dibujar()
        paleta_derecha.dibujar()
        pelota.dibujar()

        pygame.display.flip()
        reloj.tick(60)  # 60 cuadros por segundo

# Iniciar el juego
if __name__ == "__main__":
    juego()
