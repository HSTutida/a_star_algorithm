# check for the smallest cost green cells an paint it red

def smallest(space_list,green,red):
	#create a list of all costs
	red_list=[]
	cost_list = []
	
	for i in range(100):
		if space_list[i].color == green:
			cost_list.append(space_list[i].t_cost)
	for i in range(100):
		if space_list[i].color == red:
			red_list.append(space_list[i].t_cost)
	
	for i in range(100):
		if space_list[i].t_cost == min(cost_list) and space_list[i].color == green:
			try: 
				space_list[i].color = red
			except:
				print('error')	
		