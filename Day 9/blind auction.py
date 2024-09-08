from art import logo

def find_winner(bidding):
    highest_bid = 0
    winner = ''

    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of ${highest_bid}')

lances = True
compradores = {}
print(logo)

while lances:
    name = input('What is your name?: ')
    bid = int(input('What is your bid?: '))
    compradores[name] = bid
    cont = input("Are there any other bidders? Type 'yes' or 'no'.")
    if cont == 'yes':
        lances = True
    elif cont  == 'no':
        lances = False
        find_winner(compradores)
