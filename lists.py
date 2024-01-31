numbers = [1, 2, 3, 4, 5]
fruits = ["Apple", "Orange", "Grape"]

print(fruits[1])
print(numbers[3])


print(len(fruits))

# Add value
fruits.append("Blueberry")  # ['Apple', 'Orange', 'Grape', 'Blueberry']

# Remove by value
fruits.remove("Orange")  # ['Apple', 'Grape', 'Blueberry']

# Insert value into specific position
fruits.insert(2, "Kiwi")  # ['Apple', 'Grape', 'Kiwi', 'Blueberry']

# Change Value
fruits[1] = "Orange"  # ['Apple', 'Orange', 'Kiwi', 'Blueberry']

# Remove by position
fruits.pop(2)  # ['Apple', 'Orange', 'Blueberry']

fruits.reverse()  # ['Blueberry', 'Orange', 'Apple']

fruits.sort()  # ['Apple', 'Blueberry', 'Orange']

fruits.sort(reverse=True)  # ['Orange', 'Blueberry', 'Apple']

print(fruits)

# nested list
nested_numbers = [[1, 11, 21], [2, 12, 22], [3, 13, 23], [4, 14, 24]]
for i in nested_numbers:
    for j in i:
        print(f'{j} ', end='')
    print()
