
"""
Description: Adding Interest
Author: Tanelle Lavallee
Date: 02/01/2024

"""
# import section
from pprint import pprint
import csv


# opening the text file and creating a dictionary from it's contents
data = {}
with open("account_balances.txt", "r") as file:
   for line in file:
    account_number, account_balance = line.split("|")
    data[account_number] = float(account_balance)
# showing the difference in pretty print and print
print(data)
pprint(data)

# stating interest amounts per account balance amount
for account_number, account_balance in data.items():
    if account_balance >= 5000:
        interest = .05
    elif account_balance < 5000 and account_balance >= 1000:
        interest = .025
    elif account_balance < 1000 and account_balance > 0:
        interest = .01
    elif account_balance < -1:
        interest = .10

# updating account balances to include interest
    balance = account_balance + ((account_balance * interest) / 12)
    data[account_number] = balance
pprint(data)
    

# writing and updating a csv file to include an organized account & balance file
# creating headers
headers = ['Account','Balance']

with open('updated_balances_TL.csv', 'w', newline='') as file:
    writer = csv.writer(file)
# adding headers to file, adding account number and balances to file
    writer.writerow(headers)
    writer.writerows(data.items())


