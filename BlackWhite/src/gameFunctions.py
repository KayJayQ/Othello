'''
Created on Dec 23, 2018

@author: qiangkejia
'''
import pygame as py

def update_menu_screen(settings, screen, menu):
    screen.fill((128,128,128))
    menu.blitme()
    py.display.flip()

def update_game_screen(settings, screen, game):
    screen.fill((128,128,128))
    game.blitme()
    py.display.flip()

def update_multi_screen(settings, screen, multi):
    screen.fill((128,128,128))
    multi.blitme()
    py.display.flip()

def check_events_menu(settings,screen,menu):
    '''Respond to keypress and mouse events'''
    MadeSelection = False
    while not MadeSelection:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            elif event.type == py.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = py.mouse.get_pos()
                MadeSelection = menu.mouse_event(mouse_x,mouse_y)
    result = menu.result
    return result

def check_events_game(settings,screen,game):
    '''Respond to keypress and mouse events'''
    MadeSelection = False
    while not MadeSelection:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    return False
            elif event.type == py.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = py.mouse.get_pos()
                game.mouse_event(mouse_x,mouse_y)
                MadeSelection = True
    return True

def check_events_multi(settings, screen, multi):
    MadeSelection = False
    while not MadeSelection:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                quit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    return False
                multi.key_event(event.key)
                MadeSelection = True
            elif event.type == py.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = py.mouse.get_pos()
                multi.mouse_event(mouse_x,mouse_y)
                MadeSelection = True
    return True