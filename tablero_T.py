import pygame as p
import time
import threading
import time
color= p.Color(0,140,60)
p.init()


class Tablero(p.sprite.Sprite):
    def __init__(self, x_id, y_id, number):
        super().__init__()
        self.width = 120
        self.height = 120
        self.x = x_id * self.width
        self.y = y_id * self.height
        self.content = ''
        self.number = number
        self.image = blank_image
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect() 

    def update(self):
        self.rect.center = (self.x, self.y)

    def clicked(self, x_val, y_val):
        global turn, won

        if self.content == '':
            if self.rect.collidepoint(x_val, y_val):
                self.content = turn
                board[self.number] = turn

                if turn == 'x':
                    self.image = x_image
                    self.image = p.transform.scale(self.image, (self.width, self.height))
                    turn = 'o'
                    checkWinner('x')

                    if not won:
                        CompMove()

                else:
                    self.image = o_image
                    self.image = p.transform.scale(self.image, (self.width, self.height))
                    turn = 'x'
                    checkWinner('o')


def checkWinner(player):
    global background, won, startX, startY, endX, endY

    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == player:
            won = True
            getPos(winners[i][0], winners[i][2])
            break

    if won:
        Update()
        drawLine(startX, startY, endX, endY)

        Tablero_group.empty()
        background = p.image.load(player.upper() + ' Wins.png')
        background = p.transform.scale(background, (WIDTH, HEIGHT))


def Winner(player):
    global compMove, move

    for i in range(8):
        if board[winners[i][0]] == player and board[winners[i][1]] == player and board[winners[i][2]] == '':
            compMove = winners[i][2]
            move = False

        elif board[winners[i][0]] == player and board[winners[i][1]] == '' and board[winners[i][2]] == player:
            compMove = winners[i][1]
            move = False

        elif board[winners[i][0]] == '' and board[winners[i][1]] == player and board[winners[i][2]] == player:
            compMove = winners[i][0]
            move = False


def CompMove():
    global move, background

    move = True

    if move:
        Winner('o')

    if move:
        Winner('x')

    if move:
        checkDangerPos()

    if move:
        checkCentre()

    if move:
        checkCorner()

    if move:
        checkEdge()

    if not move:
        for Tablero in Tableros:
            if Tablero.number == compMove:
                Tablero.clicked(Tablero.x, Tablero.y)

    else:
        Update()
        time.sleep(1)
        Tablero_group.empty()
        background = p.image.load('Tie Game.png')
        background = p.transform.scale(background, (WIDTH, HEIGHT))


def checkDangerPos():
    global move, compMove

    if board == dangerPos1:
        compMove = 2
        move = False

    elif board == dangerPos2:
        compMove = 4
        move = False

    elif board == dangerPos3:
        compMove = 1
        move = False

    elif board == dangerPos4:
        compMove = 4
        move = False

    elif board == dangerPos5:
        compMove = 7
        move = False

    elif board == dangerPos6:
        compMove = 9
        move = False

    elif board == dangerPos7:
        compMove = 9
        move = False

    elif board == dangerPos8:
        compMove = 7
        move = False

    elif board == dangerPos9:
        compMove = 9
        move = False


def checkCentre():
    global compMove, move

    if board[5] == '':
        compMove = 5
        move = False


def checkCorner():
    global compMove, move

    for i in range(1, 11, 2):
        if i != 5:
            if board[i] == '':
                compMove = i
                move = False
                break


def checkEdge():
    global compMove, move

    for i in range(2, 10, 2):
        if board[i] == '':
            compMove = i
            move = False
            break


def getPos(n1, n2):
    global startX, startY, endX, endY

    for sqs in Tableros:
        if sqs.number == n1:
            startX = sqs.x
            startY = sqs.y

        elif sqs.number == n2:
            endX = sqs.x
            endY = sqs.y


def drawLine(x1, y1, x2, y2):
    p.draw.line(win, (0, 0, 0), (x1, y1), (x2, y2), 15)
    p.display.update()
    time.sleep(2)


def Update():
    win.blit(background, (0, 0))
    Tablero_group.draw(win)
    Tablero_group.update()
    p.display.update()


WIDTH = 500
HEIGHT = 500

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_caption('Si ganas te doy 100 pesos')
clock = p.time.Clock()

blank_image = p.image.load('Blank.png')
x_image = p.image.load('x.png')
o_image = p.image.load('o.png')
background = p.image.load('Background.png')

background = p.transform.scale(background, (WIDTH, HEIGHT))

move = True
won = False
compMove = 5

Tablero_group = p.sprite.Group()
Tableros = []

winners = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
board = ['' for i in range(10)]

dangerPos1 = ['', 'x', '', '', '', 'o', '', '', '', 'x']
dangerPos2 = ['', '', '', 'x', '', 'o', '', 'x', '', '']
dangerPos3 = ['', '', '', 'x', 'x', 'o', '', '', '', '']
dangerPos4 = ['', 'x', '', '', '', 'o', 'x', '', '', '']
dangerPos5 = ['', '', '', '', 'x', 'o', '', '', '', 'x']
dangerPos6 = ['', '', '', '', '', 'o', 'x', 'x', '', '']
dangerPos7 = ['', '', '', '', '', 'o', 'x', '', 'x', '']
dangerPos8 = ['', 'x', '', '', '', 'o', '', '', 'x', '']
dangerPos9 = ['', '', '', 'x', '', 'o', '', '', 'x', '']

startX = 0
startY = 0
endX = 0
endY = 0

num = 1
for y in range(1, 4):
    for x in range(1, 4):
        sq = Tablero(x, y, num)
        Tablero_group.add(sq)
        Tableros.append(sq)

        num += 1

turn = 'x'
run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

        if event.type == p.MOUSEBUTTONDOWN and turn == 'x':
            mx, my = p.mouse.get_pos()
            for s in Tableros:
                s.clicked(mx, my)

    Update()