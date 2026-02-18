
frontend_students = {"Aiswarya", "Rahul", "Neha", "Arjun"}
backend_students = {"Rahul", "Kiran", "Meena", "Arjun"}
backend_students.add("Sneha")
frontend_students.remove("Neha")
both_courses = frontend_students.intersection(backend_students)
print("Students in both Frontend and Backend:", both_courses)
only_backend = backend_students.difference(frontend_students)
print("Students only in Backend:", only_backend)
total_students = frontend_students.union(backend_students)
print("Total unique students:", len(total_students))
course_counts = {
    "Frontend": len(frontend_students),
    "Backend": len(backend_students)
}
print("\nCourse Student Counts:")
for course, count in course_counts.items():
    print(course, ":", count)
new_course_counts = {
    course: count for course, count in course_counts.items()
}
new_course_counts["Fullstack"] = course_counts["Frontend"] + course_counts["Backend"]
print("\nUpdated Course Counts with Fullstack:")
print(new_course_counts)
