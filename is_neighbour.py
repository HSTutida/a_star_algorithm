# Return True if found a neighbour red or blue
def neighbour(space_list,i,red,blue):
	found_neighbour = True # save when found  neighbour
	
	try:
		if space_list[i-11].color == red or space_list[i-11].color == blue:
			return found_neighbour
	except IndexError:
		print('IdexError')		
	try:
		if space_list[i-10].color == red or space_list[i-10].color == blue:
			return found_neighbour
	except IndexError:
		print('IdexError')		
	try:
		if space_list[i-9].color == red or space_list[i-9].color == blue:
			return found_neighbour
	except IndexError:
		print('IdexError')		
	try:
		if space_list[i-1].color == red or space_list[i-1].color == blue:
			return found_neighbour
	except IndexError:
		print('IdexError')		
	try:
		if space_list[i+1].color == red or space_list[i+1].color == blue:
			return found_neighbour
	except IndexError:
		print('IdexError')		
	try:
		if space_list[i+9].color == red or space_list[i+9].color == blue:
			return found_neighbour
	except IndexError:
		print('IdexError')		
	try:
		if space_list[i+10].color == red or space_list[i+10].color == blue:
			return found_neighbour
	except IndexError:
		print('IdexError')		
	try:
		if space_list[i+11].color == red or space_list[i+11].color == blue:
			return found_neighbour
	except IndexError:
		print('IdexError')		
	
	
	return False	
