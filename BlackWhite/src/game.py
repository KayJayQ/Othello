import pygame as py
from block import Block
import socket

class Game:
    '''Game class'''
    
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.chartImage = py.image.load("image/chart.png")
        self.chartRect = self.chartImage.get_rect()
        self.chartRect.centerx = self.screen.get_rect().centerx
        self.chartRect.centery = self.screen.get_rect().centery
        self.blackNumber = 2
        self.whiteNumber = 2
        
        self.tempx = 0
        self.tempy = 0
        
        self.round = True
        
        self.blocks = []
        
        self.initialize()
        self.initializeScoreBoard()
        
    
    def initialize(self):
        '''Create first four blocks'''
        for x in range(8):
            for y in range(8):
                self.blocks.append(Block(self.screen,x,y))
        self.getBlock(3,3).updateColor("White")
        self.getBlock(3,4).updateColor("Black")
        self.getBlock(4,3).updateColor("Black")
        self.getBlock(4,4).updateColor("White")
        
    def initializeScoreBoard(self):
        self.ScoreText = py.font.Font('freesansbold.ttf',15).render(f"Scores (Black:White): {self.whiteNumber} : {self.blackNumber} , {'White' if self.round else 'Black'} Turn", True, (50,50,50))
        self.ScoreTextRect = self.ScoreText.get_rect()
        self.ScoreTextRect.center = ((self.settings.screen_width/4),(self.screen.get_rect().top+50))
        
        self.ScoreNumber = py.font.Font('freesansbold.ttf',20).render("", True, (200,10,10))
        self.ScoreNumberRect = self.ScoreNumber.get_rect()
        self.ScoreNumberRect.center = ((self.settings.screen_width/2),(self.screen.get_rect().top+50))
    
    def isAvailable(self,x,y):
        '''Check if given block is available'''
        try:
            myColor = self.getBlock(x,y)
            test = myColor.status
        except:
            return False
        #First the block should be blank
        if myColor.status != 'Blank':
            return False
        #Second the block should be next to a different colored block
        left = self.getBlock(x-1, y)
        right = self.getBlock(x+1, y)
        up = self.getBlock(x, y-1)
        down = self.getBlock(x, y+1)
        upleft = self.getBlock(x-1,y-1)
        upright = self.getBlock(x+1,y-1)
        downleft = self.getBlock(x-1,y+1)
        downright = self.getBlock(x+1,y+1)
        colors = list(filter(lambda x:x!=None,[left,right,up,down,upleft,upright,downleft,downright]))
        colors = [i.status for i in colors]
        if sum([1 if i == None else 0 for i in [right,left,up,down,upleft,upright,downleft,downright]]) == 4:
            return False
        if self.round == False and 'White' not in colors:
            return False
        if self.round == True and 'Black' not in colors:
            return False
        #Third check if this line can be inverted
        #Assume it can be there
        self.getBlock(x,y).updateColor('White' if self.round else 'Black')
        if len(self.invertFrom(x, y)) == 0:
            self.getBlock(x,y).updateColor('Blank')
            return False
        self.getBlock(x,y).updateColor('Blank')
        return True
    
    def invertFrom(self,x,y):
        if self.getBlock(x,y).status == 'Black':
            color = 'Black'
            rcolor = 'White'
        else:
            color = 'White'
            rcolor = 'Black'
        TodoList = []
        temp = []
        
        #up
        for i in range(y-1,-1,-1):
            if self.getBlock(x,i).status == rcolor:
                temp.append(self.getBlock(x,i))
                continue
            if self.getBlock(x,i).status == 'Blank':
                break
            if self.getBlock(x,i).status == color:
                TodoList.extend(temp)
                break
        temp.clear()
        #down
        for i in range(y+1,8):
            if self.getBlock(x,i).status == rcolor:
                temp.append(self.getBlock(x,i))
                continue
            if self.getBlock(x,i).status == 'Blank':
                break
            if self.getBlock(x,i).status == color:
                TodoList.extend(temp)
                break
        temp.clear()
        #left
        for i in range(x-1,-1,-1):
            if self.getBlock(i,y).status == rcolor:
                temp.append(self.getBlock(i,y))
                continue
            if self.getBlock(i,y).status == 'Blank':
                break
            if self.getBlock(i,y).status == color:
                TodoList.extend(temp)
                break
        temp.clear()
        #right
        for i in range(x+1,8):
            if self.getBlock(i,y).status == rcolor:
                temp.append(self.getBlock(i,y))
                continue
            if self.getBlock(i,y).status == 'Blank':
                break
            if self.getBlock(i,y).status == color:
                TodoList.extend(temp)
                break
        temp.clear()
        #up left
        for i in range(1,min((x,y))):
            if self.getBlock(x-i,y-i).status == rcolor:
                temp.append(self.getBlock(x-i,y-i))
                continue
            if self.getBlock(x-i,y-i).status == 'Blank':
                break
            if self.getBlock(x-i,y-i).status == color:
                TodoList.extend(temp)
                break
        temp.clear()
        #up right
        for i in range(1,min((7-x,y))):
            if self.getBlock(x+i,y-i).status == rcolor:
                temp.append(self.getBlock(x+i,y-i))
                continue
            if self.getBlock(x+i,y-i).status == 'Blank':
                break
            if self.getBlock(x+i,y-i).status == color:
                TodoList.extend(temp)
                break
        temp.clear()
        #down left
        for i in range(1,min((x,7-y))):
            if self.getBlock(x-i,y+i).status == rcolor:
                temp.append(self.getBlock(x-i,y+i))
                continue
            if self.getBlock(x-i,y+i).status == 'Blank':
                break
            if self.getBlock(x-i,y+i).status == color:
                TodoList.extend(temp)
                break
        temp.clear()
        #down right
        for i in range(1,min((7-x,7-y))):
            if self.getBlock(x+i,y+i).status == rcolor:
                temp.append(self.getBlock(x+i,y+i))
                continue
            if self.getBlock(x+i,y+i).status == 'Blank':
                break
            if self.getBlock(x+i,y+i).status == color:
                TodoList.extend(temp)
                break
        temp.clear()
        return TodoList
    
    def invertExcute(self,x,y):
        TodoList = self.invertFrom(x,y)
        for i in TodoList:
            i.updateColor(self.getBlock(x,y).status)
            
    def getFromInternet(self):
        if self.settings.multi_main:
            data = self.settings.server_conn.recv(1024).decode()
            x = int(data.split()[0])
            y = int(data.split()[1])
            return (x,y)
        else:
            print("start listening")
            data = self.settings.client.recv(1024).decode()
            print("end listening",data)
            x = int(data.split()[0])
            y = int(data.split()[1])
            return (x,y)
                
    
    def sendToInternet(self,x,y):
        if self.settings.multi_main:
            self.settings.server_conn.send(f"{x} {y}".encode('utf-8'))
        else:
            self.settings.client.send(f"{x} {y}".encode('utf-8'))
    
    def mouse_event(self,mouseX,mouseY):
        x = (mouseX - 200) // 50
        y = (mouseY - 100) // 50
        if not self.isAvailable(x,y):
            return False
        try:
            if self.round:
                self.getBlock(x,y).updateColor("White")
            else:
                self.getBlock(x,y).updateColor("Black")
        except:
            pass
        self.round = not self.round
        self.invertExcute(x, y)
        self.blackNumber = sum([1 if i.status == 'Black' else 0 for i in self.blocks])
        self.whiteNumber = sum([1 if i.status == 'White' else 0 for i in self.blocks])
        self.checkWin()
        self.tempx = x
        self.tempy = y
    
    def webActions(self,x,y):
        if self.settings.multi_main:
            if not self.round:
                self.sendToInternet(x,y)
                newx,newy = self.getFromInternet()
                self.mouse_event( newx*50+201,newy*50+101)
        else:
            if self.round:
                if x!=10 and y!=10:
                    self.sendToInternet(x, y)
                newx,newy = self.getFromInternet()
                self.mouse_event(newx*50+201,newy*50+101)
        
    def checkWin(self):
        if self.blackNumber + self.whiteNumber == 64:
            if self.blackNumber > self.whiteNumber:
                self.ScoreNumber = py.font.Font('freesansbold.ttf',20).render("Black Wins", True, (200,10,10))
            if self.blackNumber < self.whiteNumber:
                self.ScoreNumber = py.font.Font('freesansbold.ttf',20).render("White Wins", True, (200,10,10))
            if self.blackNumber == self.whiteNumber:
                self.ScoreNumber = py.font.Font('freesansbold.ttf',20).render("Draw", True, (200,10,10))
        available = []
        for i in self.blocks:
            if i.status == 'Blank' and self.isAvailable(i.x, i.y):
                available.append(True)
            else:
                available.append(False)
        if not any(available):
            if self.blackNumber > self.whiteNumber:
                self.ScoreNumber = py.font.Font('freesansbold.ttf',20).render("Black Wins", True, (200,10,10))
            if self.blackNumber < self.whiteNumber:
                self.ScoreNumber = py.font.Font('freesansbold.ttf',20).render("White Wins", True, (200,10,10))
            if self.blackNumber == self.whiteNumber:
                self.ScoreNumber = py.font.Font('freesansbold.ttf',20).render("Draw", True, (200,10,10))
        
    def getBlock(self,x,y):
        for block in self.blocks:
            if block.x == x and block.y == y:
                return block
        return None
    
    def blitme(self):
        #print(Block.blankBlock,Block.blackBlock,Block.whiteBlock)
        self.ScoreText = py.font.Font('freesansbold.ttf',15).render(f"Scores (Black:White): {self.whiteNumber} : {self.blackNumber} , {'White' if self.round else 'Black'} Turn", True, (50,50,50))
        self.screen.blit(self.chartImage, self.chartRect)
        self.screen.blit(self.ScoreText, self.ScoreTextRect)
        self.screen.blit(self.ScoreNumber, self.ScoreNumberRect)
        for block in self.blocks:
            block.blitme()