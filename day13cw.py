import os


item = input("Enter the name of the new item: ")


filename = "items.txt"

if not os.path.exists(filename):
   
    with open(filename, "w") as file:
        file.write(item + "\n")
    print("File created and item added.")
else:
 
    with open(filename, "a") as file:
        file.write(item + "\n")
    print("Item added to existing file.")


print("\nFull List of Items:")
with open(filename, "r") as file:
    items = file.readlines()
    for i in items:
        print(i)