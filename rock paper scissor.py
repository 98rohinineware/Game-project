import random
scissor='''
    _______
---'_______)
    ________)
    (____)
    (___)
--,(__)

'''

rock='''
    ______
---'(_____)
    (_____)
    (____)
    (___)
--,(__)

'''

paper='''
    _____
---'_____)
    ______)
    _______)
    _____)
--,____)

'''
game_image=[rock,paper,scissor]
user_input=int(input("Enter input here: 0 for rock,1 for paper,2 for scissor,"))
if user_input >=3 or user_input < 0:
    print("Not valid try again")
else:
    print(game_image[user_input])
    computer_input=random.randint(0,2)
    print("computer_choose:")
    print(game_image[computer_input])
    if computer_input == user_input:
        print("It's a tie")
    elif user_input==0 and computer_input==2:
        print("you win")
    elif user_input==2 and computer_input==0:
        print("you lose")
    elif computer_input > user_input:
        print("you lose")
    elif user_input > computer_input:
        print("you win")
    



