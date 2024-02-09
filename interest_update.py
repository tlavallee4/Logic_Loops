
"""
Description: Adding Interest
Author: Tanelle Lavallee
Date: 02/01/2024

"""
# Pretty printing account_balances.txt file in a dictionary
from pprint import pprint

data = {}
with open("account_balances.txt", "r") as file:
   for line in file:
    account_number, account_balance = line.split("|")
    data[account_number] = float(account_balance)
print(data)
pprint(data)

# Changing values in the dictionary
for i in data.values():
   if i >= 5000:
    i = i + ((i * .05) / 12)
    print(i)
   elif i < 5000 and i >= 1000:
    i = i + ((i * .025) / 12)
   elif i < 1000 and i > 0:
    i = i + ((i * .01) / 12)
    if i < -1:
        i = i + ((i * .10) / 12)
        print(i)

# writing and updating a csv file
file = open("updated_balances_TL.csv", "w")
file.write("## Account" "\n" "## Balance")
file.write(f"{i}")
file = open("updated_balances_TL.csv", "r")
print(file.read())

