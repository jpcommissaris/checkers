import pygame
pygame.init()

b_size = 400


class Board:
    def __init__(self):
        # graphics
        self.white = (255, 255, 255)
        self.blue = (0,190,250)
        self.red = (255,0,0)
        self.image = pygame.image.load('game_board.png')
        self.image = pygame.transform.scale(self.image, (b_size, b_size))
        # sets up empty lists of objects
        self.p = [[],[],[],[],[],[],[],[]] # pieces
        self.t = [[],[],[],[],[],[],[],[]] # testing
        self.s = [[],[],[],[],[],[],[],[]] # squares
        # logic
        self.pressed = False
        self.m1 = -1
        self.m2 = -1
        self.player = 0  # player 1 or 2


        for x in range(8):
            for y in range(8):
                self.p[x].insert(y,None)
                self.s[x].insert(y, Square(x, y))
                self.t[x].insert(y,0)  # a text rep for debugging

    def setBoard(self):

        for a in range(1, 8, 2):
            self.p[a][0] = Piece(a, 0, self.blue)
            self.t[a][0] = "b"
            self.p[a][2] = Piece(a, 2, self.blue)
            self.t[a][2] = "b"
            self.p[a][6] = Piece(a, 6, self.red)
            self.t[a][6] = "r"
        for b in range(0, 8, 2):
            self.p[b][1] = Piece(b, 1, self.blue)
            self.t[b][1] = "b"
            self.p[b][5] = Piece(b, 5, self.red)
            self.t[b][5] = "r"
            self.p[b][7] = Piece(b, 7, self.red)
            self.t[b][7] = "r"
        print("initiated board\n")

    def printBoard(self):
        for row in range(8):
            for col in range(8):
                print(self.t[col][row], end=" ")
            print("")

    def drawPieces(self,win):
        for row in range(8):
            for col in range(8):

                # puts pieces in right place
                if self.p[col][row] is None:
                    pass
                else:
                    self.p[col][row].setCol(col)
                    self.p[col][row].setRow(row)
                    self.p[col][row].draw(win, self.p[col][row].getColor())
                # checks for mouse
                self.checkMouse(win, self.p[col][row])
                self.player = self.state(col, row)
                print(self.player)

    def state(self, col, row):
        if self.p[col][row] is None:
            return 0
        elif (self.p[col][row].getColor() == self.red):
            return 1
        else:
            return 2



    def drawBoard(self, win):
        win.blit(self.image, (100, 100))


    def basicMoves(self, d, win):  # returns piece we have clicked
        col = d.col
        row = d.row
        new_r = 0
        new_c = 0

        if self.p[col][row].state() == 1:
            #left-up
            new_r = row + 1; new_c = col + 1;
            if new_r > -1 and new_c > -1:  # checks for edge
                if self.p[new_c][new_r].state(new_c, new_r) == 0:
                    self.s[new_c][new_r].draw(win)
                elif self.g[new_c][new_r].state(new_c, new_r) == 2:









        pass  # takes in a square, gives other squares that the piece can move to

    def checkMouse(self, win, d):
        if d is None:
            pass
        else:
            offset = b_size/16 - 4
            m = pygame.mouse.get_pos()
            r = d.getX() - offset < m[0] < d.getX() + offset
            c = d.getY() - offset < m[1] < d.getY() + offset
            if r and c:
                d.highlight(win, (255, 255, 0))
            if d.down:
                d.highlight(win, (0, 255, 0))
                self.basicMoves(d)

    def checkClick(self):
        for row in range(8):
            for col in range(8):
                if self.s[col][row].checkMouse():
                    if self.p[col][row] is None:
                        pass
                    else:
                        self.p[col][row].down = True
                else:
                    if self.p[col][row] is None:
                        pass
                    else:
                        self.p[col][row].down = False

    def drawMoves(self):
        pass #  draws squares in move locations
class Piece:

    def __init__(self, col, row, color):
        self.row = row
        self.col = col
        self.color = color
        self.r = b_size/16 - 6
        self.board_size = b_size/8
        self.offset = 116 + self.r / 2
        self.down = False
        self.king = False

    def setCol(self, c):
        self.col = c

    def setRow(self, r):
        self.row = r

    def getCol(self):
        return self.col

    def getRow(self):
        return self.row

    def getX(self):
        return self.offset+self.col * self.board_size

    def getY(self):
        return self.offset+self.row * self.board_size

    def getColor(self):
        return self.color

    def draw(self, win, color):
        offset = 116 + self.r/2
        x = offset+self.col * self.board_size
        y = offset+self.row * self.board_size
        pygame.draw.circle(win, color, (int(x), int(y)), int(self.r))

    def highlight(self,win,color):
        offset = 116 + self.r/2
        x = offset+self.col * self.board_size
        y = offset+self.row * self.board_size
        pygame.draw.circle(win, color, (int(x) - 1, int(y) - 1), int(self.r), 4)

class Square:
    def __init__(self, c, r):
        self.r = r
        self.c = c
        self.dis = 50

    def getX(self):
        return self.c * self.dis + 100

    def getY(self):
        return self.r * self.dis + 100

    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.getX(), self.getY(), self.dis, self.dis), 2)

    def checkMouse(self):
        m = pygame.mouse.get_pos()
        r = self.getX() < m[0] < self.getX() + self.dis
        c = self.getY() < m[1] < self.getY() + self.dis
        if r and c:
            return True


'''
b = Board()
b.setBoard()
b.printBoard()
'''




