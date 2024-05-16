# Selection Sort algorithm in Python
def selectionSort(array, size):
	
	for s in range(size): #outer loop
		min_idx = s
		for i in range(s + 1, size): #inner loop
			
			# For sorting in descending order
			# for minimum element in each loop
			if array[i] < array[min_idx]: # arr[1] < arr[0], 2 < 7
				min_idx = i # min_idx = 2

		# Arranging min at the correct position
		(array[s], array[min_idx]) = (array[min_idx], array[s]) # arr[0] = arr[1], arr[1] = arr[0] [2, 7, 1, 6]

# Driver code
data = [ 7, 2, 1, 6 ]
size = len(data)
selectionSort(data, size)

print('Sorted Array in Ascending Order is :')
print(data)


# [ 7, 2, 1, 6 ]
#outer loop => i = 0 => length-1 
# inner loop => j = i + 1 => length -1
 # min_idx = i = 0 
 # i = 0, j = 1 => array[1] < array[min_idx] => min_idx = j = 1
 # i = 0, j = 2 => array[2] < array[min_idx] => min_inx = j = 2
 # i = 0, j = 3 => array[3] < array[min_idx]
 # array[i], array[min_idx] = array[min_idx], array[i]
# [ 1, 2, 7, 6 ]

#outer loop => i = 1 => length-1 
# inner loop => j = i + 1 => length -1
 # min_idx = i = 1 
 # i = 1, j = 2 => array[2] < array[min_idx]
 # i = 1, j = 3 => array[3] < array[min_idx] 
# array[i], array[min_idx] = array[min_idx], array[i]
 # [ 1, 2, 7, 6 ]

#outer loop => i = 2 => length-1 
# inner loop => j = i + 1 => length -1
 # min_idx = i = 2 
 # i = 2, j = 3 => array[3] < array[min_idx] => min_inx = j = 3

# array[i], array[min_idx] = array[min_idx], array[i]
 # [ 1, 2, 6, 7 ]
