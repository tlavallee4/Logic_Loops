
"""
Description: ATM Bank Transaction
Author: Tanelle Lavallee
Date: 02/01/2024

"""

# Declaring variables and importing 

import random 
import os
from time import sleep
selection = {"D", "W", "Q"}
D = "Deposit"
W = "Withdraw"
Q = "Quit"
balance = random.randint(-1000,10000)

# Creating the interface display
fill_space = ' '
line = '*' * 40
width = 40
line_1 = 'PIXELL RIVER FINANCIAL'
centered_line_1 = line_1.center(width, fill_space)
line_2 = 'ATM Simulator'
centered_line_2 = line_2.center(width, fill_space)
line_3 = 'Your current balance is: ' + f"${balance:,.2f}"
centered_line_3 = line_3.center(width, fill_space)
line_4 = 'Deposit: D'
centered_line_4 = line_4.center(width, fill_space)
line_5 = 'Withdraw: W'
centered_line_5 = line_5.center(width, fill_space)
line_6 = 'Quit: Q'
centered_line_6 = line_6.center(width, fill_space)

while True:
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

# Incorporate Transactions 
    selection = input("Enter your selection: ")
    capitalized_selection = selection.capitalize()

# Defining invalid lines
    invalid_line = 'INVALID SELECTION'
    insufficient_line = 'INSUFFICIENT FUNDS'
    centered_invalid_line = invalid_line.center(width, fill_space)
    centered_insufficient_line = insufficient_line.center(width, fill_space)

# Creating ATM transaction selections D, W, Q
    if capitalized_selection == 'D':
        transaction = float(input("Enter your amount of transaction: "))
        current_balance = transaction + balance
        line_7 =  'Your current balance is: ' + f"${current_balance:,.2f}"
        centered_line_7 = line_7.center(width, fill_space)
        print(line + "\n" 
        + centered_line_7 +"\n"
        + line)
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    elif capitalized_selection == 'W':
        transaction = float(input("Enter your amount of transaction: "))
        if transaction > balance : 
            print(line + "\n" 
            + centered_insufficient_line +"\n"
            + line)
            sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif transaction <= balance :
            current_balance = balance - transaction
            line_7 =  'Your current balance is: ' + f"${current_balance:,.2f}"
            centered_line_7 = line_7.center(width, fill_space)
            print(line + "\n" 
            + centered_line_7 +"\n"
            + line)
            sleep(3)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
    elif capitalized_selection == "Q":
        centered_quit_line = Q.center(width, fill_space)
        print(line + "\n"
        + centered_quit_line + "\n"
        + line)
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else: 
        print(line + "\n"
        + centered_invalid_line + "\n"
        + line
        )
        sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        continue

    