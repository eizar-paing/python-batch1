number_list = [-5, -4, - 1, 0, 1, 2, 3 ]
# less_then_zero = [-5, -4, -1]

less_then_zero = list(filter(lambda x: x < 0 , number_list))
print(less_then_zero)

even_list = list(filter(lambda x : x %2 == 0, number_list))
print(even_list)

