# Faça um programa que abra e reproduza o áudio de um arquivo mp3
import pygame
pygame.init()
pygame.mixer.music.load('<music_path>')
pygame.mixer.music.play()
pygame.event.wait()