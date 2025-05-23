import random

def game():
    randomval = random.randint(0,1000)
    uservalue = int(input("enter the value"))
    while(uservalue!=randomval):
        if(uservalue>randomval):
            print("go lower")
            uservalue = int(input("enter the value"))
        else:
            print("go higher")
            uservalue = int(input("enter the value"))
    print("randomvalue:",randomval, "uservalue:",uservalue)

game()
