class AI():
	#assign board places static values based on their strategic value
	STATICBOARDVALUES = [[100,50,50,50,50,50,50,100],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[100,50,50,50,50,50,50,100]]

	def getMove(validMoves):
		coords = [0,0]
		value = 0
		
		#loop through board looking for most strategic location
		for x in range(len(validMoves)):
			for y in range(len(validMoves[1])):
				if validMoves[x][y] == 1 and STATICBOARDVALUES[x-1][y-1] > value:
					coords = [x,y]
		
		return coords