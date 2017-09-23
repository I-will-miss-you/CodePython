#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
import pygame as mixer, time

mixer.init()
mixer.music.load('Amy.mp3')
mixer.music.play()

while mixer.music.get_busy():
    time.Clock().tick(10)
'''
'''
from pygame import mixer
mixer.init()
mixer.music.load('amy.mp3')
mixer.music.play()
while True:
    mixer.music.get_busy()
'''

from pygame import mixer
mixer.init()
son=mixer.music
son.load('{}.mp3'.format(input('Digite o nome da Musica no diretorio: ')))
while True:
    menu=input('''
    [MENU]
    1: Tocar
    2: Pause
    3: Continue
    4: Parar
    5: Sair
    ''')
    if menu=='1':
        son.play()
    elif menu=='2':
        son.pause()
    elif menu=='3':
        son.unpause()
    elif menu=='4':
        son.stop()
    elif menu=='5':
        son.stop()
        break