'''
Created on Dec 23, 2018

@author: qiangkejia
'''
import socket

class Settings:
    
    downed = False
    
    screen_width = 800
    screen_height = 600
    multiplay = False
    
    multi_main = True
    server_ip = ''
    server_conn = None
    server_port = 0
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    