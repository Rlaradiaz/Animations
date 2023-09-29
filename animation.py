import pygame
import os

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Animación con movimiento")

# Cargar las imágenes en una lista
image_paths = []
frame_directory = "C:/Users/RODRIGO/Desktop/animacion/frames"
for i in range(8, 116):
    frame_filename = f'frame_{i:04d}.jpg'
    frame_path = os.path.join(frame_directory, frame_filename)
    image_paths.append(frame_path)

# Inicializar variables para la animación
current_frame = 0
frame_delay = 5  # Controla la velocidad de la animación
movement_speed = 5  # Velocidad de movimiento
x_position = 0  # Posición en el eje X
direction = 0  # Dirección (0 para detenido, 1 para derecha, -1 para izquierda)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Detectar las teclas presionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        # Mover el personaje hacia la derecha
        direction = 1
    elif keys[pygame.K_LEFT]:
        # Mover el personaje hacia la izquierda
        direction = -1
    else:
        # Detener el movimiento si no se presionan las teclas
        direction = 0

    # Actualizar el frame actual
    current_frame += direction

    # Asegurarse de que el frame actual esté dentro de los límites
    if current_frame < 0:
        current_frame = len(image_paths) - 1
    elif current_frame >= len(image_paths):
        current_frame = 0

    # Cargar la imagen actual y mostrarla en la pantalla
    current_image_path = image_paths[current_frame]
    frame_surface = pygame.image.load(current_image_path)
    screen.fill((0, 0, 0))  # Limpiar la pantalla
    screen.blit(frame_surface, (x_position, 0))
    pygame.display.flip()

    # Control de velocidad de la animación
    pygame.time.delay(frame_delay)

# Salir del juego
pygame.quit()
