# Faça um programa em Python que abra e reproduza o aúdio de um arquivo mp3.
'''
Outra forma: 

import pyglet
music = pyglet.resource.media('capoeira.mp3')

music.play()
'''

from pygame import mixer
mixer.init()
mixer.music.load('capoeira.mp3')
input()