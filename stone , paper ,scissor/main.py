import random

computer = random.choice([-1,0,1])

dict ={
    "stone":1,
    "paper":-1,
    "scissor":0
}

reverseDict ={
    1:"stone",
    -1:"paper",
    0:"scissor"
}

userInput = input("Enter your choice: ")
userNum = dict[userInput]
print(f"computer chose {reverseDict[computer]}\n you chose {reverseDict[userNum]}")

if(computer==userNum):
    print("it's a Draw")
else:
    if(computer == -1 and userNum==1):
        print("You loose!")
    elif(computer == -1 and userNum==0):
        print("You win")
    elif(computer==1 and userNum== -1):
        print("You win")
    elif(computer == 1 and userNum == 0):
        print("You loose")          
    elif(computer == 0 and userNum == 1):
        print("You win")
    elif(computer==0 and userNum==-1):
        print("you win")    
    else:
        print("Something went wrong")
                        