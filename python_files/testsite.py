lista = [1, 2, 3, 5]

print min(lista)


def transpose_matrix(matrix):
	
	t_matrix = []
	num_col = len(matrix[0])
	num_row = len(matrix) 
	
	for col in range(0, num_col):
		new_row = []
		for row in range(0, num_row):
			new_row.append(None)
		t_matrix.append(new_row)	

	for row in range(0, num_row):
		for col in range(0, num_col):
			t_matrix = t_matrix
	return t_matrix	


print lista


