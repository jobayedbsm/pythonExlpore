fruits = ["apple", "banana", "orange", "banana", "grape"]
# find the item in list

# If you need to find all occurrences of "banana"
try:
    indexes=[i for i,fruit in enumerate(fruits) if fruit=='banana']
    print('all index of banana',indexes)
except:
    print('banana is not in list')


