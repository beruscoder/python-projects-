import random

aipoints = 0 
humanpoints = 0

def rockpaperscissor():
    moves = ["rock","paper","scissor"]
    dict = {1:"rock",2:"paper",3:"scissor"}    
    name = input("enter your name ?")
    aipoints = 0 
    humanpoints = 0
    while(aipoints<3 and humanpoints<3):
        aimove = random.choice(moves)
        try:
            human = int(input("enter the value 1 for rock, 2 for paper,3 for scissor"))
            if human not in [1,2,3]:
                print("choose between these")
                continue
        except ValueError:
            print("value between 1 to 3")
            continue
        if aimove == dict[human]:
            print("nobody got point")
        elif (aimove == "rock" and human == 2):
            print("human got point")
            humanpoints +=1
        elif(aimove == "paper" and human == 1):
            print("computer got point ")
            aipoints +=1
        elif(aimove == "rock" and human == 3):
            print("computer got point")
            aipoints +=1
        elif(aimove == "scissor" and human==1):
            print("human got point")
            humanpoints +=1
        elif(aimove=="paper" and human == 3):
            print("human got poimt")
            humanpoints +=1
        elif(aimove=="scissor" and human==2):
            print("computer got point")
            aipoints +=1
        else:
            print("choose between 1,2,3")
    if(aipoints>humanpoints):
        print("computer won")
    else:
        print("human won")    

rockpaperscissor()