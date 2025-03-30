employees = [
    {"name": "Alice", "age": 25, "salary": 5000},
    {"name": "Bob", "age": 20, "salary": 7000},
    {"name": "Charlie", "age": 30, "salary": 4500},
]

employees.sort(key=lambda x: x['salary'])

print(employees)