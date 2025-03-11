my_list = ["apple", "banana", "cherry","apple"]



# will return new list
newList=my_list+[100, 200, 300]
print(newList)

# will return new list by list unpacking
newList2=[*my_list,*[100, 200, 300]]
print(newList2)
