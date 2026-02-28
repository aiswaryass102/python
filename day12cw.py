try:
    # Ask user for book title
    title = input("Enter book title: ")

    # Validate title (only alphabets and spaces)
    if not all(char.isalpha() or char.isspace() for char in title):
        raise ValueError("Error: Title should contain only alphabets and spaces.")

    # Ask user for publication year
    year = input("Enter publication year: ")

    # Validate year (must be 4 digits and start with 19 or 20)
    if not (year.isdigit() and len(year) == 4 and (year.startswith("19") or year.startswith("20"))):
        raise ValueError("Error: Year must be a 4-digit number starting with 19 or 20.")

    print("\nBook details accepted successfully!")
    print("Title:", title)
    print("Publication Year:", year)

except ValueError as e:
    print(e)

finally:
    print("\nProgram execution completed.")