'''
Created on Dec 23, 2018

@author: qiangkejia
'''

import pygame as py
from settings import Settings
import gameFunctions as gf
from menu import Menu
from game import Game
from multi import Multi
from gameFunctions import check_events_menu

def run():
    '''Start Running'''
    menu = Menu(settings,screen)
    gf.update_menu_screen(settings, screen, menu)
    while gf.check_events_menu(settings,screen,menu):
        gf.update_menu_screen(settings, screen, menu)
        if menu.result == "Start":
            game = Game(settings, screen)
            gf.update_game_screen(settings,screen,game)
            if settings.multiplay and not settings.multi_main:
                for event in py.event.get():
                    pass
                game.webActions(10,10)
                gf.update_game_screen(settings,screen,game)
            while True:
                if not gf.check_events_game(settings, screen, game): break
                gf.update_game_screen(settings,screen,game)
                for event in py.event.get():
                    pass
                if settings.multiplay:
                    game.webActions(game.tempx, game.tempy)
                for event in py.event.get():
                    pass
                gf.update_game_screen(settings,screen,game)
            break
        elif menu.result == "Multi":
            multi = Multi(settings, screen)
            gf.update_multi_screen(settings, screen, multi)
            while gf.check_events_multi(settings, screen, multi):
                gf.update_multi_screen(settings, screen, multi)
            break

if __name__ == '__main__':
    #Initialize Pygame
    py.init()
    py.display.set_caption("Othello")
    settings = Settings()
    screen = py.display.set_mode((800,600))
    while True:
        run()