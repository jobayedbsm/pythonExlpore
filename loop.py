students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Emma": 78
}

def grade(scores):
    if scores>90:
        return "A"
    elif scores>=80:
        return "B"
    elif scores >=70:
        return "C"
    elif scores >=60:
        return "D"
    else:
        return "F"
    
for name,value in students.items():
    print(f"{name} his grade is {grade(value)}")
print('Graddig calculation has succesfully done')