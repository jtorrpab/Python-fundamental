file = open("./text.txt")
print(file.readline())
#print(file.read())

for line in file:
    print(line)

file.close()


with open('./text.txt') as file:
    for line in file:
        print(line)
