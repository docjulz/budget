# This program displays the Shift Supervisors
# yearly salary and bonus based on sales quota

# This class is for all employees
class Employee:
    def __init__(self, name, number):
        self.__name = name
        self.__number = number

    # These are the mutators for the Employee data attribute.
    def set_name(self, name):
        self.__name = name

    def set_number(self, number):
        self.__number = number

    # These are the accessors for the Employee data attribute.
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

# This class is for the ShiftSupervisor. It
# is a subclass of Employee
class ShiftSupervisor(Employee):

    def __init__(self, name, number, salary, bonus):

        # Calls the superclass
        Employee.__init__(self, name, number)

        self.__salary = salary
        self.__bonus = bonus

    # These are the mutators for the ShiftSupervisor data attribute.
    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    # These are the accessors for the ShiftSupervisor data attribute.
    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus

# The main funciton calls the Employee class and instance
# of Shift Supervisor.
def main():

    # Gets the Name, ID Number, Salary, and Bonus
    # of the ShiftSupervisor.
    name = input("Enter Name: ")
    number = input("Enter number: ")
    salary = float(input("Enter salary: "))
    bonus = float(input("Enter bonus: "))

    # Object for ShiftSupervisor.
    shift_super = ShiftSupervisor(name, number, salary, bonus)

    # Display the ShiftSupervisor data.
    print()
    print("Shift Supervisor Information")
    print('----------------------------')
    print("Name:", shift_super.get_name())
    print("Number:", shift_super.get_number())
    print("Salary $", format(shift_super.get_salary(), ",.2f"),sep='')
    print("Bonus $", format(shift_super.get_bonus(), ",.2f"), sep='')

main()
