
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


# in data: 
 #   print(data)
  
  #if balance > 0 and key < 1000: 
    #if  data[key] > 0 and data[key] < 1000:
        #interest = .01
    #elif data[key] >= 1000 and data[key] < 5000:
        #interest = .025
    #elif data[key] >= 5000:
        #interest = .05
    #elif data[key] < 0:
        #interest = .10

