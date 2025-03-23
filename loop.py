students = {
    "Alice": 85,
    "Bob": 72,
    "Charlie": 90,
    "David": 65,
    "Emma": 78
}

def grade(st):
  if st>=90:
    return "A"
  elif st>=80:
    return "B"
  elif st>=70:
    return "C"
  elif st>=60:
    return "D"
  else:
    return "F"
  

for i,v in students.items():
  print(f"{i} is grade {v}")