# create dict
student = {
    'first_name': 'Aye',
    'last_name': 'Moe',
    'age': 12,
    'subject1': 'English',
    'subject2': 'Math',
    'subject3': 'Science'
}

# Get value by key
print(student['first_name'])
print(student.get('age'))

# Make dynamic name of key
test = 'subject'

for i in range(1, 4):
    print(student[test + str(i)])
# print(student.get(test))

# print(student['subject1'])
# print(student['subject2'])
# print(student['subject3'])

# Add key value
student['phone'] = '012-344-567'
print(student)

print(student.keys())
print(student.items())


person = student.copy()

person['city'] = 'Yangon'

# Remove item
del student['subject1']
student.pop('phone')

# Clear
student.clear()
print(student)

del student

print(person)
print(len(person))
# print(student)
