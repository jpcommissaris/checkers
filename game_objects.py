import pygame
pygame.font.init()
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
        self.turn = 1  # player 1 or 2
        self.p1 = 12 
        self.p2 = 12
        self.jumped = False
        # creates 64 square objects all with no pieces
        for x in range(8):
            for y in range(8):
                self.s[x].insert(y, Square(x, y, None))

    def won(self):
        if self.p1 == 0 or self.p2 == 0:
            return True
        return False

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
                if self.s[col][row].state == 0 :
                    pass
                else:
                    self.s[col][row].piece.col = col
                    self.s[col][row].piece.row = row
                    self.s[col][row].piece.draw(win, self.s[col][row].piece.color)
                    self.moves(win, self.s[col][row], col, row)


                # checks for mouse
                self.checkMouse(win, self.s[col][row])

    def drawBoard(self, win):
        pygame.draw.rect(win, (230, 250, 230), (265, 530, 50, 25))
        win.blit(self.image, (100, 100))
        myfont = pygame.font.SysFont('Arial', 20)
        score1 = myfont.render(str(self.p1), False, (0, 0, 0))
        win.blit(score1,(120, 76))
        score2 = myfont.render(str(self.p2), False, (0, 0, 0))
        win.blit(score2,(450, 76))
        passButton = myfont.render("pass", False, (0, 0, 0))
        win.blit(passButton, (270, 530))


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

    def moves(self, win, sq, col, row):
        p = sq.piece
        b1 = False
        b3 = False
        # checks for correct piece
        if p.down:
            # up
            if self.turn == 1 or p.king:
                b1=self.leftU(win, col, row) or self.rightU(win, col, row)
            # down
            if self.turn == 2 or p.king:
                b3=self.leftD(win, col, row) or self.rightD(win, col, row)
        self.jumped = b1 or b3


    def leftU(self, win, col, row):
        if row - 1 > -1 and col - 1 > -1:
            # move
            if (self.s[col - 1][row - 1].state == 0) and not self.jumped:
                self.s[col - 1][row - 1].draw(win)
                self.doMove(col-1,row-1,col,row)
            # jump
            elif self.s[col - 1][row - 1].state == self.turn:
                pass
            elif row - 2 > -1 and col - 2 > -1:
                if self.s[col - 2][row - 2].state == 0 and self.s[col - 1][row - 1].state != 0:
                    self.s[col - 2][row - 2].draw(win)
                    self.doJump(win, col - 2, row - 2, col - 1, row - 1, col, row)
                    return True
        return False

    def rightU(self, win, col, row):
        if col + 1 < 8 and row - 1 > -1:
            # move
            if self.s[col + 1][row - 1].state == 0 and not self.jumped:
                self.s[col + 1][row - 1].draw(win)
                self.doMove(col + 1, row - 1, col, row)
            # jump
            elif self.s[col + 1][row - 1].state == self.turn:
                pass
            elif col + 2 < 8 and row - 2 > -1:
                if self.s[col + 2][row - 2].state == 0 and self.s[col + 1][row - 1].state != 0:
                    self.s[col + 2][row - 2].draw(win)
                    self.doJump(win, col + 2, row - 2, col + 1, row - 1, col, row)
                    return True
        return False

    def leftD(self, win, col, row):
        if row + 1 < 8 and col - 1 > -1:
            # move
            if self.s[col - 1][row + 1].state == 0 and not self.jumped:
                self.s[col - 1][row + 1].draw(win)
                self.doMove(col-1, row+1, col, row)
            # jump
            elif self.s[col - 1][row + 1].state == self.turn:
                pass
            elif row + 2 < 8 and col - 2 > -1:
                if self.s[col - 2][row + 2].state == 0 and self.s[col - 1][row + 1].state != 0:
                    self.s[col - 2][row + 2].draw(win)
                    self.doJump(win, col - 2, row + 2, col - 1, row + 1, col, row)
                    return True
        return False

    def rightD(self, win, col, row):
        if col + 1 < 8 and row + 1 < 8:
            # move
            if self.s[col + 1][row + 1].state == 0 and not self.jumped:
                self.s[col + 1][row + 1].draw(win)
                self.doMove(col + 1, row + 1, col, row)
            # jump
            elif self.s[col + 1][row + 1].state == self.turn:
                pass
            elif col + 2 < 8 and row + 2 < 8:
                if self.s[col + 2][row + 2].state == 0 and self.s[col + 1][row + 1].state != 0:
                    self.s[col + 2][row + 2].draw(win)
                    self.doJump(win, col+2,row+2,col+1,row+1,col,row)
                    return True
        return False

    def doMove(self, col, row, colP, rowP):
        if self.pressed:
            if self.s[col][row].checkMouse():
                self.s[col][row].setState(self.turn)
                # checks for king
                if self.s[colP][rowP].piece.king or (self.turn == 1 and row == 0) or (self.turn == 2 and row == 7):
                    self.s[col][row].piece.king = True
                self.s[colP][rowP].setState(0)
                self.doPass()

    def doJump(self, win, col, row, colJ, rowJ, colP, rowP):
        self.jumped = True
        if self.pressed:
            if self.s[col][row].checkMouse():
                self.s[col][row].setState(self.turn)
                # checks for king
                if self.s[colP][rowP].piece.king or self.turn == 1 and row == 0 or self.turn == 2 and row == 7:
                    self.s[col][row].piece.king = True
                self.s[colP][rowP].setState(0)
                self.s[colJ][rowJ].setState(0)
                self.s[col][row].piece.down = True
                #scroing
                if self.turn == 1:
                    self.p2 -= 1  # change to 1 later
                else:
                    self.p1 -= 1
                self.moves(win, self.s[col][row], col, row)
        if not self.jumped:
            self.s[col][row].piece.down = False
            self.doPass()
    def doPass(self):
        if self.turn == 1:
            self.turn = 2  # change to 1 later
        else:
            self.turn = 1




class Square:
    def __init__(self, c, r, piece):
        self.r = r
        self.c = c
        self.dis = 50
        # handle a piece object on square
        self.piece = piece
        self.state = 0
        if self.piece is None:
            l = 0
        elif self.piece.color == RED:
            l = 1
        else:
            l = 2
        self.setState(l)

    # --- getters and setters---
    def setState(self, l):
        self.state = l
        if l == 0:
            self.piece = None
        elif l == 1:
            self.piece = Piece(self.c, self.r, RED, False)
        else:
            self.piece = Piece(self.c, self.r, BLUE, False)

    def getX(self):
        return self.c * self.dis + 100

    def getY(self):
        return self.r * self.dis + 100

    # --- graphics ---
    def draw(self, win):
        pygame.draw.rect(win, (250, 20, 20), (self.getX(), self.getY(), self.dis, self.dis), 2)

    # --- logic ---

    def checkMouse(self):
        m = pygame.mouse.get_pos()
        r = self.getX() < m[0] < self.getX() + self.dis
        c = self.getY() < m[1] < self.getY() + self.dis
        if r and c:
            return True

    def moveLegal(self):
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
        #king piece
        self.king = king
        self.image = pygame.image.load('crown.png')
        self.image = pygame.transform.scale(self.image, (24, 24))

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
            win.blit(self.image, (x-13, y-12))

    def highlight(self,win,color):
        offset = 116 + self.r/2
        x = offset+self.col * self.board_size
        y = offset+self.row * self.board_size
        pygame.draw.circle(win, color, (int(x) - 1, int(y) - 1), int(self.r), 3)

    # --- logic ---




