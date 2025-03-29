fruits = ['apple', 'banana', 'cherry',"apple"]
# list comprehension (Remove all occurrence)
try:
    newList=[fruit for fruit in fruits if fruit!="apple"]
    print(newList)
except ValueError:
    print('No value occurrence in the list')