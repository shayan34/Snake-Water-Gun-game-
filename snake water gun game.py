
import random

print('Snake - Water - Gun ')

n = int(input("Enter the numbers of rounds : "))

options = [ 's' , 'w', 'g']     #jo optoin ma spaceing hoge woii computer or player ma comparison ma use hoge.

rounds= 1 

comp_win = 0

user_win = 0

while rounds <= n :

    #Rounds display.

    print(f"Round :{rounds}\nSnake - 's' \nWater - 'w'\nGun - 'g'" )

    #Players choose the options.

    try:
        player = input("Choose the options: ")
    except EOFError as e:
        print(e)

    if player != 's' and player != 'w' and player != 'g':
        print ("Invalid input , try again")
        continue
    
    #Computer choose ramdom options.

    computer = random.choice(options)

    #Game conditions on 3 options.
 
    if computer == 's':                #same hogee options jasi.
        if player == 'w':
            comp_win += 1
        elif player == 'g':
            user_win += 1    

    elif computer == 'w':
        if player == 'g':
            comp_win += 1
        elif player == 's':
            user_win += 1

    
    elif computer == 'g':
        if player == 's':
            comp_win += 1
        elif player == 'w':
            user_win += 1

    #Check whos win and rounds addition.

    if user_win > comp_win :
        print(f"User won round {rounds}\n")
    elif comp_win > user_win :
        print(f"Computer won round {rounds}\n")
    else:
        print("Round Draw")

    rounds += 1


# Finallay.

if user_win > comp_win :
    print ("\nUser won ! congratulations.")
elif comp_win> user_win:
    print ("\nComp won ! congratulations.")
else :
    print("\nMatch Draw")

