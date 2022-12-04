import pygame
from grid import Grid

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '850,100'

surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-tac-toe')

# Se crea un hilo por aparte donde se hará la rececpión de datos posteriormente
import threading
def create_thread(target):
    thread = threading.Thread(target=target)
    thread.daemon = True
    thread.start()

# Se crea tcp para la conexión entre ambos jugadores en este caso es para lo de el cliente.
import socket
HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

def receive_data():
    global turn
    while True:
        # Se reciben los datos del cliente
        data = sock.recv(1024).decode() 
         #En esta parte se hace el envio de datos de los elementos, como es gato el envió es x o y, de igual manera cuando es nuestro turno o el de el contrincante 
        data = data.split('-')
        x, y = int(data[0]), int(data[1])
        if data[2] == 'yourturn':
            turn = True
        if data[3] == 'False':
            grid.game_over = True
        if grid.get_cell_value(x, y) == 0:
            grid.set_cell_value(x, y, 'X')

# Esta es la ejecucion del hilo anteriormente mencionado, de esta manera no se afecta el orden del juego.
create_thread(receive_data)

grid = Grid()
running = True
player = "O"
turn = False
playing = 'True'

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                if turn and not grid.game_over:
                    pos = pygame.mouse.get_pos()
                    cellX, cellY = pos[0] // 200, pos[1] // 200
                    grid.get_mouse(cellX, cellY, player)
                    if grid.game_over:
                        playing = 'False'
                    send_data = '{}-{}-{}-{}'.format(cellX, cellY, 'yourturn', playing).encode()
                    sock.send(send_data)
                    turn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                grid.game_over = False
                playing = 'True'
            elif event.key == pygame.K_ESCAPE:
                running = False

    surface.fill((0,0,0))

    grid.draw(surface)

    pygame.display.flip()