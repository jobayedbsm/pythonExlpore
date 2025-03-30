students = [("Alice", 25, 3.5), ("Bob", 20, 3.8), ("Charlie", 30, 3.2), ("David", 20, 3.9)]

# sort by multiple criteria
# Sort by Age, then by GPA (Descending)
students.sort(key=lambda x :(x[1],-x[2]))
print(students)