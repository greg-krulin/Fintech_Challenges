# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations.

Automate the calculations for the loan portfolio summaries.

First, let's start with some calculations on a list of prices for 5 loans.
    1. Use the `len` function to calculate the total number of loans in the list.
    2. Use the `sum` function to calculate the total of all loans in the list.
    3. Using the sum of all loans and the total number of loans, calculate the average loan price.
    4. Print all calculations with descriptive messages.
"""
loan_costs = [500, 600, 200, 1000, 450]

# How many loans are in the list?
# @TODO: Use the `len` function to calculate the total number of loans in the list.
# Print the number of loans from the list
# YOUR CODE HERE!

number_of_loans = len(loan_costs) # this will take length of list. Count of how many seperate loans.

print(f"The number of loans right now is {number_of_loans}.") #this reports to user how many loans are in the list.

# What is the total of all loans?
# @TODO: Use the `sum` function to calculate the total of all loans in the list.
# Print the total value of the loans
# YOUR CODE HERE!

total_amount_of_loans = sum(loan_costs) #using pre-built python function to sum all loans in list together.

print(f"The total amount of loans is ${total_amount_of_loans}.") #reports to user total amount of loans.

# What is the average loan amount from the list?
# @TODO: Using the sum of all loans and the total number of loans, calculate the average loan price.
# Print the average loan amount
# YOUR CODE HERE!
average_loan_amount = total_amount_of_loans/number_of_loans  #since we saved variables from before can call them down here to calculcate average.

print(f"The average loan amount is ${average_loan_amount}.") #reports to user average of loans.

"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
# Print each variable.
# YOUR CODE HERE!

future_value = loan.get("future_value") #gets dictionary value from key "future_value"

remaining_months = loan.get("remaining_months") #gets dictionary value from key "remaining_months"

print(f"The future value of the loan is ${future_value}.")
print(f"Remaining time left on loan is {remaining_months} months.")
#We report to the user future value of loan and the reamining months of loan. User two seperate print statements to make it easier for user to see each report.

# @TODO: Use the formula for Present Value to calculate a "fair value" of the loan.
# Use a minimum required return of 20% as the discount rate.
#   You'll want to use the **monthly** version of the present value formula.
#   HINT: Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months

# YOUR CODE HERE!

#creating variable for discount rate so that user can change depending on circumstances
discount_rate = .20 #use a var for discount_rate so can change easier if needed.

present_value = future_value/ ( (1 + discount_rate/12) ** (remaining_months) ) #Define present value according to this equation with variables defined as above.



# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# @TODO: Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
#    If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
#    Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.
# YOUR CODE HERE!

if present_value >= loan.get("loan_price"): #This is saying if present_value is greater than or rqual to loan price it is worth buying
    print("The present value of the loan is equal or greater than cost so it is worth buying")

else: #if present value is not >= to loan price, then present value is < loan price so not worth buying
    print("Present value of loan is worth less than the price of loan. Not worth buying.")

"""Part 3: Perform Financial Calculations.

Perform financial calculations using functions.

1. Define a new function that will be used to calculate present value.
    a. This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
    b. The function should return the `present_value` for the loan.
2. Use the function to calculate the present value of the new loan given below.
    a. Use an `annual_discount_rate` of 0.2 for this new loan calculation.
"""

# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# @TODO: Define a new function that will be used to calculate present value.
#    This function should include parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
# YOUR CODE HERE!

#created function to calculate present value so won't need to repeat code if another calculation is required.
def present_value_calc( future_value_a, discount_rate_b, remaining_months_c):
    return future_value_a / ( (1 + discount_rate_b/12) ** (remaining_months_c) )

#Function above calculates present value according to three variables.

# @TODO: Use the function to calculate the present value of the new loan given below.
#    Use an `annual_discount_rate` of 0.2 for this new loan calculation.
# YOUR CODE HERE!

#creating variable for discount rate so that user can change depending on circumstances
discount_rate = .20

#Calling present_value_calc to instantiate present_value 
present_value = present_value_calc(new_loan.get("future_value"), discount_rate, new_loan.get("remaining_months"))
#Above we are calling function that calculates present value with the dictionary keys "future_value" and "remaining_months" and variable discount_rate. present_value will equal the return of the function

print(f"The present value of the loan is: ${round(present_value, 2)}") #reports present value to user and rounds to 2nd decimal


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!

inexpensive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!
for loan in loans:
    if loan.get("loan_price") <= 500:
        inexpensive_loans.append(loan)
#The above for loop goes through list of dictionary objects and sees if dictionary value of "loan_price" <= $500. If it is, then we add it to list of inexpensive loans.
# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!

#Can just print the whole list in one print statment with print(inexpensive_loans), however, the below code makes the list more readable for user.
counter = 0
#instantiate counter above to keep track of how many inexpensive loans we have
for loan in inexpensive_loans: #will go through each loan in the list of loans
    counter+=1 #increase counter by one
    print(f"Loan {counter}: {loan}") #prints the count of the loan in the list and the loan itself

"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!

print(f"Writing the list of inexpensive loans to CSV file {output_path}...") #Letting user know we are going to be writing loans to a csv file and to which one.

with open(output_path, 'w', newline='') as csvfile: #using CSV import to be able to open csv_file (if there is not one script will create one with name), with 'w" argument to be able to write on csv file and newline ',' is letting it know comma seperated
    csvwriter = csv.writer(csvfile) #call writer function

    csvwriter.writerow(header) #writes header values on first line of csv

    for loan in inexpensive_loans:
            csvwriter.writerow(loan.values())

            #above for loop goes through each inexpensive loan to write onto csv file.
