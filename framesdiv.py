import cv2
import os

# Ruta al archivo .mp4
video_path = "C:\\Users\\RODRIGO\\Desktop\\Animations\\Cat.mp4"


# Directorio donde se guardarán los fotogramas
output_directory = 'frames'

# Crea el directorio si no existe
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Abre el archivo de video
cap = cv2.VideoCapture(video_path)

# Inicializa un contador de fotogramas
frame_count = 0

while True:
    # Lee un fotograma del video
    ret, frame = cap.read()

    # Si no se puede leer más fotogramas, sal del bucle
    if not ret:
        break

    # Guarda el fotograma en el directorio de salida
    frame_filename = os.path.join(output_directory, f'frame_{frame_count:04d}.jpg')
    cv2.imwrite(frame_filename, frame)

    frame_count += 1

# Cierra el archivo de video y libera recursos
cap.release()

print(f'Se han guardado {frame_count} fotogramas en {output_directory}')
