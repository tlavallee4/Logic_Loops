
"""
Description: Adding Interest
Author: Tanelle Lavallee
Date: 02/01/2024

"""
from pprint import pprint
data = {}
with open("account_balances.txt", "r") as file:
   for line in file:
    number, balance = line.split("|")
    data[number] = float(balance)
    
print(data)
pprint(data)
