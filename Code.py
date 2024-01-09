import pygame
from pygame.locals import *
import random
import sys
import math
import subprocess 
pygame.init() 

class DoodleJump:
	def __init__(self):
		"""The initialization method."""
		# setup
		self.width = 530
		self.height = 700
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.caption = pygame.display.set_caption("Doodle Jump by Gautam and Charlotte")
		self.font = pygame.font.SysFont("Arial", 45, bold=True)
		self.num_platforms = 8
		# images
		self.home = pygame.image.load("assets/home.png").convert_alpha()
		self.gameover = pygame.image.load("assets/gameover.png").convert_alpha()
		self.background = pygame.image.load("assets/doodlebackground.png").convert_alpha()
		self.platformimage = pygame.image.load("assets/platform.png")
		self.playerimage = pygame.image.load("assets/player.png").convert_alpha()
		self.icon = pygame.display.set_icon(pygame.image.load("assets/icon.png").convert_alpha())
		# starting positions
		self.score = 0
		self.player_x = 250
		self.player_y = -100 # the negative gives the player some time to fall down at the start of the game
		self.change = 0 
		self.platform_x = []
		self.platform_y = []

	def platform(self): 
		"""Generates and displays random platforms that move."""
		for i in range(self.num_platforms): # adds platforms
			self.platform_x.append(random.randint(-1000, 0)) # the negative and large range helps greater randomization of platforms
			self.platform_y.append(random.randint(70, 650))
		for i in range(self.num_platforms): # creates a new platform once one has gone off of the screen
			self.screen.blit(self.platformimage, (self.platform_x[i],self.platform_y[i]))
			self.platform_x[i] += 1
			if self.platform_x[i] > 530:
				self.platform_x[i] = random.randint(-1000, 0)
				self.platform_y[i] = random.randint(70, 650)

	def movement(self): 
		"""Controls the player's movement and serves as a border check if the player moves too far left, right, or bottom."""
		self.player_y += 1.5
		for event in pygame.event.get():
			# exit
			if event.type==pygame.QUIT:
					sys.exit()
			# x movement
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RIGHT:
					self.change += 2
				if event.key==pygame.K_LEFT:
					self.change -= 2
			# no x movement
			if event.type==pygame.KEYUP:
				self.change = 0
			# border check
			if self.player_x < -50:             
				self.player_x = 515
			if self.player_x > 515:
				self.player_x = -50
		# game over
		if self.player_y > 700:
			self.screen.blit(self.gameover, (0, 0))
			result = self.font.render('score: ' + str(self.score), True, (0, 0, 0))
			self.screen.blit(result, (180, 230))
			pygame.display.update()
			DoodleJump().restart()
		self.player_x += self.change

	def collision(self):
		"""Determines if the player and the platform come in contact with one another"""
		for i in range(self.num_platforms):
			distance = math.sqrt((math.pow(self.player_x - self.platform_x[i], 2) + math.pow(self.player_y - self.platform_y[i], 2)))
			if distance < 80: 
				return True
		return False

	def changescore(self): 
		"""Allows the player to jump and updates the score"""
		if self.collision():
			self.player_y -= 200
			self.score += 3
	
	def run(self):
		"""
		This function runs the program through calling all the previous functions.
		Moreover, it controls the mouse interactions on the home screen.
		Note that "sys.exit()" was called three times in this class, which is necessary to accommodate for all three screens.
		"""
		clock = pygame.time.Clock()
		start = False
		while start == False:
			self.screen.blit(self.home,(0,0))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
						sys.exit()
				mouse = pygame.mouse.get_pos()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if 140 < mouse[0] < 330 and 320 < mouse[1] < 380:
						subprocess.Popen(["README.pdf"],shell=True)
					if 90 < mouse[0] < 280 and 210 < mouse[1] < 280:
						start = True # runs the program
		while start: 
			clock.tick(100) # ensures smoother movement
			self.screen.blit(self.background,(0,0))
			self.screen.blit(self.playerimage,(self.player_x,self.player_y))
			self.platform()
			self.movement()
			self.collision()
			self.changescore()
			text1 = self.font.render(str(self.score), True, (0, 0, 0))
			self.screen.blit(text1, (10,0))
			pygame.display.update()

			
	def restart(self):
		"""Restarts the program if the player decides to play again."""
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			mouse = pygame.mouse.get_pos()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if 160 < mouse[0] < 350 and 320 < mouse[1] < 380:
					DoodleJump().run()
					
DoodleJump().run()

