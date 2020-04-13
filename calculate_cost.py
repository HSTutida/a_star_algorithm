# Receive two spaces position and return 
# the h or g cost between the two spaces
def calculate(x1,y1,x2,y2):
	# the algorithm will count how many times x1 and y1 was
	# summed or subtracted until achieve x2 and y2 values 
	# if x1 and y1 are iterated at the same time, the cost receive
	# +14, if only one is changed, the cost receive +10
	'''
	x1 = space_list[i].x
	y1 = space_list[i].y
	x2 = space_list[z].x
	y2 = space_list[z].y
	'''
	x_change = False
	y_change = False
	cost = 0
	while x1 != x2 or y1 != y2:
		if x1<x2:
			x1 +=1
			x_change = True
		elif x1>x2:
			x1 -=1
			x_change = True
		elif x1 == x2:
			x_change = False
		
		if y1<y2:
			y1 +=1
			y_change = True
		elif y1>y2:
			y1 -=1
			y_change = True
		elif y1 == y2:
			y_change = False
		
		if x_change and y_change:
			cost += 14 
		elif x_change and not(y_change):
			cost +=10
		elif y_change and not(x_change):
			cost +=10
	
	#print(cost)
	return cost	
# calculate(0,5,3,0) to test