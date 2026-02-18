
python_students = {"Aiswarya", "Archa", "Meera"}
data_science_students = {"lekshmi", "Meena", "Priya"}
python_students.add("Kiran")
data_science_students.remove("Priya")
both_courses = python_students.intersection(data_science_students)
print("Students in both courses:", both_courses)
only_python = python_students.difference(data_science_students)
print("Students only in Python:", only_python)
all_students = python_students.union(data_science_students)
print("All students:", all_students)
course_dict = {
    "Python": len(python_students),
    "Data Science": len(data_science_students)
}
for course, count in course_dict.items():
    print(f"Course: {course}, Students: {count}")
growth_dict = {course: count * 2 for course, count in course_dict.items()}
print("Expected Growth:", growth_dict)
