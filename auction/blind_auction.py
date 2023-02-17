from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.


def find_highest_bidder(bids_dictionary):
  winner = ''
  winning_bid = 0
  for key in bids_dictionary:
    if bids_dictionary[key] > winning_bid:
      winner = key
      winning_bid = bids_dictionary[key]
      print(winning_bid)
 
  print(f"The winner is {winner} with a bid of ${winning_bid}")  

def blind_auction():

  print(logo)
  
  answer = True
  auction_dictionary = {}
  
  while answer == True:
    name = input("What is your name: ")
    bid = float(input("What is your bid: $"))
    auction_dictionary[name] = bid
    add_more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  
    if add_more_bidders == "yes":
      clear()
    else:
      answer = False
      clear()
      find_highest_bidder(auction_dictionary)


blind_auction()