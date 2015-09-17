__author__ = 'Ishan <ishanatmuzaffarpur@gmail.com>'

import argparse
# import pdb

# Setting comaand line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--debug', help='Displays the steps for explanation', action='store_true')
parser.add_argument('-v', '--verbose', help='Prints out all information reagrding inner workings', action='store_true')
args = parser.parse_args()


rows, columns = map(int, input().split())
# print(rows, columns)
forest = []
for i in range(rows):
	# print(input().split())
	forest.append(input().split())
	# print(forest[i])

if args.debug or args.verbose:
	# Printing the forest in its full glory
	print('Base-Camp',end='\n\n')
	print('The Forest')
	for i in range(rows):
		for j in range(columns):
			print(forest[i][j], end=" ")
		print("")

# Making the playground -2 for Not Accessible, -1 for not reachable (all accessible places are unreachable in the beginning)
playground = forest
playerCount = 0
playerPosition = []
for i in range(rows):
	for j in range(columns):
		if playground[i][j] is 'w':
			playground[i][j] = -2
		elif playground[i][j] is 'd':
			playground[i][j] = 0
		elif playground[i][j] is 's':
			playground[i][j] = -1
			playerCount += 1
			playerPosition.append([i, j])
		else:
			playground[i][j] = -1

# Offset values to aid in calculating 8-distance
offsets = [[-1,-1], [-1,0], [-1, 1],
		   [ 0,-1],         [ 0, 1],
		   [ 1,-1], [ 1,0], [ 1, 1]]
# Calculating the distance from destination ('0') First Pass
for i in range(rows):
	for j in range(columns):
		# Default values for 8-connected distance measurement
		defaultValues = []
		if playground[i][j] > -2 and playground[i][j] != 0:
			# 8 / 8 Connected calculation
			for ofs in offsets:
				rpos = i + ofs[0]
				cpos = j + ofs[1]
				if args.verbose:
					# Printing Verbose information
					print(rpos > -1 ,cpos > -1 ,rpos < rows, cpos < columns, sep = " ")
				if rpos > -1 and cpos > -1 and rpos < rows and cpos < columns:
					if playground[rpos][cpos] > -1:
						defaultValues.append(playground[rpos][cpos] + 1)
					else:
						pass
				else:
					pass
			# End of calculation of 8 - distance
		else:
			if args.verbose:
				# Printing Verbose information
				print('This is not accessible block and don\'t have to do anything')
			pass

		# Finding the minimum and assigning it to the playground
		if args.verbose:
			# Printing Verbose information
			print(i,j,defaultValues,sep='-')
		try:
			if playground[i][j] == -1:
				playground[i][j] = min(defaultValues)
			elif playground[i][j] > -1:
				playground[i][j] = min(playground[i][j], min(defaultValues))
		except:
			pass

# Calculating the distance from destination ('0') Second Pass
for i in reversed(range(rows)):
	for j in reversed(range(columns)):
		# Default values for 8-connected distance measurement
		defaultValues = []
		if playground[i][j] > -2 and playground[i][j] != 0:
			# 8 / 8 Connected calculation
			for ofs in offsets:
				rpos = i + ofs[0]
				cpos = j + ofs[1]
				if args.verbose:
					# Printing Verbose information
					print(rpos > -1 ,cpos > -1 ,rpos < rows, cpos < columns, sep = " ")
				if rpos > -1 and cpos > -1 and rpos < rows and cpos < columns:
					if playground[rpos][cpos] > -1:
						defaultValues.append(playground[rpos][cpos] + 1)
					else:
						pass
				else:
					pass
			# End of calculation of 8 - distance
		else:
			if args.verbose:
				# Printing Verbose information
				print('This is not accessible block and don\'t have to do anything')
			pass

		# Finding the minimum and assigning it to the playground
		if args.verbose:
			# Printing Verbose information
			print(i,j,defaultValues,sep='-')
		try:
			if playground[i][j] == -1:
				playground[i][j] = min(defaultValues)
			elif playground[i][j] > -1:
				playground[i][j] = min(playground[i][j], min(defaultValues))
		except:
			pass

# Calculating the distance from destination ('0') Third Pass
for i in range(rows):
	for j in range(columns):
		# Default values for 8-connected distance measurement
		defaultValues = []
		if playground[i][j] > -2 and playground[i][j] != 0:
			# 8 / 8 Connected calculation
			for ofs in offsets:
				rpos = i + ofs[0]
				cpos = j + ofs[1]
				if args.verbose:
					# Printing Verbose information
					print(rpos > -1 ,cpos > -1 ,rpos < rows, cpos < columns, sep = " ")
				if rpos > -1 and cpos > -1 and rpos < rows and cpos < columns:
					if playground[rpos][cpos] > -1:
						defaultValues.append(playground[rpos][cpos] + 1)
					else:
						pass
				else:
					pass
			# End of calculation of 8 - distance
		else:
			if args.verbose:
				# Printing Verbose information
				print('This is not accessible block and don\'t have to do anything')
			pass

		# Finding the minimum and assigning it to the playground
		if args.verbose:
			# Printing Verbose information
			print(i,j,defaultValues,sep='-')
		try:
			if playground[i][j] == -1:
				playground[i][j] = min(defaultValues)
			elif playground[i][j] > -1:
				playground[i][j] = min(playground[i][j], min(defaultValues))
		except:
			pass

# Debugging
# pdb.set_trace()

# Running by the players
if args.verbose:
	# Printing Verbose information
	print('Running by the players')
playerGrids = []
for x in range(playerCount):
	if args.verbose:
		# Printing Verbose information
		print('player', x, sep='=')
	playerGrids.append([])
	if args.verbose:
		# Printing Verbose information
		print(playerPosition, playerPosition[x], sep = ' | ')
	playerValue = playground[playerPosition[x][0]][playerPosition[x][1]]
	playerGrids[x].append([playerPosition[x][0], playerPosition[x][1]])
	i, j = playerPosition[x][0], playerPosition[x][1]
	if args.verbose:
		# Printing Verbose information
		print('i', i, 'j', j, sep='=')
	while playerValue > 0:
		if args.verbose:
			# Printing Verbose information
			print(x, 'beginning loop playerValue', playerValue, sep='=')

		# 2 / 8 of  8 - Connected
		rpos = i - 1
		cpos = j - 0
		if (rpos > -1 and cpos > -1 and rpos < rows and cpos < columns) and (playground[rpos][cpos] < playerValue and playground[rpos][cpos] > -1):
			if args.verbose:
				# Printing Verbose information
				print('2/8', rpos, cpos, playground[rpos][cpos], playerValue, sep='-' )
			playerGrids[x].append([rpos, cpos])
			playerValue = playground[rpos][cpos]
			i, j = rpos, cpos
			if args.verbose:
				# Printing Verbose information
				print('2/8 playerValue', playerValue, sep='=')
		else:
			# pass
			# 4 / 8 of  8 - Connected
			rpos = i - 0
			cpos = j - 1
			if (rpos > -1 and cpos > -1 and rpos < rows and cpos < columns) and (playground[rpos][cpos] < playerValue and playground[rpos][cpos] > -1):
				if args.verbose:
					# Printing Verbose information
					print('4/8', rpos, cpos, playground[rpos][cpos], playerValue, sep='-' )
				playerGrids[x].append([rpos, cpos])
				playerValue = playground[rpos][cpos]
				i, j = rpos, cpos
				if args.verbose:
					# Printing Verbose information
					print('4/8 playerValue', playerValue, sep='=')
			else:
				# pass
				# 5 / 8 of  8 - Connected
				rpos = i - 0
				cpos = j + 1
				if (rpos > -1 and cpos > -1 and rpos < rows and cpos < columns) and (playground[rpos][cpos] < playerValue and playground[rpos][cpos] > -1):
					if args.verbose:
						# Printing Verbose information
						print('5/8', rpos, cpos, playground[rpos][cpos], playerValue, sep='-' )
					playerGrids[x].append([rpos, cpos])
					playerValue = playground[rpos][cpos]
					i, j = rpos, cpos
					if args.verbose:
						# Printing Verbose information
						print('5/8 playerValue', playerValue, sep='=')
				else:
					# pass
					# 7 / 8 of  8 - Connected
					rpos = i + 1
					cpos = j - 0
					if (rpos > -1 and cpos > -1 and rpos < rows and cpos < columns) and (playground[rpos][cpos] < playerValue and playground[rpos][cpos] > -1):
						if args.verbose:
							# Printing Verbose information
							print('7/8', rpos, cpos, playground[rpos][cpos], playerValue, sep='-' )
						playerGrids[x].append([rpos, cpos])
						playerValue = playground[rpos][cpos]
						i, j = rpos, cpos
						if args.verbose:
							# Printing Verbose information
							print('7/8 playerValue', playerValue, sep='=')
					else:
						# pass
						# 1 / 8 of  8 - Connected
						rpos = i - 1
						cpos = j - 1
						if (rpos > -1 and cpos > -1 and rpos < rows and cpos < columns) and (playground[rpos][cpos] < playerValue and playground[rpos][cpos] > -1):
							if args.verbose:
								# Printing Verbose information
								print('1/8', rpos, cpos, playground[rpos][cpos], playerValue, sep='-' )
							playerGrids[x].append([rpos, cpos])
							playerValue = playground[rpos][cpos]
							i, j = rpos, cpos
							if args.verbose:
								# Printing Verbose information
								print('1/8 playerValue', playerValue, sep='=')
						else:
							# pass
							# 3 / 8 of  8 - Connected
							rpos = i - 1
							cpos = j + 1
							if (rpos > -1 and cpos > -1 and rpos < rows and cpos < columns) and (playground[rpos][cpos] < playerValue and playground[rpos][cpos] > -1):
								if args.verbose:
									# Printing Verbose information
									print('3/8', rpos, cpos, playground[rpos][cpos], playerValue, sep='-' )
								playerGrids[x].append([rpos, cpos])
								playerValue = playground[rpos][cpos]
								i, j = rpos, cpos
								if args.verbose:
									# Printing Verbose information
									print('3/8 playerValue', playerValue, sep='=')
							else:
								# pass
								# 6 / 8 of  8 - Connected
								rpos = i + 1
								cpos = j - 1
								if (rpos > -1 and cpos > -1 and rpos < rows and cpos < columns) and (playground[rpos][cpos] < playerValue and playground[rpos][cpos] > -1):
									if args.verbose:
										# Printing Verbose information
										print('6/8', rpos, cpos, playground[rpos][cpos], playerValue, sep='-' )
									playerGrids[x].append([rpos, cpos])
									playerValue = playground[rpos][cpos]
									i, j = rpos, cpos
									if args.verbose:
										# Printing Verbose information
										print('6/8 playerValue', playerValue, sep='=')
								else:
									# pass
									# 8 / 8 of  8 - Connected
									rpos = i + 1
									cpos = j + 1
									if (rpos > -1 and cpos > -1 and rpos < rows and cpos < columns) and (playground[rpos][cpos] < playerValue and playground[rpos][cpos] > -1):
										if args.verbose:
											# Printing Verbose information
											print('8/8', rpos, cpos, playground[rpos][cpos], playerValue, sep='-' )
										playerGrids[x].append([rpos, cpos])
										playerValue = playground[rpos][cpos]
										i, j = rpos, cpos
										if args.verbose:
											# Printing Verbose information
											print('8/8 playerValue', playerValue, sep='=')
									else:
										pass
	if args.verbose:
		# Printing Verbose information
		print(playerGrids[x])

if args.debug or args.verbose:
	print('')
	# Printing the playground in its full glory
	print('8-Distance Matrix')
	for i in range(rows):
		for j in range(columns):
			if playground[i][j] > -1:
				print(" ",playground[i][j], sep="", end=" ")
			else:
				print(playground[i][j], end=" ")
		print("")
	print('Legend :','-2: Not accessible', '-1: Not reachable by land', sep='\n',end='\n\n')

if args.verbose:
	# Printing Verbose information
	print(playerGrids)

# Displaying the resulting grids
if args.debug or args.verbose:
	print('Paths :', end='\n')
playerCharacters = ['a', 'b','c', 'd', 'e', 'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for x in range(playerCount):
	for i in range(rows):
		for j in range(columns):
			if playground[i][j] is 0:
				print('d', end=' ')
			elif [i,j] in playerGrids[x]:
				print(playerCharacters[x], end=' ')
			else:
				print('-',end=' ')
		print('')
	print('')