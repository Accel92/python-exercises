#!/usr/bin/python

import pygame, sys
from time import time
from pygame.locals import *

pygame.init()

FPS = 30	  # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Animation")

WHITE = (255, 255, 255)

# basePath = os.path.dirname(__file__)
# catPath = os.path.join(basePath, "cat.png")
# catImg = pygame.image.load(catPath)

# soundObj = pygame.mixer.Sound('beeping.wav')	for WAV, OGG formats
pygame.mixer.music.load('smoke.mp3')		#for mp3 formats
catImg = pygame.image.load('cat.png')

catx = 10
caty = 10
direction = "right"


#soundObj.play()
pygame.mixer.music.play(0, 55.0)
musicStart = time()
while True:		# the main game loop
	DISPLAYSURF.fill(WHITE)

	if direction == "right":
		catx += 10
		if catx == 280:
			direction = "down"
	elif direction == "down":
		caty += 10
		if caty == 220:
			direction = "left"
	elif direction == "left":
		catx -= 10
		if catx == 10:
			direction = "up"
	elif direction == "up":
		caty -= 10
		if caty == 10:
			direction = "right"
		
	DISPLAYSURF.blit(catImg, (catx, caty))

	musicEnd = time()
	if musicEnd - musicStart >= 5:
		pygame.mixer.music.stop()
		musicStart = time()
		pygame.mixer.music.play(0, 55.0)

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fpsClock.tick(FPS)
