import os

def clear():

    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')




dic_bid = {"names": [],
           "bids": []}
Q3 = "yes"
while Q3 == "yes":

  Q1= input("What is your name? ")
  Q2= input("What is your bid? ")
  Q3= input("Are there any other bidders? type yes or no. ").lower()

  dic_bid["names"].append(Q1)
  dic_bid["bids"].append(Q2)
  if Q3 == "yes":
    clear()

winner_bid = max(dic_bid["bids"])


winner = dic_bid["names"][dic_bid["bids"].index(max(dic_bid["bids"]))]
print(f"{winner} won the with bid {winner_bid}.")
