print("Welcome to he secret auction program")
bids = {}
game = True

def checker(bidding_records):
    top_bid = 0
    winner = ''
    for bidder in bidding_records:
        bidding_amount = bidding_records[bidder]
        if bidding_amount > top_bid:
            top_bid = bidding_amount
            winner = bidder
        print(f'The winner {winner} with a bid of ${top_bid}')

while game:
    bidder_name = input("what is your name")
    bidding_amount = int(input("What is your bid?"))
    bids[bidder_name] = bidding_amount
    hould = input("new bids").lower()
    if hould == "no":
        game = False
        checker(bids)
    
        
    
print(bids)