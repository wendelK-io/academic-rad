file = open("sample.txt","w")

# Create/ overwrite a file
file.write("Hello, world!")
file.close()
print(file.closed)


# Lists - case 1

shopping_list_file = open("shopping_list", "w")
list = ["banana", "apple", "grapes", "breads", "juice"]

for item in list:
    shopping_list_file.write(str(item) + "\n")

shopping_list_file.close()

shopping_list_file = open("shopping_list", "r")
print(shopping_list_file.read())

# Lists - case 2

file = open("point_list", "w")
point_list = [("Bianca", "2.5"), ("Teo", "2"), ("Brenda", "4")]

for student, points in point_list:
    file.write(f"Student: {student} | Points: {points} \n")

file.close()

file = open("point_list", "r")
print(file.read())