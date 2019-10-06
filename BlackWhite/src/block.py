import pygame as py

class Block():
    '''A block in game chart'''
    
    def __init__(self,screen,x,y):
        self.screen = screen
        self.status = 'Blank'
        self.x = x
        self.y = y
        self.imageBlank = py.image.load("image/blank.png")
        self.imageBlack = py.image.load("image/black.png")
        self.imageWhite = py.image.load("image/white.png")
        self.imageAvailable = py.image.load("image/available.png")
        self.rect = self.imageBlank.get_rect()
        self.rect.centerx = self.x * 50 + 225
        self.rect.centery = self.y * 50 + 125
    
    def updateColor(self,color):
        self.status = color
                
    
    def blitme(self):
        if self.status == 'Blank':
            self.screen.blit(self.imageBlank, self.rect)
        if self.status == 'Black':
            self.screen.blit(self.imageBlack, self.rect)
        if self.status == 'White':
            self.screen.blit(self.imageWhite, self.rect)
        if self.status == 'Available':
            self.screen.blit(self.imageAvailable, self.rect)
        