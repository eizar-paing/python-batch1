# Python program for implementation of MergeSort

# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]

#merge(arr, 0, 0, 1)
# arr = [12, 11, 13, 5, 6, 7]
# n1 = 0 - 0 + 1
# n2 = 1-0
# L = [0] * 1
# R = [0] * 1

#arr = [12, 11, 13, 5, 6, 7]


def merge(arr, l, m, r): #merge(arr, 0, 0, 1) L = arr[0] => [12] , R = arr[1] => [11]
	n1 = m - l + 1 # 1 , 0-0+1 = 1 => 4 - 3 + 1 = 2 [5, 6]
	n2 = r - m # 1, 1- 0 = 1 => 5-4 = 1 [7]

	#[11, 12, 13, 5, 6, 7] => merge(arr, 0, 1, 2) => n1 = 2, n2 = 1

	# create temp arrays
	L = [0] * (n1) # [0, 0]
	R = [0] * (n2) # [0]
	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1): # 0 => 0
		L[i] = arr[l + i] # [11, 12] 

	for j in range(0, n2): # 0 => 0
		R[j] = arr[r] # 0 + 1 + 0 # [11] # m + 1 + j , [13]

	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = l	 # Initial index of merged subarray
	# L = [12], R = [11]
	# arr[0] = 11

	# L = [11, 12], R = [13]
	# arr[0] = 11
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i] #arr = [11, 12, 13, 5, 6, 7]
			i += 1 # i = 2
		else:
			arr[k] = R[j] #arr = [11, 11, 13, 5, 6, 7]
			j += 1 # j = 1
		k += 1 # k = 2

	# Copy the remaining elements of L[], if there
	# are any
	while i < n1:
		arr[k] = L[i] #arr = [11, 12, 13, 5, 6, 7]
		i += 1 # i = 1
		k += 1 # k = 2

	# Copy the remaining elements of R[], if there
	# are any
	while j < n2:
		arr[k] = R[j] #arr = [11, 12, 13, 5, 6, 7]
		j += 1 # j = 1
		k += 1 # k = 3
# l is for left index and r is right index of the
# sub-array of arr to be sorted

# l = 3 , r =5  => 4
# l = 0 , r = 2 => 

def mergeSort(arr, l, r): # l = 0, r = 5
	if l < r:

		# Same as (l+r)//2, but avoids overflow for
		# large l and h
		m = l+(r-l)//2 # (l + r) // 2

		# Sort first and second halves
		mergeSort(arr, l, m)
		mergeSort(arr, m+1, r)
		merge(arr, l, m, r)

# mergeSort(arr, 0, n-1) => mergeSort(arr, 0, 5) => m = 2
    #mergeSort(arr, 0, 2) => m = 1
        #mergeSort(arr, 0, 1) => m = 0
            #mergeSort(arr, 0, 0)
            #mergeSort(arr, 1, 1)
            #merge(arr, 0, 0, 1) # [12] [11] , arr = [11, 12, 13, 5, 6, 7]
        #mergeSort(arr, 2, 2)
        #merge(arr, 0, 1, 2) #arr = [11, 12, 13, 5, 6, 7]
    #mergeSort(arr, 3, 5) => m = 4
        #mergeSort(arr, 3, 4) => m = 3
            #mergeSort(arr, 3, 3)
            #mergeSort(arr, 4, 4)
            #merge(arr, 3, 3, 4) 
        #mergeSort(arr, 5, 5)
        #merge(arr, 3, 4, 5)
    #merge(arr, 0, 2, 5) 


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]

n = len(arr)
print("Given array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

mergeSort(arr, 0, n-1)
print("\n\nSorted array is")
for i in range(n):
	print("%d" % arr[i],end=" ")

# This code is contributed by Mohit Kumra
