
"""
Description: Adding Interest
Author: Tanelle Lavallee
Date: 02/01/2024

"""
from pprint import pprint

data = {}
with open("account_balances.txt", "r") as file:
   for line in file:
    account_number, account_balance = line.split("|")
    data[account_number] = float(account_balance)
print(data)
pprint(data)


for i in data.values():
   if i > 5000:
    i = i + ((i * .05) / 12)
    print(i)
    if i < -1:
        i = i + ((i * .10) / 12)
        print(i)


file = open("updated_balances_TL.csv", "w")
file.write("## Account" "\n" "## Balance")
file.write(f"{i}")
file = open("updated_balances_TL.csv", "r")
print(file.read())

