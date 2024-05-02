f = open("demofile.txt", "a")
f.write("Now the file has more content!")
# "studentname, school name, mark1, mark2, mark3"

f = open("demofile.txt", "r")
print(f.read())
f.close()