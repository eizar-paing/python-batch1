# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes', 'Apples')

# Cannot change
# fruits[2] = 'Berry'

# Using a constructor
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples')

# Get value
print(fruits[1])
print(type(fruits2))
print(type(fruits))

# Can't change value
# fruits[0] = 'Pears'

# Delete tuple
del fruits2

# Get length
print(len(fruits))


# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create set
fruits_set = {'Apples', 'Oranges', 'Mango', 'Grape'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Apples')
fruits_set.add('Mango')
print(fruits_set)

# You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
# print(fruits_set[1])

# Remove from set
fruits_set.remove('Grape')

# Add duplicate
fruits_set.add('Apples')

# Clear set
fruits_set.clear()
print(fruits_set)

# Delete
del fruits_set

# print(fruits_set)

tup1 = ("Rohan", "Physics", 21, 69.75)
tup2 = (1, 2, 3, 4, 5)
tup3 = ("a", "b", "c", "d")
tup4 = (25.50, True, -55, 1+2j)
tup5 = (1, 2, 3)

print(max(tup2, tup5))
