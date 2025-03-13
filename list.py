fruits = ["apple", "banana", "orange", "banana", "grape"]

allOcurenceOfBanana=[index for index,value in enumerate(fruits) if value=="banana"]

for index in allOcurenceOfBanana:
    print('banana all index=',index)
