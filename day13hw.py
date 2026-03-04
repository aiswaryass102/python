import os

filename = "students.txt"


if os.path.exists(filename):
    print("Existing Student Names:")
    with open(filename, "r") as file:
        for line in file:
            print(line)
else:
    print("No existing file found. A new file will be created.")


n = int(input("\nHow many student names do you want to add? "))


with open(filename, "a") as file:
    for i in range(n):
        name = input(f"Enter name {i+1}: ")
        file.write(name + "\n")

print("\nNames saved successfully!")


print("\nUpdated Student List:")
with open(filename, "r") as file:
    for line in file:
        print(line)