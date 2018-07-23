import sys, time
import pygame
from pygame.locals import *
from random import randint

def draw_grid():
	for i in range(horizontal_cells):
		pygame.draw.line(screen, grey, (i*cell_size, 0), (i*cell_size, screen_height))
	for j in range(vertical_cells):
		pygame.draw.line(screen, grey, (0, j*cell_size), (screen_width, j*cell_size))

def near_alive_cells(x, array):
	i = 0
	near_cells = [[x[0]-1, x[1]-1],[x[0], x[1]-1],[x[0]+1, x[1]-1],[x[0]-1, x[1]],[x[0]+1, x[1]],[x[0]-1, x[1]+1],[x[0], x[1]+1],[x[0]+1, x[1]+1]]
	for near_cell in near_cells:
		if near_cell in array:
			i += 1
		else:
			pass
	return i


FPS = 10

#colors
white = [255, 255, 255]
black = [0, 0, 0]
grey = [128, 128, 128]
purple = [75, 0, 130]
light_grey = [220, 220, 220]
dark_red = [102, 0, 0]

screen_width = 700
screen_height = 700

#NUMBER OF CELLS ON X AND Y AXES
horizontal_cells = 50
vertical_cells = 50


cell_size = screen_width/horizontal_cells

total_cells = horizontal_cells * vertical_cells
last = total_cells - 1 


all_cells = []

clicked_cells= []



gosper_cannon = [[2, 8], [3, 8], [3, 9], [2, 9], [12, 9], [12, 8], [12, 10], [13, 11], [14, 12], [15, 12], [17, 11], [18, 10], [18, 9], [18, 8], [19, 9], [17, 7], [16, 9], [15, 6], [14, 6], [13, 7], [22, 8], [23, 8], [22, 7], [23, 7], [23, 6], [22, 6], [24, 5], [24, 9], [26, 5], [26, 4], [26, 9], [26, 10], [36, 7], [37, 7], [37, 6], [36, 6]]
pulsar = [[12, 10], [13, 10], [14, 10], [18, 10], [19, 10], [20, 10], [15, 12], [15, 13], [15, 14], [17, 12], [17, 13], [17, 14], [18, 15], [19, 15], [20, 15], [14, 15], [13, 15], [12, 15], [22, 14], [22, 13], [22, 12], [10, 14], [10, 13], [10, 12], [12, 17], [13, 17], [14, 17], [18, 17], [19, 17], [20, 17], [22, 18], [22, 19], [22, 20], [10, 18], [10, 19], [10, 20], [15, 18], [15, 19], [15, 20], [17, 18], [17, 19], [17, 20], [18, 22], [19, 22], [20, 22], [14, 22], [13, 22], [12, 22]]
pentadecathlon = [[14, 23], [15, 23], [16, 23], [17, 23], [18, 23], [19, 23], [20, 23], [21, 23], [22, 23], [23, 23]]
blinker = [[23, 20], [23, 21], [23, 22]]
toad = [[22, 21], [23, 21], [24, 21], [23, 22], [22, 22], [21, 22]]
r_pentomino = [[24, 19], [25, 19], [24, 20], [23, 20], [24, 21]]
die_hard = [[15, 19], [16, 19], [16, 20], [20, 20], [21, 20], [22, 20], [21, 18]]
acorn = [[15, 26], [16, 26], [16, 24], [18, 25], [19, 26], [21, 26], [20, 26]]
glider = [[22, 19], [23, 20], [23, 21], [22, 21], [21, 21]]
lwss = [[4, 14], [4, 15], [5, 15], [5, 14], [5, 16], [6, 16], [6, 15], [7, 15], [7, 14], [8, 14], [7, 13], [6, 13]]
block = [[22, 20], [23, 20], [23, 21], [22, 21]]
beehive = [[22,20], [23,20], [24,21], [23,22], [22,22], [21,21]]
loaf = [[22,20], [23,20], [24,21], [24,22], [23,23], [22,22], [21,21]]
boat = [[22,20], [23,20], [24,21], [23,22],[22,21]]
tub = [[22,20], [23,21], [22,22], [21,21]]




for cell in range(total_cells):
	cell_x = int(cell/horizontal_cells)
	cell_y = int(cell%horizontal_cells)
	all_cells.append([cell_x, cell_y])

main = True
menu1 = True 
randomCells = False
menu2_2 = False
menu3_1 = False
menu3_2 = False
menu3_3 = False
menu3_4 = False
user_input = False
running = False
start = False

pygame.init()

startNumber = 0
titleFont = pygame.font.Font(None, 60)
menuFont = pygame.font.Font(None, 40)
menuFont1 = pygame.font.Font(None, 30)
menuFont2 = pygame.font.Font(None, 20)
generationFont = pygame.font.Font(None, 30)
referenceFont = pygame.font.Font(None, 20)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Conway's Game of Life")
fps = pygame.time.Clock()


previous_generation = []


while  main:

	while menu1:

		screen.fill(light_grey)

		titleText = titleFont.render("Conway's Game of Life Simulator", 2, dark_red)
		option1Text = menuFont.render("1.Random", 1, purple)
		option2Text = menuFont.render("2. Classic Configurations", 1, purple)
		option3Text = menuFont.render("Select Initial Configuration of Alive Cells", 1, purple)
		option4Text = menuFont1.render("Type the number corresponding to the option you want to select", 1, dark_red)
		option6Text = menuFont.render("3.Select alive cells by clicking", 1, purple)
		option6_1Text = menuFont.render("on them",1,purple)

		text_rect = titleText.get_rect(center = (350, 50))
		initialM_rect = option3Text.get_rect(center = (350, 150))
		option4rect = option4Text.get_rect(center = (350, 200))
		screen.blit(titleText, text_rect)
		screen.blit(option1Text, (200, 300))
		screen.blit(option2Text, (200, 400))
		screen.blit(option3Text, initialM_rect)
		screen.blit(option4Text, option4rect)
		screen.blit(option6Text, (200, 500))
		screen.blit(option6_1Text, (205, 550))
		#screen.blit(option5Text, (350, 450))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_1:
					menu1 = False
					randomCells = True
				elif event.key == K_2:
					menu1 = False
					menu2_2 = True
				elif event.key == K_3:
					menu1 = False
					user_input = True
				elif event.key == K_ESCAPE:
					sys.exit()


		pygame.display.update()




	while randomCells:

		
		
		screen.fill(light_grey)

		RandomText = menuFont.render("Select the number of starting living cells", 1, purple)
		RandomText1 = menuFont1.render("1. 10", 1, purple)
		RandomText2 = menuFont1.render("2. 50", 1, purple)
		RandomText3 = menuFont1.render("3.100", 1, purple)
		RandomText4 = menuFont1.render("4.150",1, purple)
		RandomText5 = menuFont1.render("5.300",1, purple) 

		screen.blit(RandomText, (100,100))
		screen.blit(RandomText1, (200,200))
		screen.blit(RandomText2, (200,300))
		screen.blit(RandomText3, (200,400))
		screen.blit(RandomText4, (200,500))
		screen.blit(RandomText5, (200,600))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_ESCAPE:
						sys.exit()

				elif event.key == K_b:
					randomCells = False
					menu1 = True
				elif event.key == K_1:
					startNumber = 10
					previous_generation = alive_cells
					randomCells = False
					running = True

				elif event.key == K_2:
					startNumber = 50
					previous_generation = alive_cells
					randomCells = False
					running = True

				elif event.key == K_3:
					startNumber = 100
					previous_generation = alive_cells
					randomCells = False
					running = True

				elif event.key == K_4:
					startNumber = 150
					previous_generation = alive_cells
					randomCells = False
					running = True

				elif event.key == K_5:
					startNumber ==  300
					previous_generation = alive_cells
					randomCells = False
					running = True


				elif event.key == K_RETURN:
					if startNumber == 0:
						startNumber = 150
					previous_generation = alive_cells
					randomCells = False
					running = True


		alive_cells = []

		for i in range(150):
			x = randint(0, last)
			alive_cells.append(all_cells[x])


		pygame.display.update()

		

	while menu2_2:

		screen.fill(light_grey)


		option2_1Text = menuFont.render("1.Still Lives", 1, purple)
		option2_2Text = menuFont.render("2.Oscillators", 1, purple)
		option2_3Text = menuFont.render("3.Spaceships", 1, purple)
		option2_4Text = menuFont.render("4.Methuselah", 1, purple)
		option2_5Text = menuFont.render("5.Gosper Cannon", 1, purple)
		backText = menuFont1.render("Press b to go back", 1, dark_red)

		screen.blit(backText, (20, 650))
		screen.blit(titleText, text_rect)
		screen.blit(option2_1Text, (200, 200))
		screen.blit(option2_2Text, (200, 300))
		screen.blit(option2_3Text, (200, 400))
		screen.blit(option2_4Text, (200, 500))
		screen.blit(option2_5Text, (200, 600))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_1:
					menu2_2 = False
					menu3_1 = True
				elif event.key == K_2:
					menu2_2 = False
					menu3_2 = True
				elif event.key == K_3:
					menu2_2 = False
					menu3_3 = True
				elif event.key == K_4:
					menu2_2 = False
					menu3_4 = True
				elif event.key == K_5:
					menu2_2 = False
					previous_generation = gosper_cannon
					running = True
				elif event.key == K_b:
					menu2_2 = False
					menu1 = True
				elif event.key == K_ESCAPE:
					sys.exit()

		pygame.display.update()


	while menu3_1:

		screen.fill(light_grey)

		tubText = menuFont.render("1.Tub",1, purple)
		blockText = menuFont.render("2. Block",1, purple)
		beeaiveText = menuFont.render("3.Beehive",1, purple)
		loafText = menuFont.render("4.Loaf",1, purple)
		boatText = menuFont.render("5.Boat",1, purple)
		backText = menuFont1.render("Press b to go back", 1, dark_red)

		screen.blit(backText, (20, 650))
		screen.blit(tubText, (200, 200))
		screen.blit(blockText, (200, 300))
		screen.blit(beeaiveText, (200, 400))
		screen.blit(loafText, (200, 500))
		screen.blit(boatText, (200, 600))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_1:
					menu3_1 = False
					previous_generation = tub
					running = True
				elif event.key == K_2:
					menu3_1 = False
					previous_generation = block
					running = True
				elif event.key == K_3:
					menu3_1 = False
					previous_generation = beehive
					running = True
				elif event.key == K_4:
					menu3_1 = False
					previous_generation = loaf
					running = True
				elif event.key == K_5:
					menu3_1 = False
					previous_generation = boat
					running = True
				elif event.key == K_b:
					menu3_1 = False
					menu2_2 = True
				elif event.key == K_ESCAPE:
					sys.exit()

		pygame.display.update()

	while menu3_2:

		screen.fill(light_grey)

		pulsarText = menuFont.render("1.Pulsar",1, purple)
		blinkerText = menuFont.render("2.Blinker",1, purple)
		pentaText = menuFont.render("3.Pentadecathlon",1, purple)
		backText = menuFont1.render("Press b to go back", 1, dark_red)

		screen.blit(backText, (20, 650))
		screen.blit(pulsarText, (200, 200))
		screen.blit(blinkerText, (200, 300))
		screen.blit(pentaText, (200, 400))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_1:
					menu3_2 = False
					previous_generation = pulsar
					running = True
				elif event.key== K_2:
					menu3_2 = False
					previous_generation = blinker
					running = True
				elif event.key == K_3:
					menu3_2 =False
					previous_generation = pentadecathlon
					running = True
				elif event.key == K_b:
					menu3_2 = False
					menu2_2 = True
				elif event.key == K_ESCAPE:
					sys.exit()


		pygame.display.update()

	while menu3_3:

		screen.fill(light_grey)

		gliderText = menuFont.render("1.Glider",1, purple)
		lwssText = menuFont.render("2.Light Weight Spaceship",1, purple)
		backText = menuFont1.render("Press b to go back", 1, dark_red)

		screen.blit(backText, (20, 650))
		screen.blit(gliderText, (200, 300))
		screen.blit(lwssText, (200, 400))


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_1:
					menu3_3 = False
					previous_generation = glider
					running = True
				elif event.key== K_2:
					menu3_3 = False
					previous_generation = lwss
					running = True
				elif event.key == K_b:
					menu3_3 = False
					menu2_2 = True
				elif event.key == K_ESCAPE:
					sys.exit()

		pygame.display.update()

	while menu3_4:

		screen.fill(light_grey)

		dieHardText = menuFont.render("1.Die Hard",1, purple)
		acornText = menuFont.render("2.Acorn",1, purple)
		rpText = menuFont.render("3.The R-pentomino",1, purple)
		backText = menuFont1.render("Press b to go back", 1, dark_red)
		
		screen.blit(backText, (20, 650))
		screen.blit(dieHardText, (200, 200))
		screen.blit(acornText, (200, 300))
		screen.blit(rpText, (200, 400))



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == KEYDOWN:
				if event.key == K_1:
					menu3_4 = False
					previous_generation = die_hard
					running = True
				elif event.key== K_2:
					menu3_4 = False
					previous_generation = acorn
					running = True
				elif event.key == K_3:
					menu3_4 = False
					previous_generation = r_pentomino
					running = True
				elif event.key == K_b:
					menu3_4 = False
					menu1 = True
				elif event.key == K_ESCAPE:
					sys.exit()

		pygame.display.update()




	while user_input:

		screen.fill(light_grey)

		backText = menuFont1.render("Press b to go back", 1, black)
		clearText = menuFont1.render("Press c to clear all",1, black)
		returnText = menuFont1.render("Press ENTER to start the simulation",1, black)

		screen.blit(backText, (20, 20))
		screen.blit(clearText, (20, 50))
		screen.blit(returnText, (20, 80))

		draw_grid()

		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit()
				elif event.key == K_RETURN:
					running= True
					user_input = False
					previous_generation = clicked_cells
				elif event.key == K_b:
					user_input = False
					menu1 = True
				elif event.key == K_c:
					clicked_cells = []
			elif event.type == MOUSEBUTTONDOWN:
				mouseCoor = pygame.mouse.get_pos() 
				cell_Selected_x = mouseCoor[0]/cell_size
				cell_Selected_y = mouseCoor[1]/cell_size
				cell_Selected = [cell_Selected_x, cell_Selected_y]
				if cell_Selected in clicked_cells:
					clicked_cells.remove(cell_Selected)
				else:
					clicked_cells.append(cell_Selected)
			elif event.type == pygame.QUIT:
				sys.exit()


		for clicked_cell in clicked_cells:
			rect = pygame.Rect(clicked_cell[0]*cell_size, clicked_cell[1]*cell_size, cell_size, cell_size)
			pygame.draw.rect(screen, purple, rect)

		pygame.display.update()

	next_generation = []


	generation = 0

	pgeneration = previous_generation
	time_passed = 0

	while running:

		start_time = time.time()
		
		next_generation = []

		screen.fill(light_grey)

		backText = menuFont1.render("Press b to go back to menu", 2, black)
		restartText = menuFont1.render("Press r to restart the simulation", 2, black)
		generationText = menuFont1.render("Generation: {}".format(generation), 1, black)
		aliveCellsText = menuFont1.render("Alive Cells: {}".format(len(previous_generation)), 1, black)
		dtText = menuFont1.render("Previous Generation life: {} s".format(time_passed),1, black)
		
		screen.blit(backText, (20, 50))
		screen.blit(restartText, (20, 20))
		screen.blit(generationText, (530, 20))
		screen.blit(aliveCellsText, (530, 40))
		screen.blit(dtText, (20, 660))

		draw_grid()

		for event in pygame.event.get():
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					sys.exit()
				elif event.key == K_b:
					running = False
					menu1 = True
				elif event.key == K_r:
					previous_generation = pgeneration
					generation = 0
			elif event.type == pygame.QUIT:
				sys.exit()

		for cell in all_cells:
			x = near_alive_cells(cell, previous_generation)
			if cell in previous_generation:
				if x == 2 or x == 3:
					next_generation.append(cell)
			else:
				if x == 3:
					next_generation.append(cell)

		for cell in next_generation:
			rect = pygame.Rect(cell[0] * cell_size, cell[1] * cell_size, cell_size, cell_size)
			pygame.draw.rect(screen, purple, rect)

		previous_generation = next_generation

		generation += 1

		time_passed = time.time() - start_time

		
		pygame.display.update()
		fps.tick(FPS)



