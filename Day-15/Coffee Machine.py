MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coffe_request = input('What would you like? (espresso/latte/cappuccino): ').lower()

while coffe_request != "off":

    if coffe_request == 'report':
        print(resources)

    request = MENU[coffe_request]
    ingredients = request['ingredients']

    for a in ingredients:
        if ingredients[a] > resources[a]:
            print(f'Sorry there is not enough {a}.')
            coffe_request = 'off'

    if coffe_request != 'off' and coffe_request != 'report':
        quarters = int(input('insert quarters($0.25) coins: '))
        dimes = int(input('insert dimes($0.10) coins: '))
        nickles = int(input('insert nickles($0.05) coins: '))
        pennies = int(input('insert pennies($0.01) coins: '))
        coins_insert = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)
        print(f'${round(coins_insert, 2)}')

        if coins_insert < request['cost']:
            print("Sorry that's not enough money. Money refunded.")
            coins_insert = 0
        else:
            resources['Money'] = request['cost']
            if coins_insert > request['cost']:
                print(f'Here is ${round(coins_insert - request['cost'], 2)} dollars in change.')

            print(resources)
            for a in ingredients:
                resources[a] = resources[a] - ingredients[a]
            print(resources)
            print(f'Here is your {coffe_request}. Enjoy')

    coffe_request = input('What would you like? (espresso/latte/cappuccino): ').lower()