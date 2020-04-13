import pygame
from change_color import change

def start_condition(square_list,o_x,o_y,d_x,d_y,black,blue,yellow,pygame.event):
	# Ask user the size of wall.
	size = 0
	size = int(input('Digit the number of wall spaces: '))

	# Position the wall painting in black

	while size>0:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:	
				mx, my = pygame.mouse.get_pos()
		
				for i in range(100):
					# Distance between the click and the square
					distance = ((mx-space_list[i].x)**2+(my-space_list[i].y)**2)**0.5		
					if distance <=250:
						#print('Square[{}]'.format(i))
						# Turn the square nearest to black and draw it
						space_list[i].color = black
						screen.blit(space_list[i].icon, (space_list[i].x,space_list[i].y))
						size -= 1





	# Position the origin 

	# Position the destiny
