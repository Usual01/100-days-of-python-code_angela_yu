"""
creates and compares secret bid
"""

my_bids = {}
bidds = True
def highest_bids(bidders_h_all):
    bidders_high = 0
    winner = ""
    for b in bidders_h_all:
        bid_amount = bidders_h_all[b]
        if bid_amount > bidders_high:
            bidders_high = bid_amount
            winner = b
    print(f"the winner is {winner} with ${bidders_high}")
while bidds:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?\n"))
    my_bids[name] = bid
    bidding_finished = input("Any more bids, type yes or no")
    if bidding_finished == "no":
        bidds = False
        highest_bids(my_bids)
    