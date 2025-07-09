file = open('data.txt','r')
content = file.readline()
print(content)
file.close()

file = open('data.txt','w')
file.write("New Content to be added to file")
file.close()

