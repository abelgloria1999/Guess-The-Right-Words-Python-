name = input("Enter File\n")
count = dict()
fhandle = open(name)
for lines in fhandle:
    words = lines.split()
    for word in words:
        count[word] = count.get(word, 0) + 1
print(count)
