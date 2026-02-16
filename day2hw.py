# Multiline string storing a paragraph about a Python course
paragraph = """
Python is a popular programming language used for web development, data analysis,
artificial intelligence, and automation. This Python course is designed for beginners
who want to learn programming concepts in a simple and practical way.
"""

# Remove extra whitespaces from start and end
paragraph = paragraph.strip()

# Display length of the paragraph
length = len(paragraph)
print("Length of paragraph:", length)

# Display first and last characters
print("First character:", paragraph[0])
print("Last character:", paragraph[-1])

# Slice and print first 50 characters
preview = paragraph[:50]
print("Preview (first 50 chars):", preview)

# Replace "Python" with "PYTHON"
replaced_paragraph = paragraph.replace("Python", "PYTHON")
print("\nAfter replacement:\n", replaced_paragraph)

# Convert entire paragraph to lowercase
lowercase_paragraph = paragraph.lower()
print("\nLowercase paragraph:\n", lowercase_paragraph)

# Split paragraph into individual words
words = paragraph.split()
print("\nList of words:\n", words)

# Check if the word "course" exists
if "course" in paragraph.lower():
    print("\nThe word 'course' was found in the paragraph.")
else:
    print("\nThe word 'course' was not found.")

# Display final message using format()
word_count = len(words)
final_message = "The course description is {} characters long and has {} words.".format(length, word_count)
print("\n" + final_message)
