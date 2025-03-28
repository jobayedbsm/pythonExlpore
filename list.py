fruits = ["apple", "banana", "orange", "banana", "grape"]
# it's means value in extend should be iterable 

print(fruits.index('banana'))

newListWithOutBanana=[fruit for fruit in fruits if fruit=='banana']
print(newListWithOutBanana)