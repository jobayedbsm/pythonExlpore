my_list = ["apple", "banana", "cherry","apple"]

# insert data in specific index 
# there are another same function which is insert function
my_list[1]='jobayed'
# print(my_list)

# print data through loop

for data in my_list:
    print(data)

print('is there specific data exist')

if "data" in my_list:
    print('yes,data is exists there')
else:
    print('no, data is not exist in list')

print("add data in list in the last position")

my_list.append('pineapple')
print(my_list)

