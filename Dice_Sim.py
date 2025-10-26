import random
playing=True
while playing:
    permission=input("Would you like to roll the dice?(y/n) ").lower()
    if permission=='y':
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(f"You got {dice1} and {dice2}")
        print("Thank you for playing.")
    elif permission=='n':
        playing=False
        break    
    else:
        print("Please choose y or n")
