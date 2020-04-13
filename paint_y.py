from is_neighbour import neighbour


# To paint in yellow all red and adjacent to yellow

def paint_yellow(space_list,yellow,red,blue):
	cost_list=[]
	index_list = []
	for i in range(100):
		if 	space_list[i].path_flag == True: 
			# check all the costs of red neighbours and paint the smallest
			# make a list of costs of all red neighbours
			space_list[i].path_flag = False
			
			if neighbour(space_list,i,blue,blue):
				return 0

			print('found the flag')
			try:
				if space_list[i-11].color == red: 
					cost_list.append(space_list[i-11].t_cost)
					index_list.append(i-11)
			except IndexError:
				print('IdexError')		
			try:
				if space_list[i-10].color == red: 
					cost_list.append(space_list[i-10].t_cost)
					index_list.append(i-10)
			except IndexError:
				print('IdexError')		
			try:
				if space_list[i-9].color == red: 
					cost_list.append(space_list[i-9].t_cost)
					index_list.append(i-9)
			except IndexError:
				print('IdexError')		
			try:
				if space_list[i-1].color == red: 
					cost_list.append(space_list[i-1].t_cost)
					index_list.append(i-1)
			except IndexError:
				print('IdexError')		
			try:
				if space_list[i+1].color == red: 
					cost_list.append(space_list[i+1].t_cost)
					index_list.append(i+1)
			except IndexError:
				print('IdexError')		
			try:
				if space_list[i+9].color == red: 
					cost_list.append(space_list[i+9].t_cost)
					index_list.append(i+9)
			except IndexError:
				print('IdexError')		
			try:
				if space_list[i+10].color == red:
					cost_list.append(space_list[i+10].t_cost)
					index_list.append(i+10)
			except IndexError:
				print('IdexError')		
			try:
				if space_list[i+11].color == red:
					cost_list.append(space_list[i+11].t_cost)
					index_list.append(i+11)
			except IndexError:
				print('IdexError')		
		
			break	

	# take the smallest and paint
	for i in index_list:
		if space_list[i].t_cost == min (cost_list):
			space_list[i].color = yellow
			space_list[i].path_flag = True # to mark the next to become the space that is near to the next space to be painted