def NullifyMatrix(matrix):
	row_has_zero = False
	col_has_zero = False

	def NullifyRow(row):
		for i in range(0, len(row)):
			row[i] = 0

	def NullifyCol(matrix, col):
		for i in range (0, len(matrix)):
			matrix[i][col] = 0
		

	for elem in matrix[0]:
		if elem == 0:
			row_has_zero = True
			break

	for row in matrix:
		if row[0] == 0:
			col_has_zero = True
			break

	# Set first col and row elements to zero in the rest of the array
	for i in range(1, len(matrix)):
		for j in range(1, len(matrix[0])):
			if matrix[i][j] == 0:
				matrix[i][0] = 0
				matrix[0][j] = 0

	for i in range(1, len(matrix)):
		if matrix[i][0] == 0:
			NullifyRow(matrix[i])

	for j in range(1, len(matrix[0])):
		if matrix[0][j] == 0:
			NullifyCol(matrix, j)
	
	if row_has_zero:
		NullifyRow(matrix[0])
	
	if col_has_zero:
		NullifyCol(matrix, 0)
matrix1 = [[1, 0, 2], [1, 1, 0], [1, 1, 1]]
matrix2 = [[1, 1, 1, 1], [2, 2, 0, 2], [3, 3, 3, 3], [4, 4, 4, 4]]

NullifyMatrix(matrix1)
print matrix1

NullifyMatrix(matrix2)
print matrix2
