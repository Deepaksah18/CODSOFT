import random
count_user=0
count_computer=0
play = ["Rock", "Paper", "Scissors"]
computer = play[random.randint(0,2)] 
player = False
while player == False: 
    player = input("Rock, Paper, Scissors?") 
    if player == computer: 
        print("Tie!") 
        print("No one scored because it's TIE!!")
    elif player == "Rock": 
        if computer == "Paper": 
            count_computer+=1
            print("You lose!", computer, "covers", player)
            print("computer score is")
            print(count_computer)
            print("your score is")
            print(count_user)
        else: 
            count_user+=1
            print("You win!", player, "smashes", computer) 
            print("computer score is")
            print( count_computer)
            print("your score is")
            print( count_user)

    elif player == "Paper": 
        if computer == "Scissors": 
            count_computer+=1
            print("You lose!", computer, "cuts", player)
            print("computer score is")
            print(count_computer)
            print("your score is")
            print(count_user)
             

        else:  
            count_user+=1
            print("You win!", player, "covers", computer) 
            print("computer score is")
            print(count_computer)
            print("your score is")
            print(count_user)


    elif player == "Scissors": 
        if computer == "Rock": 
            count_computer+=1
            print("You lose...", computer, "smashes", player) 
            print("your score is")
            print( count_user)
            print("computer score is")
            print(count_computer)

             


        else: 
            count_user+=1
            print("You win!", player, "cuts", computer) 
            print( count_computer)
            print("your score is")
            print(count_user)
            print("computer score is")
            print(count_computer)




    else: 
        print("That's not a valid play. Check the spelling!") 
    player = False 
    computer = play[random.randint(0,2)]