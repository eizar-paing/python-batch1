total = 0
for i in range(6):
    user_marks = int(input("Enter your marks: "))
    total += user_marks
print(total)

average_mark = total/6

if average_mark > 90:
    print("A1 Grade")
elif average_mark > 80:
    print("A2 Grade")
elif average_mark > 70:
    print("B1 Grade")
elif average_mark > 60:
    print("B2 Grade")
elif average_mark > 50:
    print("C1 Grade")
elif average_mark > 40:
    print("C2 Grade")
elif average_mark > 32:
    print("D Grade")
elif average_mark > 20:
    print("E1 Grade")
else:
    print("E2 Grade")
