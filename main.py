file = open("sample.txt","r")

# .seek() place the cursor in the desired position
file.seek(5)
print(file.readline())

# Return the cursor positioon in bytes
print(file.tell())
