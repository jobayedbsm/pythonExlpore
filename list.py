fruits = ["apple", "banana", "orange", "banana", "grape"]
# is data exist in the list


try:
    if fruits.count('bananas')>0:
        print('yes, banana is present in the list')
    else:
        print('banana is not in list')
except:
    print('There was an error occured')


