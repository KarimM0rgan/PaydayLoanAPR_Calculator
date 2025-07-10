# Description: This program calculates the Annual Percentage Rate (APR) for payday loans. It can calculate APR following two scenarios based on the input details the user has

# Instructions to the user
print("Welcome to the payday loan APR calculator.")
print("Please have the proposed terms of your payday loan handy so we can calculate the APR.")
print("Select which one best fits your situation.\n1. I know the total loan amount, the finance charge, and the repayment period (in days or months).\n2. I know the fee in dollars for every 100 dollars borrowed and the repayment period (in days or months).")

# Constants
days_per_year = 365   # Number of days in a year
months_per_year = 12  # Number of months in a year

# Defining the function to undergo the first scenario
def scenario1():
    # Input values of the user 
    loan = float(input("What is the total loan amount?"))
    fcharge = float(input("What is the total finance charge?"))

    # Input function to ask whether the repayment period is in days or months
    DorM = str(input("Is the length of the repayment period in days or months? Enter d or m:"))

    # APR for a repayment period in days
    if DorM == "d":
        period = float(input("How many days is the repayment period?"))
        APR = (fcharge/loan)*(days_per_year/period)*100  # APR calculation formula in first scenario for days
        print("Your", period, "day loan has an APR of", format(APR, ".2f"), "%")  # the result

    # APR for a repayment period in months
    else:
        period = float(input("How many months is the repayment period?"))
        APR = (fcharge/loan)*(months_per_year/period)*100  # APR calculation formula in first scenario for months
        print("Your", period, "month loan has an APR of", format(APR, ".2f"), "%")  # the result

# Defining the function to undergo the second scenario
def scenario2():
    # The user's fee per $100 borrowed
    fee = float(input("What is the fee for each $100 borrowed?"))

    # Input function to ask whether the repayment period is in days or months
    DorM = str(input("Is the length of the repayment period in days or months? Enter d or m:"))

    # APR for a repayment period in days
    if DorM == "d":
        period = float(input("How many days is the repayment period?"))
        APR = fee * (days_per_year/period)  # APR calculation formula in second scenario for days
        print("Your", period, "day loan has an APR of", format(APR, ".2f"), "%")  # the result

    # Calculate APR for a repayment period in months
    else:
        period = float(input("How many months is the repayment period?"))
        APR = fee * (months_per_year/period)  # APR calculation formula in second scenario for months
        print("Your", period, "month loan has an APR of", format(APR, ".2f"), "%")  # the result

# Input function that asks the user to select which scenario works for their situation according to the data they have
path = int(input("How was the information given to you? Choose (1) or (2):"))

# Call the appropriate function based on the user's selection
if path == 1:
    scenario1()  # If the user knows the total loan amount and finance charge
else:
    scenario2()  # If the user knows the fee for each $100 borrowed