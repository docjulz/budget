# This program creates a pie chart
# for monthly expenses

# Import matplotlib
import matplotlib.pyplot as plt

def main():

    # Open txt file to read values
    infile = open('monthly_expenses.txt','r')

    # Create an empty expense list
    expense = []

    # Loop through txt file and append values to expense list
    for line in infile:
        amount= int(line)
        expense.append(amount)

    # Display values in the list
    print(expense)
        
    # Assign values to each expense item
    rent = amount
    gas = amount
    food = amount
    clothing = amount
    car_payment = amount
    misc = amount

    # Create amount list to hold each exepnse value
    amount = [rent, gas, food, clothing, car_payment, misc]

    # Label each slice to reflect expense value
    slice_labels = ["Rent", "Gas", "Food", "Clothing", "Car Payment", "Misc"]

    # Assign values to pie chart
    plt.pie(expense, labels = slice_labels)

    # Label pie chart
    plt.title("Monthly Expenses")

    # Display pie chart
    plt.show ()

    # Close txt file
    infile.close()

main()

