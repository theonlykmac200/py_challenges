# 1. Create a simple calculator that first asks the user what operation they would like to use (addition, subtraction, multiplication, division) and then asks the user for two numbers, returning the result of the operation with the two numbers.

#start with the functions to define the math operations
def addition(a,b):
    return a + b

def subtraction(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a,b):
    return a / b

#Make the calculator function

question=input("What operation would you like to use? (addition, subtraction, multiplication, division)")

def calculator():
    a = int(input("What is the first number?"))
    b = int(input("what is the second number?"))
    if question == "addition":
        print(addition(a,b))
    elif question == "subtraction":
        print(subtraction(a,b))
    elif question == "multiplication":
        print(multiplication(a,b))
    elif question == "division":
        print(division(a,b))
    else:
        print("please re-read the questions and try again")


#Reverse a string manually. Create a new variable storing an empty string and add the letters from the first string one by one. The for loop should iterate over the length of the string and you should access letters individually.

#start with the string
switch = input("What string would you like to reverse?")

#make the function

def reverse_string():
    new_string = ""
    for i in range(len(switch)):
        new_string += switch[-i-1]
    print(new_string)

reverse_string()


# Create a prompt that asks the user if they would like to display their balance, withdraw or deposit. Write three funtions to perform these calculations and output the result to the user. Here is a sample output:
account = {
    "name": "John Doe",
    "account_number": 123456789,
    "balance": 1000
}

def display_balance():
    print(f"Your balance is ${account['balance']}.")

def withdraw():
    withdraw = int(input("How much would you like to withdraw?"))
    balance = account["balance"] - withdraw
    account["balance"] = balance
    print(f"You have withdrawn ${withdraw}, Your new balance is ${account['balance']}.")

def deposit():
    deposit = int(input("How much would you like to deposit?"))
    balance = account["balance"] + deposit
    account["balance"] = balance
    print(f"You have deposited ${deposit}, Your new balance is ${account['balance']}.")


def bank():
    question = input("What would you like to do? (display_balance, withdraw, deposit)")
    if question == "display_balance":
        display_balance()
    elif question == "withdraw":
        withdraw()
    elif question == "deposit":
        deposit()
    else:
        print("Please re-read the questions and try again.")

bank()