#   FILE:   employee_program.py
#   VERSION:    2.0
#   DATE:   2021-04-04 -- Use ISO-8601 date format YYYY-MM-DD
#   AUTHOR: Bob Trapp -- use the student's name
#   VERSION:    1.0.2
#   DESCRIPTION:
"""
This is the second lab for the employee program example.  The
employee program example will grow and change as new concepts are 
added throughout the semester.

The full program at the end of semester will have a menu as its 
primary control state.  This program displays a menu, asks the 
user for a choice, and then displays a message based on the 
choice made by the user.

Note: Users like to enter numbers for menu options but we aren't 
using the numbers for math.  That means we can read the values
as strings.  This will keep the program from crashing if the 
user enters a non-numeric value.

Note: This program also introduces the "Press Enter to continue... " concept.
This is a good way to get users to stop and read the output before going 
forward (something they are not prone to doing).  To do this, we use the input()
function with a prompt telling them to press Enter.  We ignore anything returned
by the input() function because we are only interested in the fact that the 
user pressed Enter.

"""

# A constant for the number of characters across the console
CONSOLE_WIDTH = 80

#   This part is just to help students plan ahead for the overall program.
#
#   INPUTS
#   menu choice String entered by the user
#
#   PROCESSES
#   Show a program title
#   Show a menu
#   Prompt for the user choice and read that in
#   Show a message based on the user choice
#   Display the outputs
#   Tell the user the program is complete
#
#   OUTPUTS
#   A message describing the user choice
#

def main():
    """ 
        This function will print a menu of options for the user.  Then it will 
        prompt the user for a menu choice.  Using an if-elif-else structure,
        it will print a message related to the user's choice
    """
    program_title = "*** EMPLOYEE PROGRAM ***"
    print(f'\n{program_title:^{CONSOLE_WIDTH}}')
    # Print the menu title and its options
    print('\t-- Main Menu --')
    print('\t1) Add an Employee')
    print('\t2) Show All Employees')
    print('\t3) View an Employee')
    print('\t4) Update an Employee')
    print('\t5) Delete an Employee')
    print('\tQ) Quit')
    # Prompt the user for input
    prompt = '\nYour choice: ' # remember the space at the end
    # Get the user input as a string
    user_choice = input(prompt)
    # Decide what to do based on the input
    if user_choice == '1':
        print('\nYou chose to add a new employee record.')
    elif user_choice == '2':
        print('\nYou chose to view all employee records.')
    elif user_choice == '3':
        print('\nYou chose to view an individual employee record.')
    elif user_choice == '4':
        print('\nYou chose to update (change) an employee record.')
    elif user_choice == '5':
        print('\nYou chose to delete (remove) an employee record.')
    elif user_choice == 'Q' or user_choice == 'q': # check both
        print('\nYou chose to quit the program')
    else:
        print('\nYour choice was not recognized.  Please try again.')
    # Pause before going forward by telling the user to press the Enter key
    # to continue.  Read the input but discard it because we only care that the
    # user pressed the Enter key.  This is a common technique for working with
    # users because it encourages them to read the output before going forward.
    input("\nPress the Enter key to continue... ")
    # Let the use know the program is done
    print("\nProgram complete.\n")


# Call main()
main()

