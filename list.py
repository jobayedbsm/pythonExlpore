my_list = ["apple", "banana", "cherry","apple"]
# find the item in list
finditem=my_list.index('banana')
# handing error if data not exist

try:
    finditem=my_list.index('bananas')
    print('index of banana',finditem)
except:
    print('banana is not in list')


