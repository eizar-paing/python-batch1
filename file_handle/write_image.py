f = open("cat1.jpeg", "rb")
image_binary = f.read()

f = open("image.txt", "wb")
f.write(image_binary)
