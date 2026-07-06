#!/usr/bin/env python3
#   FILE    employee_program.py
#   DATE    2025-09-22 (ISO-8601 format )
#   AUTHOR  Chris Bofole
#   DESCRIPTION
"""
This is the employee program that will let the user work with 
employee records.

MOD DATE:   2025-11-05
MOD BY:     Chris Bofole
MOD DESCRIPTION:
    Added a loop to the menu.

MOD DATE:   2025-11-5
MOD BY:     Chris bofole
MOD DESCRIPTION:
    Add command line arguments and split the program into functions.

MOD DATE:   2025-11-5
MOD BY:     Chris bofole
MOD DESCRIPTION:
    Split the functions into separate modules.
"""

import sys

import employee_handler
import ui_helper

VERSION = "1.0.5"
""" The current version of the program.  """

def main(argv: list):
    """
    Check the command line arguments to see what the user wishes to do.

    INPUTS:
        argv A list of command line arguments
    """
    # print(argv)
    if len(argv) == 1:
        do_program_logic()
    elif len(argv) == 2:
        if argv[1] == "--version" or argv[1] == "-v":
            show_version()
        elif argv[1] == "--help" or argv[1] == "-h" or argv[1] == "-?":
            show_help()
        else:
            show_error(f"Invalid command line argument: {argv[1]}")
    else:
        show_error(f"Invalid number of command line arguments: {argv}")

###############################################################################
#
#   Functions for responding to command line arguments
#
###############################################################################

def show_error(message: str):
    """
    Display an error message, the show help, and exit the program with error 
    code.
    """
    ui_helper.show_message(f"\nERROR: {message}")
    show_help()
    sys.exit(1)

def show_help():
    """
    Display the standard usage for the program.
    """
    ui_helper.show_message("\nUSAGE:")
    ui_helper.show_message("python employee_program.py")
    ui_helper.show_message("python employee_program.py [-? | -h | --help]")
    ui_helper.show_message("python employee_program.py [-v | --version]")

def show_version():
    """
    Display the current version number
    """
    ui_helper.show_message(f'Employee Program {VERSION}')



def do_program_logic():
    """
    Display a menu of options, get the user's choice, and display 
    a related message.
    """
    program_title = "*** EMPLOYEE PROGRAM ***"
    ui_helper.show_program_title(program_title)
    invalid_choice_message = "Your choice was not recognized.  Please try again."
    # Print the menu title and its options
    done = False
    while not done:
        # Prompt the user for a choice and get that choice
        user_choice = get_user_choice()
        # Decide what to do based on the user's choice
        if user_choice == "1":
            employee_handler.handle_add_employee()
        elif user_choice == "2":
            employee_handler.handle_show_all_employees()
        elif user_choice == "3":
            employee_handler.handle_view_employee()
        elif user_choice == "4":
            employee_handler.handle_update_employee()
        elif user_choice == "5":
            employee_handler.handle_delete_employee()
        elif user_choice == "X" or user_choice == "x":
            done = confirm_quit()
            ui_helper.press_enter_key_to_continue()
        else:
            ui_helper.show_message(invalid_choice_message)
            ui_helper.press_enter_key_to_continue()
    # Tell the user the program is complete
    ui_helper.show_message("\nProgram complete.")

def confirm_quit()->bool:
    """
    Asks the user if they wish to actually quit.  Returns True if they yes and
    False otherwise.

    RETURNS:
        bool An answer to whether they want to quit.
    """
    ui_helper.show_message("\nYou chose to quit the program.")
    prompt = "Confirm quit (Y/N) "
    choice = ui_helper.get_user_string(prompt)
    return (choice == "Y" or choice == "y")

def get_user_choice()->str:
    """
    Displays a menu and prompts the user for a choice.

    RETURNS:
        string The string entered by the user
    """
    menu_title = "Main Menu"
    prompt = "Your choice: "
    options = ["1) Add an Employee","2) Show All Employees"
               ,"3) View an Employee","4) Update an Employee"
               ,"5) Delete an Employee","X) Exit"]
    ui_helper.show_menu(menu_title, options)
    return ui_helper.get_user_string(prompt)


###############################################################################
#
#   Call main()
#
###############################################################################
if __name__ == "__main__":
    main(sys.argv)
    