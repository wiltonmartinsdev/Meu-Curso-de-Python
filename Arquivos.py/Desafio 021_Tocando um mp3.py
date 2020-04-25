# Faça um programa em Python que abra e reproduza o aúdio de um arquivo mp3.

from pygame import mixer
mixer.init()
mixer.music.load('capoeira.mp3')
input()


