# # exercises to function
# # for nested loop
# def nested_loop(row_num): # can't put user_row here, u will have to give new name
#     for i in range(1, row_num + 1):
#         for j in range(i):
#             print(i, end = "")
#         print()

# user_row = int(input("Enter your row number: "))
# nested_loop(user_row)


# # *  *  *  *
# # *        *
# # *        *
# # *  *  *  *

# # for square_star
# def square_star(a_b):
#     for i in range(a_b):
#         for j in range(a_b):
#             if i == 0 or i == a_b - 1 or j == 0 or j == a_b - 1:
#                 print("*", end = " ")
#             else:
#                 print(" ", end = " ")
#         print()

# user_input = int(input("Enter your row number: "))
# square_star(user_input)

# Trace
# user will input her value in user_input
# user's value is subtarct with 1 so 2 ==> 1, 3 ==>, index line
# that new value is put into fun in argu
# it went to the fun para then start to work

# if the user's new value is 4
# outer loop, i ==> 0 , vertical m=line (*)
#           inner loop ==> 0 , horizontal line (*)
#           inner loop ==> 1 (*)
#           inner loop ==> 2 (*)
#           inner loop ==> 3 (*)
#           inner loop ==> 4 (*)

# outer loop, i ==> 1 , vertical m=line
#           inner loop ==> 0 , horizontal line (*)
#           inner loop ==> 1
#           inner loop ==> 2
#           inner loop ==> 3
#           inner loop ==> 4 (*)

# outer loop, i ==> 2 , vertical m=line
#           inner loop ==> 0 , horizontal line (*)
#           inner loop ==> 1
#           inner loop ==> 2
#           inner loop ==> 3
#           inner loop ==> 4 (*)
    
# outer loop, i ==> 3 , vertical m=line
#           inner loop ==> 0 , horizontal line
#           inner loop ==> 1
#           inner loop ==> 2
#           inner loop ==> 3
#           inner loop ==> 4

# outer loop, i ==> 4 , vertical m=line
#           inner loop ==> 0 , horizontal line
#           inner loop ==> 1
#           inner loop ==> 2
#           inner loop ==> 3
#           inner loop ==> 4

# new one
def my_color(my_list):
    print(f"my fav color is {my_list[user_fav]}")

list_list = []

for i in range(5): # 0 to 4
    user_list = input("Enter your colors: ")
    list_list.append(user_list)

print(list_list)
user_fav = int(input("Enter your fav colors index: "))
my_color(list_list)
