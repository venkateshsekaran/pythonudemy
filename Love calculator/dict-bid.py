from os import system
bids={}
bids_finished=False

def highest_bids(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
           highest_bid = bid_amount
           winner=bidder
    print(f"The winner is {winner} with the bid of {highest_bid}")       
while not bids_finished:
   name=input("What is your name?: ")
   price=int(input("What is your bidding price?: $"))
   bids[name]=price
   bids_more=input('Any other bid? Type "yes" or "no"')
   if bids_more== "no":
       bids_finished=True
       highest_bids(bids)
   elif bids_more== "yes":
        _ = system('cls')
   