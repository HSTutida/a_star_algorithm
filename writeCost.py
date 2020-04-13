from calculate_cost import calculate

# receives the position of origin and destiny
# and writes the cost
def write_cost(space_list,i,x1,y1,x2,y2,green):
	neighbours = []
	
	# Set all the costs on neighbours to the origin or neighbour to green cells
	for z in range(100):
		if space_list[z].color == green:
			space_list[z].g_cost = calculate(space_list[z].index_x,space_list[z].index_y,x1,y1)
			print('x1 = {}, y1 = {}'.format(x1,y1))
			space_list[z].h_cost = calculate(space_list[z].index_x,space_list[z].index_y,x2,y2)
			print('x2 = {}, y2 = {}'.format(x2,y2))	
