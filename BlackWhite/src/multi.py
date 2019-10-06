import pygame
import internet

class Multi:
    
    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.screenRect = self.screen.get_rect()
        
        self.Font0 = pygame.font.Font('freesansbold.ttf',30)
        
        self.ModeItem = self.Font0.render("Play as a host", True, (100,10,10))
        self.ModeRect = self.ModeItem.get_rect()
        self.ModeRect.center = ((self.settings.screen_width/2),(self.screenRect.top+50))
        
        
        self.clientHintItem = self.Font0.render("Please Enter Host IP Address and Port Number", True, (100,10,10))
        self.clientHintRect = self.clientHintItem.get_rect()
        self.clientHintRect.center = ((self.settings.screen_width/2),(self.screenRect.top+100))
        
        self.ip = ""
        self.IPItem = self.Font0.render(self.ip, True, (100,10,10))
        self.IPRect = self.IPItem.get_rect()
        self.IPRect.center = (self.settings.screen_width/2, self.screenRect.top+150)
        
        
        self.hostHintItem = self.Font0.render("Tell Your Friend Your IP and Port is ", True, (100,10,10))
        self.hostHintRect = self.hostHintItem.get_rect()
        self.hostHintRect.center = ((self.settings.screen_width/2),(self.screenRect.top+100))
        
        self.ip = internet.getIP()
        self.IPItem = self.Font0.render(self.ip+":4235", True, (100,10,10))
        
        self.confirmItem = self.Font0.render("Confirm Settings", True, (100,10,10))
        self.confirmRect = self.confirmItem.get_rect()
        self.confirmRect.center = (self.settings.screen_width/2, self.screenRect.top+200)
        
        self.doneItem = self.Font0.render("Undone", True, (100,10,10))
        self.doneRect = self.doneItem.get_rect()
        self.doneRect.center = (self.settings.screen_width/2, self.screenRect.top+250)
        
        self.settingItems = [(self.ModeRect,0),(self.confirmRect,1)]
        
        
    def change_mode(self):
        if self.settings.multi_main:
            self.ip = ""
            self.settings.multi_main = not self.settings.multi_main
            self.ModeItem = self.Font0.render("Play as a guest", True, (100,10,10))
        else:
            self.settings.multi_main = not self.settings.multi_main
            self.ModeItem = self.Font0.render("Play as a host", True, (100,10,10))
            self.ip = internet.getIP()
            self.IPItem = self.Font0.render(self.ip+":4235", True, (100,10,10))
            
    def confirm(self):
        if self.settings.multi_main:
            self.settings.server_ip = self.ip
            self.settings.server.bind((self.settings.server_ip,4235))
            self.settings.server.listen(5)
            while True:
                conn, addr = self.settings.server.accept()
                try:
                    data = conn.recv(1024)
                    if data.decode() == "CHINANO.1":
                        self.settings.multiplay = True
                        conn.send("Confirmed".encode(encoding='utf_8', errors='strict'))
                        self.doneItem =  self.Font0.render("Done", True, (100,10,10))
                        self.settings.server_conn = conn
                        break
                except ConnectionError:
                    break
        else:
            self.settings.server_ip = self.ip[:-5]
            self.settings.server_port = int(self.ip[-4:])
            self.settings.client.connect((self.settings.server_ip,self.settings.server_port))
            while True:
                msg = "CHINANO.1"
                try:
                    self.settings.client.send(msg.encode('utf_8'))
                except OSError:
                    pass
                data = self.settings.client.recv(1024)
                if data.decode() == "Confirmed":
                    self.settings.multiplay = True
                    self.doneItem = self.Font0.render("Done", True, (100,10,10))
                    break
                
    
    def mouse_event(self, x, y):
        for (item,index) in self.settingItems:
            if x < item.right and x > item.left and y < item.bottom and y > item.top:
                if index == 0:
                    self.change_mode()
                if index == 1:
                    self.confirm()
    
    def key_event(self, keyPressed):
        if self.settings.multi_main:
            return
        if keyPressed == pygame.K_0:
            self.ip += '0'
        if keyPressed == pygame.K_1:
            self.ip += '1'
        if keyPressed == pygame.K_2:
            self.ip += '2'
        if keyPressed == pygame.K_3:
            self.ip += '3'
        if keyPressed == pygame.K_4:
            self.ip += '4'
        if keyPressed == pygame.K_5:
            self.ip += '5'
        if keyPressed == pygame.K_6:
            self.ip += '6'
        if keyPressed == pygame.K_7:
            self.ip += '7'
        if keyPressed == pygame.K_8:
            self.ip += '8'
        if keyPressed == pygame.K_9:
            self.ip += '9'
        if keyPressed == pygame.K_BACKSPACE:
            self.ip = self.ip[:-1]
        if keyPressed == pygame.K_PERIOD:
            self.ip += '.'
        if keyPressed == pygame.K_SEMICOLON:
            self.ip += ':'
        self.IPItem = self.Font0.render(self.ip, True, (100,10,10))
     
    def blitme(self):
        self.screen.blit(self.ModeItem,self.ModeRect)
        if self.settings.multi_main:
            self.screen.blit(self.hostHintItem,self.hostHintRect)
            self.screen.blit(self.IPItem,self.IPRect)
        else:
            self.screen.blit(self.clientHintItem,self.clientHintRect)
            self.screen.blit(self.IPItem,self.IPRect)
        self.screen.blit(self.confirmItem,self.confirmRect)
        self.screen.blit(self.doneItem, self.doneRect)