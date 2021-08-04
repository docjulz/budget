# Stadium Seating
# This program will calculate the total sales
# for each seat section

# Assign Constants	
CLASS_A = 20
CLASS_B = 15
CLASS_C = 10

# Main will call the seat and total function
def main():
    # Get seats for each seating class section
    seat_A = get_seats1 ()
    seat_B = get_seats2 ()
    seat_C = get_seats3 ()

    # Calculate total number of seats sold in each section
    total = total_sales (seat_A, seat_B, seat_C)
    print("Total income from tickets sold $", format(total, ',.2f'), sep='')

# Formula for the number of seats purchased in each section	
def get_seats1():
    seat_A = int(input("How many tickets sold for Class A? "))
    while seat_A < 0:
        print("You will need to enter a seat number above \"0\".")
        seat_A = int(input("Please enter the number again for Class A: "))
    return seat_A

def get_seats2():
    seat_B = int(input("How many tickets sold for Class B? "))
    while seat_B < 0:
        print("You will need to enter a seat number above \"0\".")
        seat_B = int(input("Please enter the number again for Class B: "))
    return seat_B

def get_seats3():
    seat_C = int(input("how many tickets sold for Class C? "))
    while seat_C < 0:
        print("You will need to enter a seat number above \"0\".")
        seat_C = int(input("Please enter the number again for Class C: "))
    return seat_C

# Calculate the number of seats sold per Class
def total_sales(seat_A, seat_B, seat_C):
    total = (seat_A*CLASS_A) + (seat_B * CLASS_B) + (seat_C * CLASS_C)
    return total

main()
