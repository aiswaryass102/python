
header = "BOOK STORE RECEIPT\n"

book1 = "Python Basics"
price1 = 450

book2 = "Data Science Intro"
price2 = 600

line1 = "Book Title: {}\tPrice: ₹{}\n".format(book1, price1)
line2 = "Book Title: {}\tPrice: ₹{}\n".format(book2, price2)

total = price1 + price2
total_line = "Total: ₹{}".format(total)


thank_you = "\nThank You for Shopping!"


receipt = header + line1 + line2 + total_line + thank_you


print(receipt.upper())
