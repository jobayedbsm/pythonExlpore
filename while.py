attempt=0

while attempt<6:
    password=input('Enter your pass:')
    if(password=="123"):
        print('successfully login')
        break
    attempt+=1
    if(attempt==3):
        print('you triyed 3 times')
        print('your remaining attempt',6-attempt)
        continue
    