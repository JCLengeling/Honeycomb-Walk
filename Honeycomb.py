neighbourFields = 6
n = 0
#generate play field

field = []
for x in range(0, 30):
	field.append([])
	for y in range(0, 30):
		field[x].append([])
		#save the results for increased performance
		for s in range(0, 15):
			field[x][y].append(0)

def walks(x,y,s):
	#Lookup if we already know the number of steps
	if field[x][y][s]:
		return field[x][y][s];

	
	#return if we managed to return to the center (1) or if not (0)
	if s == 0:
		return x==15 and y ==15

	#check for my 6 neighbours and increase the amount
	field[x][y][s]=field[x][y][s] + walks(x-1,y-1,s-1);
	field[x][y][s]=field[x][y][s] + walks(x+1,y+1,s-1);
	field[x][y][s]=field[x][y][s] + walks(x-1,y,s-1);
	field[x][y][s]=field[x][y][s] + walks(x+1,y,s-1);
	field[x][y][s]=field[x][y][s] + walks(x,y-1,s-1);
	field[x][y][s]=field[x][y][s] + walks(x,y+1,s-1);
	
	return field[x][y][s];
	

#numberOfRuns = int(input('Number of program runs:'))	
numberOfRuns = int(input())

while numberOfRuns > 0:
	while n<1 or n>15:
		#n = int(input('Enter the number of steps (between 1 and 14): '))
		n = int(input())
	#print ("Number of steps, n = " + str(n))
	#(15,15) is the middle of the field
	#print ("Number of different walks: " + str(walks(15,15,n)))
	print (str(walks(15,15,n)))
	n = 0
	numberOfRuns - 1

