while(True):
    you=input("Enter your choice(rock/paper/scissor) : ")
    choose=["rock","paper","scissor"]
    import random
    computer=random.choice(choose)
    while you not in choose:
        you=input("Invalid Input. Enter your choice(rock/paper/scissor) : ")
        break
    print("Computer chose",computer,"you chose",you)
    if you==computer:
        print("Both selected",you,"It's a Tie")
    elif you=="rock":
        if computer=="scissor":
            print("Rock beats scissors! You win")
        else:
            print("Paper beats rock! You lose")
    elif you=="paper":
        if computer=="rock":
            print("Paper beats rock! You win")
        else:
            print("Scissor beats paper! You lose")
    elif you=="scissor":
        if computer=="paper":
            print("Scissor beats paper! You win")
        else:
            print("Rock beats scissor! You lose")
    a=input("Do you want to play again? (yes/no): ")
    if(a=="yes"):
        continue
    else:
        print("Thank you for playing")
        break