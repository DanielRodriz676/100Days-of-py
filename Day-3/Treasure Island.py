print('Welcome to Treasure Island.\nYour mission is to find the treasure.')

if input('left or right? ') == 'left':
    if input('swim or wait? ') == 'wait':
        door = input('Which door?(red), (blue), (yellow) ')
        if door == 'red':
            print('Burned by fire.\nGame Over.')
        elif door == 'blue':
            print('Eaten by beasts.\nGame Over.')
        elif door == 'yellow':
            print('You Win!')
        else:
            print('Game Over')
    else:
        print('Game Over')
else:
    print('Game Over')