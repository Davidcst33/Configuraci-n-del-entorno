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

# Fuente para el marcador
fuente = pygame.font.Font(None, 36)

# Clase para la pelota
class Pelota:
    def __init__(self):
        self.x = ANCHO // 2
        self.y = ALTO // 2
        self.radio = 10
        self.vel_x = random.choice([-5, 5])  # Velocidad aleatoria en x
        self.vel_y = random.choice([-5, 5])  # Velocidad aleatoria en y

    def mover(self):
        """
        Mueve la pelota en la dirección de las velocidades actuales.
        """
        self.x += self.vel_x
        self.y += self.vel_y

    def dibujar(self):
        """
        Dibuja la pelota en la pantalla en su posición actual.
        """
        pygame.draw.circle(pantalla, BLANCO, (self.x, self.y), self.radio)

    def rebote(self):
        """
        Cambia la dirección de la pelota si toca los bordes superior o inferior.
        """
        if self.y <= 0 or self.y >= ALTO:
            self.vel_y = -self.vel_y

# Clase para la paleta
class Paleta:
    def __init__(self, x):
        self.x = x
        self.y = ALTO // 2 - paleta_alto // 2
        self.velocidad = 6  # Velocidad de movimiento de la paleta

    def mover(self, keys):
        """
        Mueve la paleta en función de las teclas presionadas (arriba y abajo).
        Se utiliza la estructura repetitiva para verificar las teclas presionadas.
        """
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.velocidad  # Mueve hacia arriba
        if keys[pygame.K_DOWN] and self.y < ALTO - paleta_alto:
            self.y += self.velocidad  # Mueve hacia abajo

    def dibujar(self):
        """
        Dibuja la paleta en la pantalla en su posición actual.
        """
        pygame.draw.rect(pantalla, BLANCO, (self.x, self.y, paleta_ancho, paleta_alto))

# Función para dibujar el marcador
def dibujar_marcador(puntaje_izquierda, puntaje_derecha):
    """
    Dibuja el marcador de puntos en la pantalla.
    """
    texto_izquierda = fuente.render(str(puntaje_izquierda), True, BLANCO)
    texto_derecha = fuente.render(str(puntaje_derecha), True, BLANCO)
    pantalla.blit(texto_izquierda, (ANCHO // 4 - texto_izquierda.get_width() // 2, 20))
    pantalla.blit(texto_derecha, (ANCHO * 3 // 4 - texto_derecha.get_width() // 2, 20))

# Función principal del juego
def juego():
    reloj = pygame.time.Clock()
    pelota = Pelota()
    paleta_izquierda = Paleta(30)
    paleta_derecha = Paleta(ANCHO - 30 - paleta_ancho)

    puntaje_izquierda = 0
    puntaje_derecha = 0

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

        # Verificar si la pelota pasó la paleta izquierda o derecha
        if pelota.x <= paleta_izquierda.x + paleta_ancho and paleta_izquierda.y <= pelota.y <= paleta_izquierda.y + paleta_alto:
            pelota.vel_x = -pelota.vel_x  # Rebote en la paleta izquierda
        elif pelota.x >= paleta_derecha.x - pelota.radio and paleta_derecha.y <= pelota.y <= paleta_derecha.y + paleta_alto:
            pelota.vel_x = -pelota.vel_x  # Rebote en la paleta derecha
        elif pelota.x <= 0:
            puntaje_derecha += 1  # Punto para la paleta derecha
            pelota = Pelota()  # Reiniciar la pelota
        elif pelota.x >= ANCHO:
            puntaje_izquierda += 1  # Punto para la paleta izquierda
            pelota = Pelota()  # Reiniciar la pelota

        pantalla.fill(NEGRO)

        # Dibujar los objetos (pelota y paletas)
        paleta_izquierda.dibujar()
        paleta_derecha.dibujar()
        pelota.dibujar()

        # Dibujar el marcador
        dibujar_marcador(puntaje_izquierda, puntaje_derecha)

        # Actualizar la pantalla
        pygame.display.flip()

        # Repetir el ciclo para mantener 60 FPS
        reloj.tick(60)

# Iniciar el juego
if __name__ == "__main__":
    juego()
