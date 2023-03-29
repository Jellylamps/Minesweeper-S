import pygame
import sys
import os
import random


pygame.init()

def main():
    FPS = 30

#variable to represent image in same folder
    #TriHeart_Pic = pygame.image.load('Triheart.png')
#variable to represent image in sub-folder
    #BackG = pygame.image.load(os.path.join('testsprites','SandPunk.png'))
    Uncleared = pygame.image.load(os.path.join('minesprites','uncleared.jpg'))
    Empty = pygame.image.load(os.path.join('minesprites','empty.jpg'))
    Mine = pygame.image.load(os.path.join('minesprites','mine.jpg'))
    Flag = pygame.image.load(os.path.join('minesprites','flag.jpg'))
    Cell1 = pygame.image.load(os.path.join('minesprites','1.jpg'))
    Cell2 = pygame.image.load(os.path.join('minesprites','2.jpg'))
    Cell3 = pygame.image.load(os.path.join('minesprites','3.jpg'))
    Cell4 = pygame.image.load(os.path.join('minesprites','4.jpg'))
    Cell5 = pygame.image.load(os.path.join('minesprites','5.jpg'))
    Cell6 = pygame.image.load(os.path.join('minesprites','6.jpg'))
    Cell7 = pygame.image.load(os.path.join('minesprites','7.jpg'))
    Cell8 = pygame.image.load(os.path.join('minesprites','8.jpg'))
    S0 = pygame.image.load(os.path.join('minesprites','s0.jpg'))
    S1 = pygame.image.load(os.path.join('minesprites','s1.jpg'))
    S2 = pygame.image.load(os.path.join('minesprites','s2.jpg'))
    S3 = pygame.image.load(os.path.join('minesprites','s3.jpg'))
    S4 = pygame.image.load(os.path.join('minesprites','s4.jpg'))
    S5 = pygame.image.load(os.path.join('minesprites','s5.jpg'))
    S6 = pygame.image.load(os.path.join('minesprites','s6.jpg'))
    S7 = pygame.image.load(os.path.join('minesprites','s7.jpg'))
    S8 = pygame.image.load(os.path.join('minesprites','s8.jpg'))
    ExampleS1 = pygame.image.load(os.path.join('minesprites','ExampleS1.jpg'))
#resize BackG
    #BG = pygame.transform.scale(BackG,(500,500))


    x = 9
    y = 9
    mines = 10
    begin = True


    done = True
#    done = False
    while not done:
        x = input("columns: ")
        y = input("rows: ")
        mines = input("mines: ")


        try:
            mines = int(mines)
            x = int(x)
            y = int(y)
            if mines <= 0: print(youdiditwrong)
            if mines >= x*y: print(youdiditwrong)
            if x <= 0: print(youdiditwrong)
            if y <= 0: print(youdiditwrong)
            done = True
        except:
            print("Please enter positive integer numbers with fewer mines than cells.")



    board = [[[0,0] for item in range(x)] for item in range(y)]


    def startmenu():
        global menuquit
        menuquit = False
        menu = True
        instructions = False
        instruct = pygame.transform.scale(Mine,(boardwidth,boardheight))
        #box = pygame.Rect(190,190,100,40)
        while menu:
            WINDOW.fill((150,150,150))
            WINDOW.blit(FG,(spawnx,spawny))
            if instructions:
                #WINDOW.blit(instruct,(spawnx,spawny))
                WINDOW.blit(font.render("Standard Minesweeper rules apply.",True,(20,20,20)),(100,100))
                WINDOW.blit(font.render("Left click on uncleared cells to clear them.",True,(20,20,20)),(100,130))
                WINDOW.blit(font.render("Right click on uncleared cells to flag them.",True,(20,20,20)),(100,160))
                WINDOW.blit(font.render("Left click on flagged cells to change them to \"S\" cells.",True,(20,20,20)),(100,190))
                WINDOW.blit(font.render("\"S\" cells display yellow numbers indicating how many mines are adjacent.",True,(20,20,20)),(100,220))
                WINDOW.blit(font.render("The yellow number does not include the \"S\" cell IF it is a mine.",True,(20,20,20)),(100,250))
                WINDOW.blit(font.render("ANY uncleared cell can be an \"S\" cell, whether it is a mine or not.",True,(20,20,20)),(100,280))
                WINDOW.blit(font.render("Left click on \"S\" cells to revert them to flags.",True,(20,20,20)),(100,310))
                WINDOW.blit(font.render("Right click on \"S\" cells or flagged cells to unmark them.",True,(20,20,20)),(100,340))
            else:
                WINDOW.blit(titlefont.render("Minesweeper",True,(20,20,20)),(300,130))
                WINDOW.blit(titlefont.render("S",True,(244,254,84)),(440,180))
            WINDOW.blit(font.render("Press Enter",True,(20,20,20)),(390,450))
            if not instructions: WINDOW.blit(font.render("Press \"i\" for Instructions",True,(20,20,20)),(325,470))
            for event in pygame.event.get():
                key = pygame.key.get_pressed()
                if key[pygame.K_RETURN]: menu = False
                if key[pygame.K_i]: instructions = True
                if key[pygame.K_BACKSPACE]: instructions = False
                if event.type == pygame.QUIT:
                    menuquit = True
                    menu = False

            pygame.display.update()
            clock.tick(FPS)



    def menu():
        global menuquit
        global menux
        global menuy
        global menumines
        global menureset
        menureset = False
        menuquit = False
        menu = True
        invalid = False
        beginnerbox = pygame.Rect(.1*WIDTH+190,.1*HEIGHT+40,100,40)
        intermediatebox = pygame.Rect(.1*WIDTH+190,.1*HEIGHT+100,100,40)
        advancedbox = pygame.Rect(.1*WIDTH+190,.1*HEIGHT+160,100,40)
        brutalbox = pygame.Rect(.1*WIDTH+190,.1*HEIGHT+220,100,40)
        xbox = pygame.Rect(beginnerbox.x+120,beginnerbox.y,100,40)
        ybox = pygame.Rect(intermediatebox.x+120,intermediatebox.y,100,40)
        minesbox = pygame.Rect(advancedbox.x+120,advancedbox.y,100,40)
        startbox = pygame.Rect(brutalbox.x+120,brutalbox.y,100,40)
        text = ""
        xtext = str(x)
        ytext = str(y)
        minestext = str(mines)
        textpick = ""


        while menu:
            screenxtext = font.render(xtext,True,(80,80,80))
            screenytext = font.render(ytext,True,(80,80,80))
            screenminestext = font.render(minestext,True,(80,80,80))
            WINDOW.fill((115,115,115))
            WINDOW.blit(FG,(spawnx,spawny))
            pygame.draw.rect(WINDOW,(30,235,30),beginnerbox)
            pygame.draw.rect(WINDOW,(30,30,235),intermediatebox)
            pygame.draw.rect(WINDOW,(30,30,30),advancedbox)
            pygame.draw.rect(WINDOW,(235,30,30),brutalbox)
            WINDOW.blit(font.render("Easy",True,(40,40,60)),(beginnerbox.x+7,beginnerbox.y+10))
            WINDOW.blit(font.render("Medium",True,(20,20,40)),(intermediatebox.x+7,intermediatebox.y+10))
            WINDOW.blit(font.render("Hard",True,(180,180,180)),(advancedbox.x+7,advancedbox.y+10))
            WINDOW.blit(font.render("Brutal",True,(220,220,40)),(brutalbox.x+7,brutalbox.y+10))
            if textpick == "x": pygame.draw.rect(WINDOW,(235,235,235),xbox)
            else: pygame.draw.rect(WINDOW,(255,255,255),xbox)
            if textpick == "y": pygame.draw.rect(WINDOW,(235,235,235),ybox)
            else: pygame.draw.rect(WINDOW,(255,255,255),ybox)
            if textpick == "mines": pygame.draw.rect(WINDOW,(235,235,235),minesbox)
            else: pygame.draw.rect(WINDOW,(255,255,255),minesbox)
            pygame.draw.rect(WINDOW,(30,30,30),startbox)
            WINDOW.blit(screenxtext,(xbox.x+10,xbox.y+10))
            WINDOW.blit(font.render("Columns",True,(40,40,40)),(xbox.x+115,xbox.y+10))
            WINDOW.blit(screenytext,(ybox.x+10,ybox.y+10))
            WINDOW.blit(font.render("Rows",True,(40,40,40)),(ybox.x+115,ybox.y+10))
            WINDOW.blit(screenminestext,(minesbox.x+10,minesbox.y+10))
            WINDOW.blit(font.render("Mines",True,(40,40,40)),(minesbox.x+115,minesbox.y+10))
            WINDOW.blit(font.render("START",True,(250,250,20)),(startbox.x+10,startbox.y+10))
            if not begin: WINDOW.blit(font.render("Press the Escape Key to Resume",True,(20,20,20)),(280,460))
            if invalid:
                WINDOW.blit(font.render("Please enter positive integers",True,(40,40,40)),(brutalbox.x+10,minesbox.y+130))
                WINDOW.blit(font.render("with fewer mines than cells.",True,(40,40,40)),(brutalbox.x+10,minesbox.y+160))

            if textpick == "x": text = xtext
            elif textpick == "y": text = ytext
            elif textpick == "mines": text = minestext

            menux = x
            if xtext != str(x): menux = xtext
            menuy = y
            if ytext != str(y): menuy = ytext
            menumines = mines
            if minestext != str(mines): menumines = minestext

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    menuquit = True
                    menu = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE: text = text[:-1]
                    else:
                        if (len(text) < 3 or (textpick == "mines" and len(text) < 6)): text += event.unicode.strip()
                    key = pygame.key.get_pressed()
                    if key[pygame.K_RETURN]:
                        try:
                            menux = int(menux)
                            menuy = int(menuy)
                            menumines = int(menumines)
                            if menumines <= 0: youdiditwrong = yep
                            if menumines >= menux*menuy: youdiditwrong = yep
                            if menux <= 0: youdiditwrong = yep
                            if menuy <= 0: youdiditwrong = yep
                            invalid = False
                            menureset = True
                            menu = False
                        except:
                            invalid = True
                            textpick = ""
                    elif (key[pygame.K_ESCAPE] and not begin):
                        menux = x
                        menuy = y
                        menumines = mines
                        menu = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if beginnerbox.collidepoint(event.pos):
                        xtext = "9"
                        ytext = "9"
                        minestext = "10"
                        #menureset = True
                        #menu = False
                    elif intermediatebox.collidepoint(event.pos):
                        xtext = "16"
                        ytext = "16"
                        minestext = "40"
                        #menureset = True
                        #menu = False
                    elif advancedbox.collidepoint(event.pos):
                        xtext = "30"
                        ytext = "16"
                        minestext = "99"
                        #menureset = True
                        #menu = False
                    elif brutalbox.collidepoint(event.pos):
                        xtext = "16"
                        ytext = "16"
                        minestext = "120"
                        #menureset = True
                        #menu = False
                    elif xbox.collidepoint(event.pos):
                        textpick = "x"
                        text = xtext
                    elif ybox.collidepoint(event.pos):
                        textpick = "y"
                        text = ytext
                    elif minesbox.collidepoint(event.pos):
                        textpick = "mines"
                        text = minestext
                    elif startbox.collidepoint(event.pos):
                        try:
                            menux = int(menux)
                            menuy = int(menuy)
                            menumines = int(menumines)
                            if menumines <= 0: youdiditwrong = yep
                            if menumines >= menux*menuy: youdiditwrong = yep
                            if menux <= 0: youdiditwrong = yep
                            if menuy <= 0: youdiditwrong = yep
                            invalid = False
                            menureset = True
                            menu = False
                        except:
                            invalid = True
                            textpick = ""
            if textpick == "x": xtext = text
            elif textpick == "y": ytext = text
            elif textpick == "mines": minestext = text

            pygame.display.update()
            clock.tick(FPS)


    def distribute(x,y,mines):
        while mines != 0:
            xloc = random.randint(0,x-1)
            yloc = random.randint(0,y-1)
            #print(xloc+1,yloc+1)
            if board[yloc][xloc] == ["X",0]:
                #print("repeat at",(xloc+1),",",(yloc+1))
                mines = mines+1
            board[yloc][xloc] = ["X",0]
            mines = mines-1


    def adjacentinc(x,y):
        line = 0
        spot = 0
        while line != y:
            while spot != x:
                #print(line+1,spot+1)
                if board[line][spot] == [0,0]:
                    #print("row",line+1,"column",spot+1)
                    if spot !=0:
                        if board[line][spot-1] == ["X",0]: board[line][spot][0] = int(board[line][spot][0])+1
                        if line !=0:
                            if board[line-1][spot-1] == ["X",0]: board[line][spot][0] = int(board[line][spot][0])+1
                        if line !=y-1:
                            if board[line+1][spot-1] == ["X",0]: board[line][spot][0] = int(board[line][spot][0])+1
                    if spot !=x-1:
                        if board[line][spot+1] == ["X",0]: board[line][spot][0] = int(board[line][spot][0])+1
                        if line !=0:
                            if board[line-1][spot+1] == ["X",0]: board[line][spot][0] = int(board[line][spot][0])+1
                        if line !=y-1:
                            if board[line+1][spot+1] == ["X",0]: board[line][spot][0] = int(board[line][spot][0])+1
                    if line !=0:
                        if board[line-1][spot] == ["X",0]: board[line][spot][0] = int(board[line][spot][0])+1
                    if line !=y-1:
                        if board[line+1][spot] == ["X",0]: board[line][spot][0] = int(board[line][spot][0])+1
                spot = spot+1
            spot = 0
            line = line+1


    def emptyclear():
        active = True
        cleared = 0
        line = 0
        spot = 0
        while active:
            while line != y:
                while spot != x:
                    if (board[line][spot][0] == 0 and board[line][spot][1] == 1):
                        if spot !=0:
                            if board[line][spot-1][1] != 1:
                                board[line][spot-1][1] = 1
                                cleared = cleared+1
                            if (line !=0 and  board[line-1][spot-1][1] != 1):
                                board[line-1][spot-1][1] = 1
                                cleared = cleared+1
                            if (line !=y-1 and board[line+1][spot-1][1] != 1):
                                board[line+1][spot-1][1] = 1
                                cleared = cleared+1
                        if spot !=x-1:
                            if board[line][spot+1][1] != 1:
                                board[line][spot+1][1] = 1
                                cleared = cleared+1
                            if (line !=0 and board[line-1][spot+1][1] != 1):
                                board[line-1][spot+1][1] = 1
                                cleared = cleared+1
                            if (line !=y-1 and board[line+1][spot+1][1] != 1):
                                board[line+1][spot+1][1] = 1
                                cleared = cleared+1
                        if (line !=0 and board[line-1][spot][1] != 1):
                            board[line-1][spot][1] = 1
                            cleared = cleared+1
                        if (line !=y-1 and board[line+1][spot][1] != 1):
                            board[line+1][spot][1] = 1
                            cleared = cleared+1
                    spot = spot+1
                spot = 0
                line = line+1
            if cleared == 0: active = False
            cleared = 0
            line = 0


    def startflag():
        for row in board:
            z = board.index(row)
            for cell in row:
                w = row.index(cell)
                if (board[z][w][1] == 1 and board[z][w][0] == "X"): board[z][w][1] = 2


    def autoclear(line,spot):
        finc = 0
        if spot !=0:
            if board[line][spot-1][1] == 2: finc = finc+1
            if line !=0:
                if board[line-1][spot-1][1] == 2: finc = finc+1
            if line !=y-1:
                if board[line+1][spot-1][1] == 2: finc = finc+1
        if spot !=x-1:
            if board[line][spot+1][1] == 2: finc = finc+1
            if line !=0:
                if board[line-1][spot+1][1] == 2: finc = finc+1
            if line !=y-1:
                if board[line+1][spot+1][1] == 2: finc = finc+1
        if (line !=0 and board[line-1][spot][1] == 2): finc = finc+1
        if (line !=y-1 and board[line+1][spot][1] == 2): finc = finc+1
        if finc == board[line][spot][0]:
            if spot !=0:
                if board[line][spot-1][1] != 2: board[line][spot-1][1] = 1
                if (line !=0 and board[line-1][spot-1][1] != 2): board[line-1][spot-1][1] = 1
                if (line !=y-1 and board[line+1][spot-1][1] != 2): board[line+1][spot-1][1] = 1
            if spot !=x-1:
                if board[line][spot+1][1] != 2: board[line][spot+1][1] = 1
                if (line !=0 and board[line-1][spot+1][1] != 2): board[line-1][spot+1][1] = 1
                if (line !=y-1and board[line+1][spot+1][1] != 2): board[line+1][spot+1][1] = 1
            if (line !=0 and board[line-1][spot][1] != 2): board[line-1][spot][1] = 1
            if (line !=y-1 and board[line+1][spot][1] != 2): board[line+1][spot][1] = 1

#increment yellow number on spot
    def sinc(line,spot):
        s = 0
        if board[line][spot][0] != "X": s = board[line][spot][0]
        elif board[line][spot][0] == "X":
            if spot !=0:
                if board[line][spot-1][0] == "X": s = s+1
                if line !=0:
                    if board[line-1][spot-1][0] == "X": s = s+1
                if line !=y-1:
                    if board[line+1][spot-1][0] == "X": s = s+1
            if spot !=x-1:
                if board[line][spot+1][0] == "X": s = s+1
                if line !=0:
                    if board[line-1][spot+1][0] == "X": s = s+1
                if line !=y-1:
                    if board[line+1][spot+1][0] == "X": s = s+1
            if (line !=0 and board[line-1][spot][0] == "X"): s = s+1
            if (line !=y-1 and board[line+1][spot][0] == "X"): s = s+1
        board[line][spot][1] = s+3

    distribute(x,y,mines)
    adjacentinc(x,y)

#produce window/display with name

    WIDTH, HEIGHT = 900, 500
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Minesweeper S")

#size the board on screen
    def draw():
        global boardwidth
        global boardheight
        global spawnx
        global spawny
        global celldim
        global FG
        if WIDTH/x <= HEIGHT/y:
            boardwidth = 0.8*WIDTH
            boardheight = (boardwidth/x)*y
            spawnx = 0.1*WIDTH
            spawny = (HEIGHT-boardheight)/2
        else:
            boardheight = 0.8*HEIGHT
            boardwidth = (boardheight/y)*x
            spawny = 0.1*HEIGHT
            spawnx = (WIDTH-boardwidth)/2
        celldim = boardwidth/x
        FG = pygame.transform.scale(Uncleared,(boardwidth,boardheight))

    draw()

#game loop
    clock = pygame.time.Clock()
    titlefont = pygame.font.SysFont(None,72)
    font = pygame.font.SysFont(None,32)
    time = 0
    displaytime = "0000"
    closeout = False
    playing = True
    progress = True
    start = True
    win = False
    lose = False
    while playing:
        while progress:
            if begin: progress = False
            global xout
            xout = False
            for event in pygame.event.get():
                #close window when X clicked
                if event.type == pygame.QUIT:
                    xout = True
                    progress = False
                elif event.type == pygame.KEYDOWN:
                    key = pygame.key.get_pressed()
                    #reset game with same settings
                    if key[pygame.K_RETURN]:
                        progress = False
                    if key[pygame.K_r]:
                        start = True
                        board = [[[0,0] for item in range(x)] for item in range(y)]
                        distribute(x,y,mines)
                        adjacentinc(x,y)

                #report mouse clicks
                elif (event.type == pygame.MOUSEBUTTONDOWN and not win):
                    if event.button == 1:
                        leftclick = pygame.mouse.get_pos()
                        #print("left click at ", leftclick)
                        if (leftclick[0] >= spawnx and leftclick[0] < spawnx+boardwidth):
                            if (leftclick[1] >= spawny and leftclick[1] < spawny+boardheight):
                                clickx = leftclick[0]-spawnx
                                unitx = int(clickx/boardwidth*x)
                                #print(unitx)
                                clicky = leftclick[1]-spawny
                                unity = int(clicky/boardheight*y)
                                #print(unity)
                                if board[unity][unitx][1] == 0: board[unity][unitx][1] = 1
                                elif board[unity][unitx][1] == 2: sinc(unity,unitx)
                                elif board[unity][unitx][1] > 2: board[unity][unitx][1] = 2
                                if start:
                                    if unitx != 0:
                                        board[unity][unitx-1][1] = 1
                                        if unity != 0: board[unity-1][unitx-1][1] = 1
                                        if unity != y-1: board[unity+1][unitx-1][1] = 1
                                    if unitx != x-1:
                                        board[unity][unitx+1][1] = 1
                                        if unity != 0: board[unity-1][unitx+1][1] = 1
                                        if unity != y-1: board[unity+1][unitx+1][1] = 1
                                    if unity != 0: board[unity-1][unitx][1] = 1
                                    if unity != y-1: board[unity+1][unitx][1] = 1
                                    startflag()
                                    start = False
                                if board[unity][unitx][1] == 1: autoclear(unity,unitx)
                                emptyclear()

                    elif (event.button == 3 and not start):
                        rightclick = pygame.mouse.get_pos()
                        #print("right click at ", rightclick)
                        if (rightclick[0] >= spawnx and rightclick[0] < spawnx+boardwidth):
                            if (rightclick[1] >= spawny and rightclick[1] < spawny+boardheight):
                                clickx = rightclick[0]-spawnx
                                unitx = int(clickx/boardwidth*x)
                                #print(unitx)
                                clicky = rightclick[1]-spawny
                                unity = int(clicky/boardheight*y)
                                #print(unity)
                                if board[unity][unitx][1] == 0: board[unity][unitx][1] = 2
                                elif board[unity][unitx][1] > 1: board[unity][unitx][1] = 0
            #MatrixBup.emptyclear()
            WINDOW.fill((150,150,150))
            if win: WINDOW.fill((100,220,100))
            if lose: WINDOW.fill((220,100,100))
            #if time > 5000: WINDOW.fill((150,150,220))
            #draw images with locarion of top left pixel
            #WINDOW.blit(BG,(WIDTH/2-250,HEIGHT/2-250))
            #WINDOW.blit(TriHeart_Pic,(WIDTH/2-153,HEIGHT/2-153))
            #WINDOW.blit(Uncleared,(0,0))
            #WINDOW.blit(Empty,(700,0))
            #WINDOW.blit(Mine,(700,200))
            WINDOW.blit(FG,(spawnx,spawny))
            WINDOW.blit(font.render(displaytime[:len(displaytime)-3] + "." + displaytime[len(displaytime)-3],True,(20,20,20)),(430,15))
            if (win or lose):
                WINDOW.blit(font.render("Menu: Press the Enter Key",True,(20,20,20)),(310,470))
                WINDOW.blit(font.render("Press \"r\" to Restart",True,(20,20,20)),(350,450))
            #WINDOW.blit(font.render(displaytime,True,(40,40,40)),(10,450))
            #WINDOW.blit(font.render(str(len(displaytime)),True,(40,40,40)),(10,470))
            win = False
            lose = False
            z = 0
            w = 0
            cleared = 0
            while z != y:
                while w != x:
                    if board[z][w][0] == 0:
                        WINDOW.blit(pygame.transform.scale(Empty,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][0] == "X":
                        WINDOW.blit(pygame.transform.scale(Mine,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][0] == 1:
                        WINDOW.blit(pygame.transform.scale(Cell1,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][0] == 2:
                        WINDOW.blit(pygame.transform.scale(Cell2,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][0] == 3:
                        WINDOW.blit(pygame.transform.scale(Cell3,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][0] == 4:
                        WINDOW.blit(pygame.transform.scale(Cell4,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][0] == 5:
                        WINDOW.blit(pygame.transform.scale(Cell5,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][0] == 6:
                        WINDOW.blit(pygame.transform.scale(Cell6,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][0] == 7:
                        WINDOW.blit(pygame.transform.scale(Cell7,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][0] == 8:
                        WINDOW.blit(pygame.transform.scale(Cell8,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    if board[z][w][1] == 0:
                        WINDOW.blit(pygame.transform.scale(Uncleared,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][1] == 2:
                        WINDOW.blit(pygame.transform.scale(Flag,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][1] == 3:
                        WINDOW.blit(pygame.transform.scale(S0,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][1] == 4:
                        WINDOW.blit(pygame.transform.scale(S1,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][1] == 5:
                        WINDOW.blit(pygame.transform.scale(S2,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][1] == 6:
                        WINDOW.blit(pygame.transform.scale(S3,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][1] == 7:
                        WINDOW.blit(pygame.transform.scale(S4,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][1] == 8:
                        WINDOW.blit(pygame.transform.scale(S5,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][1] == 9:
                        WINDOW.blit(pygame.transform.scale(S6,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][1] == 10:
                        WINDOW.blit(pygame.transform.scale(S7,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    elif board[z][w][1] == 11:
                        WINDOW.blit(pygame.transform.scale(S8,(celldim,celldim)),(spawnx+w*celldim,spawny+z*celldim))
                    if (board[z][w][1] == 1 and board[z][w][0] != "X"): cleared = cleared+1
                    if (board[z][w][1] == 1 and board[z][w][0] == "X" and start == False): lose = True
                    w = w+1
                if cleared == x*y-mines: win = True
                w = 0
                z = z+1
            #MatrixBup.emptyclear()
            pygame.display.update()
            clock.tick(FPS)
            if (not start and not win and not lose): time = time + clock.get_time()
            if time >= 10000000: time = 9999999
            if start: time = 0
            displaytime = str(time)
            if len(displaytime) == 1: displaytime = "000" + displaytime
            elif len(displaytime) == 2: displaytime = "00" + displaytime
            elif len(displaytime) == 3: displaytime = "0" + displaytime
            if xout:pygame.quit()

        if xout: break
        if begin: startmenu()
        if menuquit: break
        menu()
        begin = False
        if menuquit: break
        reset = True
        if (x == menux and y == menuy and mines == menumines):
            progress = True
            reset = False
        if menureset: reset = True
        if reset:
            x = menux
            y = menuy
            mines = menumines
            start = True
            board = [[[0,0] for item in range(x)] for item in range(y)]
            draw()
            distribute(x,y,mines)
            adjacentinc(x,y)
            progress = True
    if playing == False: pygame.quit()

#"__main__" NO MATTER WHAT THE PROJECT IS TITLED
if __name__ == "__main__": main()


#print("pog?")
