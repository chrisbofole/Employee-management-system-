#!/usr/bin/env python3
#   file employee.program_4.py
#   date : 2026-07-06
#   author: Chris bofole
#DESCRIPTION
"""
This is the employee program that will let the user work with
employee records.
"""
VERSION = "1.0.2"
""" The current version in of the program. """
CONSOLE_WIDTH = 80
""" The width of the console in characters. """
def main():
    """
    Display a menu of options, get the user's choice, and display
    a related message.
    """
    program_title = "*** EMPLOYEE PROGRAM ***"
    print(f"\n{program_title:^{CONSOLE_WIDTH}}\n")
    # print the menu title and its options
    print("\t-- Main Menu --")
    print("\t1) add an Employee")
    print("\t2) show all Employees")
    print("\t3)  View an Employee")
    print("\t4) update an Employee")
    print("\t5) Delete an Employee")
    print("\tx) Exit")
    # prompt the user for a choice and get that choice
    prompt = "\nYour choice: "
    user_choice = input(prompt)
    # Decide waht to do based on the user's choice 
    if user_choice == "1":
        print("You chose to add an Amployee.")
    elif user_choice == "2":
        print("You chose to show All Employees")
    elif user_choice == "3":
        print("You chose to View an Employee")
    elif user_choice == "4":
        print("You chose to update an Employee")
    elif user_choice == "5":
        print("You chose to Delete an Employee")
    elif user_choice == "X" or user_choice == "X":
        print("You chose to exit.")
    else:
        print(" I didn't understand that option. please try again.")
    # Wait for the user to acknowledge
    input("\nPress the enter key to continue: ")
    # Inputs
    # proces
    # outputs
    # Tell the user the program is complete
    print("\nprogram complete.")
    

if __name__ == "__main__":
    main()
    
    