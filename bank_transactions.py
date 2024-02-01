
"""
Description: ATM Bank Transaction
Author: Tanelle Lavallee
Date: 02/01/2024

"""

import random 
D = "Deposit"
W = "Withdraw"
Q = "Quit"

balance = random.randint(-1000,10000)
balance = f"${balance:,.2f}"
string_balance = str(balance)


## print(f"${random.randint(-1000,10000):,.2f}")
## convert to dollar by 2 decimal place 
## print(f"${balance:,.2f}")

fill_space = ' '
line = '*' * 40
width = 40
line_1 = 'PIXELL RIVER FINANCIAL'
centered_line_1 = line_1.center(width, fill_space)
line_2 = 'ATM Simulator'
centered_line_2 = line_2.center(width, fill_space)
line_3 = 'Your current balance is: ' + string_balance
centered_line_3 = line_3.center(width, fill_space)
line_4 = 'Deposit: D'
centered_line_4 = line_4.center(width, fill_space)
line_5 = 'Withdraw: W'
centered_line_5 = line_5.center(width, fill_space)
line_6 = 'Quit: Q'
centered_line_6 = line_6.center(width, fill_space)

print(line + "\n"
    + centered_line_1 + "\n" 
    + centered_line_2 + "\n"
    + centered_line_3 + "\n"
    + fill_space + "\n"
    + centered_line_4 + "\n"
    + centered_line_5 + "\n"
    + centered_line_6 + "\n"
    + line
    )
    
    