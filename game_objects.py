import pygame

b_size = 400
RED = (255, 0, 0)
BLUE = (0, 190, 250)

class Board:
    def __init__(self):
        # graphics
        self.image = pygame.image.load('game_board.png')
        self.image = pygame.transform.scale(self.image, (b_size, b_size))
        # sets up empty lists of objects
        self.s = [[],[],[],[],[],[],[],[]] # squares
        # logic
        self.pressed = False
        self.turn = 2  # player 1 or 2
        # creates 64 square objects all with no pieces
        for x in range(8):
            for y in range(8):
                self.s[x].insert(y, Square(x, y, None))


    def setBoard(self):

        for t in range(1, 8, 2):
            self.s[t][0] = Square(t, 0, Piece(t, 0, BLUE, False))
            self.s[t][2] = Square(t, 2, Piece(t, 2, BLUE, False))
            self.s[t][6] = Square(t, 6, Piece(t, 6, RED, False))
        for b in range(0, 8, 2):
            self.s[b][1] = Square(b, 1, Piece(b, 1, BLUE, False))
            self.s[b][5] = Square(b, 5, Piece(b, 5, RED, False))
            self.s[b][7] = Square(b, 7, Piece(b, 7, RED, False))

        print("initiated board\n")

    def drawPieces(self,win):
        for row in range(8):
            for col in range(8):

                # puts pieces in right place
                if self.s[col][row].state == 0:
                    pass
                else:
                    self.s[col][row].piece.col = col
                    self.s[col][row].piece.row = row
                    self.s[col][row].piece.draw(win, self.s[col][row].piece.color)
                # checks for mouse
                self.checkMouse(win, self.s[col][row])

    def drawBoard(self, win):
        win.blit(self.image, (100, 100))

    def checkMouse(self, win, d):
        if d.state == 0:
            pass
        else:
            p = d.piece
            offset = b_size/16 - 4
            m = pygame.mouse.get_pos()
            r = p.getX() - offset < m[0] < p.getX() + offset
            c = p.getY() - offset < m[1] < p.getY() + offset
            if r and c and d.state == self.turn:
                p.highlight(win, (255, 255, 0))
            if p.down:
                p.highlight(win, (0, 255, 0))

    def checkClick(self):
        for row in range(8):
            for col in range(8):
                if self.s[col][row].checkMouse():
                    if self.s[col][row].state == self.turn:
                        self.s[col][row].piece.down = True
                else:
                    if self.s[col][row].state != 0:
                        self.s[col][row].piece.down = False

class Square:
    def __init__(self, c, r, piece):
        self.r = r
        self.c = c
        self.dis = 50
        # handle a piece object on square
        if piece is None:
            state = 0
        elif piece.color == RED:
            state = 1
        else:
            state = 2
        self.state = state
        self.piece = piece  # None, or a piece

    # --- getters ---
    def getX(self):
        return self.c * self.dis + 100

    def getY(self):
        return self.r * self.dis + 100

    # --- graphics ---
    def draw(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.getX(), self.getY(), self.dis, self.dis), 2)

    # --- logic ---

    def checkMouse(self):
        m = pygame.mouse.get_pos()
        r = self.getX() < m[0] < self.getX() + self.dis
        c = self.getY() < m[1] < self.getY() + self.dis
        if r and c:
            return True


class Piece:

    def __init__(self, col, row, color, king):
        self.row = row
        self.col = col
        self.color = color
        self.r = b_size/16 - 6
        self.board_size = b_size/8
        self.offset = 116 + self.r / 2
        self.down = False
        self.king = king

    # --- getters ---
    def getX(self):
        return self.offset+self.col * self.board_size

    def getY(self):
        return self.offset+self.row * self.board_size

    # --- graphics ---
    def draw(self, win, color):
        offset = 116 + self.r/2
        x = offset+self.col * self.board_size
        y = offset+self.row * self.board_size
        pygame.draw.circle(win, color, (int(x), int(y)), int(self.r))
        if self.king:
            pass # blit image of crown

    def highlight(self,win,color):
        offset = 116 + self.r/2
        x = offset+self.col * self.board_size
        y = offset+self.row * self.board_size
        pygame.draw.circle(win, color, (int(x) - 1, int(y) - 1), int(self.r), 4)

    # --- logic ---




