import os


def clear():
    os.system('clear')


from art import logo

print(logo)
print("Welcome to Bid World! Whoever is the highest bidder will win!")
# set empty dictionary
bids = {}
# create function for highest bidder
continue_bid = False


def highest_bidder(bidding_record):
    # set bid to 0 first
    highest_bid = 0
    # set empty string for winner
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not continue_bid:
    name = input("What is your name? \n")
    bid_amount = float(input("What is your bid price? $"))
    bids[name] = bid_amount
    other_name = input("Is there other bidder? 'Yes' or 'No'\n").lower()
    if other_name == 'no':
        continue_bid = True
        highest_bidder(bids)
    elif other_name == 'yes':
        clear()
