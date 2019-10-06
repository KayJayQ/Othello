import pygame

class Menu():
    '''Class creates game menu at start'''
    def __init__(self, settings, screen):
        '''Initializes the screen and display menu options'''
        self.screen = screen
        self.settings = settings
        
        #Get Screen Rect
        self.screenRect = screen.get_rect()
        
        #Load logo and put it on the screen
        self.logoImage = pygame.image.load("image/title.png")
        self.logoRect = self.logoImage.get_rect()
        self.logoRect.centerx = self.screenRect.centerx
        self.logoRect.top = self.screenRect.top + 50
        
        #Title
        self.TitleText = pygame.font.Font('freesansbold.ttf',60).render("Othello by QKJ", True, (10,10,200))
        self.TitleRect = self.TitleText.get_rect()
        self.TitleRect.center = ((self.settings.screen_width/2),(self.screenRect.top+300))
        
        #Selection items QUIT
        UnderlineFont = pygame.font.Font('freesansbold.ttf',30)
        UnderlineFont.set_underline(True)
        self.QuitItem = UnderlineFont.render("Exit", True, (100,10,10))
        self.QuitRect = self.QuitItem.get_rect()
        self.QuitRect.center = ((self.settings.screen_width/2),(self.screenRect.bottom-100))
        
        #Selection items OPTIONS
        self.OptionsItem = UnderlineFont.render("Internet", True, (100,10,10))
        self.OptionsRect = self.OptionsItem.get_rect()
        self.OptionsRect.center = ((self.settings.screen_width/2),(self.screenRect.bottom-150))
        
        #Selection items Start
        self.StartItem = UnderlineFont.render("Start", True, (100,10,10))
        self.StartRect = self.StartItem.get_rect()
        self.StartRect.center = ((self.settings.screen_width/2),(self.screenRect.bottom-200))
        
        #Add all items into list and give them an unique index
        self.items = [(self.StartRect,0),(self.OptionsRect,1),(self.QuitRect,2)]
        
    def mouse_event(self, mx, my):
        '''Take mouse coordinate then take action of each selections'''
        for (item,index) in self.items:
            if mx > item.left and mx < item.right and my > item.top and my < item.bottom:
                if index == 0:
                    self.startGame()
                if index == 1:
                    self.options()
                if index == 2:
                    pygame.quit()
                    quit()
                return True
        return False
        
    def startGame(self):
        '''Start a new game'''
        self.result = "Start"
    
    def options(self):
        '''Display options'''
        self.result = "Multi"
    
    def blitme(self):
        '''Draw current menu'''
        #Logo
        self.screen.blit(self.logoImage, self.logoRect)
        #Title
        self.screen.blit(self.TitleText, self.TitleRect)
        #Items
        self.screen.blit(self.QuitItem, self.QuitRect)
        self.screen.blit(self.OptionsItem, self.OptionsRect)
        self.screen.blit(self.StartItem, self.StartRect)