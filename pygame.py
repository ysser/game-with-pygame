import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
#color
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)


bright_red = (255,0,0)
bright_green = (0,255,0)


block_color = (53,115.255)

car_width = 73




#height of the interface and its width
gameDisplay = pygame.display.set_mode((display_width,display_height))

#the type of the game
pygame.display.set_caption('A bit Racey')

#the function of time
clock = pygame.time.clock()

#create your player from an image
carImg = paygame.image.load('racecar.png')

#count haw many things u dodged
def things-dodged(count):
	font = pygame.font.SysFont(None,25)
	text = font.render ("Dodged: "+str(count),True, black)
	gameDisplay.blit(text,(0,0))


#define things
def things(thingx,thingy,thingw,thingh,color):
	pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])	

#player location
def car (x,y):
	gamedisplay.blit(carImg,(x,y))

def text_objects(text,fint):
	textSurface = font.render(text,True, black)
	return textSurface.get_rect()

def message_display(text):
	largeText = pygame.font.Font('freesansbold.ttf',115)
	TextSurf, TextRect = text_objects (text, largeText)
	TextRect.center = ((display_width/2),(display_height/2))	
	game display.blit(TextSurf,TextRect)

	pygame.display.update()

	time.sleep(2)

	game_loop()

#define function crash
def crash():
	message_display('you Crashed')

#the intro duction befor the beguining of the game	
def game_intro():

	intro = True
	while intro:
		for event in pygame.event.get():
			pygame.quit()
		quit()

	gameDisplay.fill(white)
	largeText = pygame.font.Font('freesansbild.ttf',115)
	TextSurf, TextRect = text_objects ("A bit Racey", largeText)
	TextRect.center = ((display_width/2),(display_height/2))	
	game display.blit(TextSurf,TextRect)


mouse = pygame.mouse.get_pos()

#print(mouse)

if 	150+100 > mouse [0] > 150 and 450+50 > mouse [1] > 450:
	pygame.draw.rect(gameDisplay,bright_green,(150,450,100,50))
else:
	pygame.draw.rect(gameDisplay,red,(550,450,100,50))
	pygame.draw.rect(gameDisplay,red,(550,450,100,50))

pygame.display.update()
clock.tick(15)

defgame_loop():

x = (display_width * 0.45)
y = (display_height * 0.8)

x_change =0 

thing_startx = random.randrange(0,display_width)
thing_starty = -600
thing_speed = 4
thing_width = 100
thing-height = 100

thingCount = 1

dodged = 0


#the end or the continue of the game
gameExit = False

while not gameExit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

#condition in mouvement of your player
			if event.type == pygame.KEYDOWN:
			if event.key == pygame.k_LEFT:
				x_change = -5
			elif event.key == pygame.k_RIGHT:
				x_change = 5
			if event.type == pygame.KEYUP:
				if event.key == pygame.k_LEFT or event.key == pygame.k_RIGHT:
					x_change = 0
					x+=x_change

		gameDisplay.fill(white)


		things(thing_startx,thing_starty,thing_width,thing_height,block_color)

		thing_starty += thing_speed

		car (x,y)
		things_dodged(dodged)
		 
#show the event of the end

if x > display_width - car_width or x<0:
crash()



if thing_starty > display_height:
	thing_starty = 0 - thing_height
	thing-startx = random.randrange(0,display_width)

	dodged += 1
	thing_speed += 1
	thing_width += (dodged * 1.2)



#condition of the colition of the extrimit in y
if y < thing_starty+thing_height:
	print('y crossover')	





#candition of the colition of the extrimity of the thing in x
if x < thing_startx and x < thing_statx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx + thing_width
	print('xcrossover')
	crash()

			
#update the surface in 60s
	pygame.display.update()
	
	clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()