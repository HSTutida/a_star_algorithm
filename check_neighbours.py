from calculate_cost import calculate

# check for the cost of neighbours and return a list of the
# index of smallest ones
# receives the position of origin and destiny
def smallest(space_list,i,x1,y1,x2,y2):
	neighbours = []
	
	# Set all the costs on neighbours to the origin or neighbour to green cells
	for z in range(100):
		if space_list[z].color == green:
			space_list[z].g_cost = calculate(space_list[z].index_x,space_list[z].index_y,x1,y1)
			space_list[z].h_cost = calculate(space_list[z].index_x,space_list[z].index_y,x2,y2)

	# Append to the neighbours list in the format
	# [(index,cost)]


	# Change the color only for the smallest ones