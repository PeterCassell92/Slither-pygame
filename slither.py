import pygame
import random

pygame.init()

white= (255,255,255)
black= (0,0,0)
red = (255,0,0)
green = (0,155,0)
display_width = 800
display_height = 600
block_size =20
appleThickness = 30
img = pygame.image.load('Snakehead.png')
appleimg= pygame.image.load('Apple.png')

FPS = 10

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Slither')
pygame.display.update()
pygame.display.set_icon(img)

clock = pygame.time.Clock()

smallfont= pygame.font.SysFont(None, 25)
medfont= pygame.font.SysFont(None, 50)
largefont= pygame.font.SysFont(None, 80)

def gameIntro():
	intro = True
	while intro:
		gameDisplay.fill(white)
		message_to_screen("Welcome to Slither", green, -100, "large")
		message_to_screen("The objective of the game is to eat red apples", black, -30)
		message_to_screen("The more apples you eat, the longer you become", black, 10)
		message_to_screen("You will lose if you collide with yourself or the edges", black, 50)
		message_to_screen("Press C to Continue or Q to Quit", black, 150, "medium")

		for event in pygame.event.get():
				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_q:
						pygame.quit()
						quit()
					elif event.key == pygame.K_c:
						intro = False
				if event.type == pygame.QUIT :
					pygame.quit
					quit()



		pygame.display.update()
		clock.tick(5)
def pause():
	paused = True
	message_to_screen("Paused", black, -100, "large")
	message_to_screen("Press C to continue or Q to quit ", black, -30)
	pygame.display.update()
	while paused:
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_q:
					pygame.quit()
					quit()
				elif event.key == pygame.K_c:
					paused = False
			if event.type == pygame.QUIT :
				pygame.quit
				quit()

		#gameDisplay.fill(white)
		

		clock.tick(5)


def score(score):
	text = smallfont.render("Score: " + str(score), True, black)
	gameDisplay.blit(text, (0,0))

def apple(applex, appley):
	gameDisplay.blit(appleimg, (applex, appley))
	
	
def randAppleGen():
	randapple_y = round(random.randrange(0,display_height - appleThickness))
	randapple_x = round(random.randrange(0,display_width - appleThickness))
	return randapple_x, randapple_y

def snake(snakeList, block_size):

	if direction == 'right':
		head= pygame.transform.rotate(img, 270)
	if direction == 'left':
		head= pygame.transform.rotate(img, 90)
	if direction == 'up':
		head= pygame.transform.rotate(img, 0)
	if direction == 'down':
		head= pygame.transform.rotate(img, 180)

	gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))

	for XnY in snakeList[:-1] :
		pygame.draw.rect(gameDisplay,green,[XnY[0],XnY[1],block_size,block_size])

def text_Objects(text, color, size):
	if size == "small":
		textSurface = smallfont.render(text, True, color)
	elif size == "medium":
		textSurface = medfont.render(text, True, color)
	elif size == "large":
		textSurface = largefont.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message_to_screen(msg, color,y_displace =0, size = "small"):
	#screen_text = font.render(msg, True, color)
	#gameDisplay.blit(screen_text, [display_width/4, display_height/2])
	
	textSurf, textRect = text_Objects(msg, color, size)
	textRect.center = (display_width/2), (display_height/2) + y_displace
	gameDisplay.blit(textSurf,textRect)
	

def gameLoop():
	global direction
	global mode
	direction = 'right'
	gameExit= False
	gameOver= False
	snakeList = []
	snakeLength = 1
	growthperapple =1
	
	snakeSpeed = block_size

	
	lead_x = display_width/2
	lead_y = display_height/2
	lead_xchange= snakeSpeed
	lead_ychange= 0
	randapple_x, randapple_y = randAppleGen()
	#print randapple_x
	#print randapple_y
	while not gameExit:
		if gameOver == True:
			message_to_screen("Game Over", red, -100, "large")
			message_to_screen(" Press C to continue or Q to quit", black, 50, "medium")
			pygame.display.update()

		while gameOver == True:
			#gameDisplay.fill(white)			
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN :
					if event.key == pygame.K_q:
						gameOver = False
						gameExit = True
					elif event.key == pygame.K_c:
						gameLoop()
				if event.type == pygame.QUIT :
					gameOver = False
					gameExit = True



		for event in pygame.event.get():
			#print event
			if event.type == pygame.QUIT :
				gameExit = True
			if event.type == pygame.KEYDOWN :
				if event.key == pygame.K_RIGHT:
					lead_xchange = snakeSpeed
					lead_ychange = 0
					direction= 'right'
				if event.key == pygame.K_LEFT:
					lead_xchange = -snakeSpeed
					lead_ychange = 0
					direction= 'left'
				if event.key == pygame.K_DOWN:
					lead_ychange = snakeSpeed
					lead_xchange = 0
					direction= 'down'
				if event.key == pygame.K_UP:
					lead_ychange = -snakeSpeed
					lead_xchange = 0
					direction= 'up'
				if event.key == pygame.K_ESCAPE:
					pause()
		if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
			gameOver = True

		lead_x += lead_xchange
		lead_y += lead_ychange

		# if lead_x == randapple_x and lead_y == randapple_y:
		# 	randapple_x = round(random.randrange(0,display_width - block_size)/10.0)*10.0
		# 	randapple_y = round(randomrandrange(0, display_height - block_size)/10.0)*10.0
		# 	snakeLength += growthperapple
	
		#if lead_x >= randapple_x and lead_x < randapple_x + appleThickness:
		#	if lead_y >= randapple_y and lead_y < randapple_y + appleThickness or lead_y + block_size > randapple_y and lead_y + block_size < randapple_y + appleThickness:
		#		randapple_y = round(random.randrange(0,(display_height - appleThickness)/block_size))*10
		#		randapple_x = round(random.randrange(0,(display_width - appleThickness)/block_size))*10
				#print randapple_x
				#print randapple_y
		#		snakeLength += growthperapple

		if lead_x >= randapple_x and lead_x < randapple_x +appleThickness or lead_x + block_size > randapple_x and lead_x + block_size < randapple_x + appleThickness:
			#print "X crossover"
			if lead_y >= randapple_y and lead_y <randapple_y +appleThickness or lead_y + block_size > randapple_y and lead_y + block_size < randapple_y + appleThickness:
				randapple_x, randapple_y = randAppleGen()
				snakeLength += growthperapple
				#print lead_x
				#print lead_y
				#print "X & Y crossover"


		gameDisplay.fill(white)
		
		#pygame.draw.rect(gameDisplay, red, [randapple_x, randapple_y,appleThickness,appleThickness])

		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)

		if len(snakeList) >(snakeLength):
			del snakeList[0]

		for eachSegment in snakeList[:-1]:
			if eachSegment == snakeHead :
				gameOver = True

		apple(randapple_x,randapple_y)
		snake(snakeList, block_size)
		score((snakeLength-1)*10)
		#gameDisplay.fill(red, rect = [100,100,40,40]) example of fill to draw square/ rect

		pygame.display.update()
		clock.tick(FPS)
gameIntro()
gameLoop()

pygame.quit
quit()