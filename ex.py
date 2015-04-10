readfile = open('example.txt','r')

content = readfile.readline()
location = readfile.tell()
print(content[:-1]+"; The pointer is now at",location)

print("Return to character number 10:")
readfile.seek(10)
content = readfile.read()
print(content)

readfile.close()
