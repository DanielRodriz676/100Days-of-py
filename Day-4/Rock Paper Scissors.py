from random import choice
rps = [
    "    _______\n"
    "---'   ____)\n"
    "      (_____)\n"
    "      (_____)\n"
    "      (____)\n"
    "---.__(___)",
    "    _______\n"
    "---'   ____)____\n"
    "          ______)\n"
    "          _______)\n"
    "         _______)\n"
    "---.__________)",
    "    _______\n"
    "---'   ____)____\n"
    "          ______)\n"
    "       __________)\n"
    "      (____)\n"
    "---.__(___)"
]

your_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. '))
print(rps[your_choice])

comp_choice = choice(rps)
print('Computer chose:')
print(comp_choice)

if rps[your_choice] == comp_choice:
    print("It's a draw")
else:
    if your_choice == 0:
        if comp_choice == rps[1]:
            print('You lose')
        else:
            print('You win')
    elif your_choice == 1:
        if comp_choice == rps[2]:
            print('You lose')
        else:
            print('You win')
    elif your_choice == 2:
        if comp_choice == rps[0]:
            print('You lose')
        else:
            print('You win')


