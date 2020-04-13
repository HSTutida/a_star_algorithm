# With the coordinate values, change
# the color of the space
def change (space_list, x,y,color):
	# Look for all the values next	
	for i in range(100):
		if space_list[i].index_x == x and space_list[i].index_y == y:
				space_list[i].color = color
