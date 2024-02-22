import cust_module
import exercises


row_in = int(input("Enter row number : "))
cust_module.pyramid_star(row_in)
cust_module.new_fun()

exercises.get_fibonacci(1, 1)

add_result = cust_module.add(5, 6)
final_result = cust_module.multiply(add_result, 10)
print(final_result)

result1 = cust_module.add(5, 6, 7)
another_cal = cust_module.multiply(result1, 10, 2)
print(another_cal)