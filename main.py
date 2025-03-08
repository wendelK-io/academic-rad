file = open("sample.txt","r")

# reads one line of the file at a time
print(file.readline())

# returns a list of strings from each line of the file
print(file.readlines())