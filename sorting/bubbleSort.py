# Python3 program for Bubble Sort Algorithm Implementation
def bubbleSort(arr):
     
  n = len(arr)

  # For loop to traverse through all 
  # element in an array
  for i in range(n-1): # 3, 0 to 2
    for j in range(0, n - i - 1): # (0, 3)
      # Range of the array is from 0 to n-i-1
      # Swap the elements if the element found 
      #is greater than the adjacent element
      if arr[j] > arr[j + 1]: # arr[0] > arr[1]
          arr[j], arr[j + 1] = arr[j + 1], arr[j] # arr[0] = arr[1], arr[1] = arr[0]

# 3, i(0 to 2)
          # j(0, 3) --> arr[0] > arr[1], 2 > 1
          # arr[0] = arr[1], arr[1] = arr[0], [1, 2, 10, 23]

          # j(1, 3) --> arr[1] > arr[2], 2 > 10
          # no changes will happen,  [1, 2, 10, 23]

          # j(2, 3) --> arr[2] > arr[3], 10 > 23
          # no changes will happen,  [1, 2, 10, 23]

# new_arr 
      # 3, i(0 to 2)
          # j(0, 3) --> new_arr[0] > new_arr[1], 7 > 6
          # new_arr[0] = new_arr[1], new_arr[1] = new_arr[0], [6, 7, 4, 3]

          # j(1, 3) --> new_arr[1] > new_arr[2], 7 > 4
          # new_arr[1] = new_arr[2], new_arr[2] = new_arr[1], [6, 4, 7, 3]

          # j(2, 3) --> new_arr[2] > new_arr[3], 7 > 3
          # new_arr[2] = new_arr[3], new_arr[3] = new_arr[2], [6, 4, 3, 7] 

      # 3, i(1 to 2) --> 
          # j(0, 3) --> new_arr[0] > new_arr[1], 6 > 4
          # new_arr[0] = new_arr[1], new_arr[1] = new_arr[0], [4, 6, 3, 7]

          # j(1, 3) --> new_arr[1] > new_arr[2], 6 > 3
          # new_arr[1] = new_arr[2], new_arr[2] = new_arr[1], [4, 3, 6, 7]

          # j(2, 3) --> new_arr[2] > new_arr[3], 6 > 7
          # no changes will happen, [4, 3, 6, 7]

          # .... continue
          # [3, 4, 6, 7]
          


#(n-1)*(3+2+1) = 18 = 4 * 4 = 16
                 
# Driver code
 
# Example to test the above code
arr = [2, 1, 10, 23 ] # 4
new_arr = [7, 6, 4, 3]
 
bubbleSort(arr)
bubbleSort(new_arr)

 
print("Sorted array is:")
for i in range(len(arr)):
  print("%d" % arr[i])

print("New Sorted array is:")
for i in range(len(new_arr)):
  print("%d" % new_arr[i])