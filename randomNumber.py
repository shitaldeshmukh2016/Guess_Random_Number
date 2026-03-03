import random

target=random.randint(1,100)

while True:
    userChoice=input("Guess the target number between 1 and 100 OR Quit: ")
    if(userChoice=="Quit"):
        break


    userChoice=int(userChoice)
    if(userChoice==target):
        print("sucess : Correct Guess!!")
        break
    elif(userChoice>target):
        print("your number was too big.Take samller guess.")
    else:
        print("your number to small.Take bigger guess.")

print("______GAME OVER________")
