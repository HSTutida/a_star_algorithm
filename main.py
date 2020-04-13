import pygame
from change_color import change
from calculate_cost import calculate
from smallest_green import smallest
from writeCost import write_cost
from is_neighbour import neighbour
from paint_y import paint_yellow
import time

# Initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((1000,1000))

# font for text
font = pygame.font.Font('freesansbold.ttf',16)
###########################################################
# Show the input value in position x,y
def show_cost(x,y,value):
	score = font.render(str(value),True,(0,0,0))
	screen.blit(score,(x,y))
############################################################

# Defines each space in the grid 
class space():
	def __init__(self,g_cost,h_cost,t_cost, color,x,y,index_x,index_y,path_flag):
		self.g_cost = g_cost # distance from starting node, plus 10 for each horizontal step, plus 14 for diagonal step
		self.h_cost = h_cost # distance from end node, plus 10 for each horizontal step, plus 14 for diagonal step
		self.t_cost = t_cost # g_cost + h_cost
		self.color = color # defines the sprite color
		self.x = x # position on the grid
		self.y = y # position on the grid
		self.index_x = index_x # index address of the square
		self.index_y = index_y # index address of the square
		self.path_flag = False # boolean to show if space must turn to path color
#############################################################
# Load the space colors

black = pygame.image.load('square_black.png')
white = pygame.image.load('square_white.png')
red = pygame.image.load('square_red.png')	
green = pygame.image.load('square_green.png')
blue = pygame.image.load('square_blue.png')	
yellow = pygame.image.load('square_yellow.png')	

space_list = [] # Save a list of all spaces
pos_x = 10 # Save the starting X position
pos_y= 10 # Save the starting Y position 
#############################################################
# Creates a list of squares instances, the start parameters is shown below
for i in range(10):
	for z in range (10):
		space_list.append(space(g_cost=0,h_cost=0,t_cost = 0,color=white,x=pos_x+95*i,y=pos_y+95*z,index_x=i,index_y=z,path_flag=False))
####################################################################


		

######################################################
# using to make loop only once
#once = True

# Keep track of all spaces that must change
list_change = []
# Turn red list
turn_red = []
# Coordinate index of origin and destiny
#o_x = 0
#o_y = 0
#d_x = 9
#d_y = 9
# Index of the destiny in the square_list[d_index]
#d_index = 10*d_x + d_y
### Start LOOP ###
# running value to be used to exit while loop
running = True



# Will continue choosing the black spaces until parameters is zero
parameters_phase = 5
ask = ''
while parameters_phase>0:
	
	# Draw all squares	
	for i in range(100):
		screen.blit(space_list[i].color, (space_list[i].x,space_list[i].y))

	for event in pygame.event.get():
		for event in pygame.event.get():
		# Exit if exit button is pressed on window
			if event.type == pygame.QUIT:
				pygame.quit()	

		if event.type == pygame.MOUSEBUTTONDOWN:	
			mx, my = pygame.mouse.get_pos()
	
			for i in range(100):
				# Distance between the click and the square
				distance = ((mx-(space_list[i].x+45))**2+(my-(space_list[i].y))**2)**0.5		
				if distance <=45:
					#print('Square[{}]'.format(i))
					# Turn the square nearest to black and draw it
					space_list[i].color = black
					screen.blit(space_list[i].color, (space_list[i].x,space_list[i].y))
					
					

					#pygame.display.update()
					parameters_phase -= 1


	pygame.display.update()

###############################33
# User select a space to be the origin (blue)
parameters_phase = 1

while parameters_phase>0:
	
	# Draw all squares	
	for i in range(100):
		screen.blit(space_list[i].color, (space_list[i].x,space_list[i].y))

	for event in pygame.event.get():
		for event in pygame.event.get():
		# Exit if exit button is pressed on window
			if event.type == pygame.QUIT:
				pygame.quit()	

		if event.type == pygame.MOUSEBUTTONDOWN:	
			mx, my = pygame.mouse.get_pos()
	
			for i in range(100):
				# Distance between the click and the square
				distance = ((mx-(space_list[i].x+45))**2+(my-(space_list[i].y))**2)**0.5		
				if distance <=45:
					#print('Square[{}]'.format(i))
					# Turn the square nearest to black and draw it
					space_list[i].color = blue
					screen.blit(space_list[i].color, (space_list[i].x,space_list[i].y))
					o_x = space_list[i].index_x
					o_y = space_list[i].index_y
					print('Ox defined: {}'.format(o_x))

					#pygame.display.update()
					parameters_phase -= 1


	pygame.display.update()
##########################################################################
# User select a space to be the destiny (yellow)
parameters_phase = 1

while parameters_phase>0:
	
	# Draw all squares	
	for i in range(100):
		screen.blit(space_list[i].color, (space_list[i].x,space_list[i].y))

	for event in pygame.event.get():
		for event in pygame.event.get():
		# Exit if exit button is pressed on window
			if event.type == pygame.QUIT:
				pygame.quit()	

		if event.type == pygame.MOUSEBUTTONDOWN:	
			mx, my = pygame.mouse.get_pos()
	
			for i in range(100):
				# Distance between the click and the square
				distance = ((mx-(space_list[i].x+45))**2+(my-(space_list[i].y))**2)**0.5		
				if distance <=45:
					#print('Square[{}]'.format(i))
					# Turn the square nearest to black and draw it
					space_list[i].color = yellow
					screen.blit(space_list[i].color, (space_list[i].x,space_list[i].y))
					#pygame.display.update()
					d_x = space_list[i].index_x
					d_y = space_list[i].index_y
					d_index = 10*d_x + d_y
					parameters_phase -= 1


	pygame.display.update()

##########################start finding path##############################
while running:

# Draw all squares	
	for i in range(100):
		screen.blit(space_list[i].color, (space_list[i].x,space_list[i].y))
		
	for event in pygame.event.get():
		# Exit if exit button is pressed on window
		if event.type == pygame.QUIT:	
			running = False

	#change(space_list,o_x,o_y , blue) # origin
	#change(space_list,d_x,d_y, yellow) # destiny
	'''		
	
	change(space_list,1,2 , black) # wall
	change(space_list,1,3 , black) # wall
	change(space_list,1,4 , black) # wall
	change(space_list,0,4,black)
	change(space_list,2,4 , black) # wall
	change(space_list,3,4 , black) # wall
	change(space_list,5,4 , black) # wall
	change(space_list,4,4 , black) # wall
	change(space_list,2,5 , black) # wall

	change(space_list,2,6 , black) # wall
	
	change(space_list,1,5 , black) # wall
	
	
	'''
	
	
		# change the color of the neighbours
	for i in range (100):
		if neighbour(space_list,i,red,blue):
			list_change.append(i)
			print('list of spaces that have neighbour: {}'.format(list_change))
	for i in list_change:
			if space_list[i].color != yellow and space_list[i].color != black and space_list[i].color != blue and space_list[i].color!=red: 			
				change(space_list,space_list[i].index_x,space_list[i].index_y,green)
	
	# write the costs
	for i in range(100):
		write_cost(space_list,i,o_x,o_y,d_x,d_y,green) # x1,y1,x2,y2 is the origin and destiny 

	
	# show the cost in each space
	for i in range(100):
			space_list[i].t_cost = space_list[i].h_cost + space_list[i].g_cost 
			#print('cost shown: {}'.format(space_list[i].t_cost))
			show_cost(space_list[i].x,space_list[i].y,space_list[i].t_cost)
	
	
	#Turn red the smallest green space
	smallest(space_list,green,red)		

	# When arrive the destiny paint the path in yellow
	#x = ''
	#time.sleep(1)
	if neighbour(space_list,d_index,red,red):
		space_list[d_index].path_flag = True
		running = False
		#x = input('wainting for input')
		
	pygame.display.update()
####################################################################
#start painting yellow spaces
running = True
while running:

	for i in range(100):
		screen.blit(space_list[i].color, (space_list[i].x,space_list[i].y))
		
	for event in pygame.event.get():
		# Exit if exit button is pressed on window
		if event.type == pygame.QUIT:	
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			mx, my = pygame.mouse.get_pos()		
			print('x = {}, y = {}'.format(mx,my))	

	
	a = paint_yellow(space_list,yellow,red,blue)
	
	time.sleep(1)
	# show the cost in each space
	for i in range(100):
			space_list[i].t_cost = space_list[i].h_cost + space_list[i].g_cost 
			#print('cost shown: {}'.format(space_list[i].t_cost))
			show_cost(space_list[i].x,space_list[i].y,space_list[i].t_cost)
			show_cost(space_list[i].x+40,space_list[i].y,space_list[i].h_cost)
			show_cost(space_list[i].x,space_list[i].y+40,space_list[i].g_cost)
	


	pygame.display.update()




pygame.quit()
quit()