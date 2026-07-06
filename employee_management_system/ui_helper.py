#!/usr/bin/env python3
#   FILE    ui_helper.py
#   DATE    2025-10-15 (ISO-8601 format)
#   AUTHOR  Chris bofole
#   DESCRIPTION
"""
This module contains functions for interacting with the user.
"""

CONSOLE_WIDTH = 80
""" The width of the console in characters."""


###############################################################################
#
#   Functions for general user interaction
#
###############################################################################

def show_program_title(program_title:str):
    """
    Displays a program title in a consistent manner.

    INPUTS: 
        program_title A string with the title to display
    """
    print(f"\n{program_title:^{CONSOLE_WIDTH}}\n")

def show_section_title(title:str):
    """
    Displays a section title in a consistent manner.

    INPUTS:
        title A string with the title to display
    """
    print(f"\n\t-- {title} --")


def show_message(message: str):
    """
    Displays a message in a consistent manner.

    INPUTS:
        message The message to display
    """
    print(message)


def get_user_string(prompt: str)->str:
    """
    Prompt the user for a string and return what they enter.

    INPUTS:
        prompt A string with instructions for the user
    
    RETURNS:
        string The string entered by the user
    """
    return input(prompt + " ").strip()

def get_user_int(prompt:str)->int:
    """
    Prompt the user for an int and return what they enter.

    INPUTS:
        prompt A string with instructions for the user
    
    RETURNS:
        int The int entered by the user
    """
    value = 0
    needed = True
    while needed:
        user_input = input(prompt + " ")
        try:
            value = int(user_input)
            needed = False
        except:
            print("That was not a whole number. Try again.")
            press_enter_key_to_continue()
    return value

def get_user_positive_int(prompt:str)->int:
    """
    Prompt the user for an int and return what they enter.

    INPUTS:
        prompt A string with instructions for the user
    
    RETURNS:
        int The int entered by the user
    """
    value = 0
    needed = True
    while needed:
        value = get_user_int(prompt )
    
        if value >= 0:
            needed = False
        else:
    
            print("Value must be greater than or equal to zero. Try again.")
            press_enter_key_to_continue()
    return value


def get_user_float(prompt:str)->float:
    """
    Prompt the user for a float and return what they enter.

    INPUTS:
        prompt A string with instructions for the user
    
    RETURNS:
        float The float entered by the user
    """
    value = 0.0
    needed = True
    while needed:
        user_input = input(prompt + " ")
        try:
            value = float(user_input)
            needed = False
        except:
            print("That was not a whole number. Try again.")
            press_enter_key_to_continue()
    return value

def get_user_cancelable_float(prompt:str)->float:
    """
    Prompt the user for a float and return what they enter.

    INPUTS:
        prompt A string with instructions for the user
    
    RETURNS:
        float The float entered by the user
    """
    value = 0.0
    needed = True
    while needed:
        user_input = input(prompt + " ")
        if user_input == "": # Just hit enter with no value
            raise ValueError("Canceled") # outside the try/except structure
        try:
            value = float(user_input)
            needed = False
        except:
            print("That was not a whole number. Try again.")
            press_enter_key_to_continue()
    return value




def press_enter_key_to_continue():
    """
    Prompt the user to press the Enter key and wait until they do.
    """
    input("\nPress the Enter key to continue... ")


###############################################################################
#
#   Functions for menus
#
###############################################################################

def show_menu(menu_title:str, options:list):
    """
    Displays the menu.

    INPUTS:
        menu_title A string with the title of the menu
        options A list strings represent the menu options
    """
    print(f"\n\n\t-- {menu_title} --")
    for option in options:
        print(f"\t{option}")



###############################################################################
#
#   Functions for tables
#
###############################################################################

def draw_table(column_defs: list, headers: list, data: list):
    """
    Draws a text-based table with the data provided.

    NOTE: All the lists in the parameters must be the same length.

    INPUTS:
        column_defs A list of tuples with column widths and alignment
        headers A list of strings with the column headers
        data A list of lists where each sublist is a record
    """
    # determine the width of the table
    bar_size = 0
    for col in column_defs:
        bar_size += col[0]
    bar_size += len(headers) + 1 # for the vertical bars
    # draw the top bar
    print("")
    draw_bar(bar_size, "-")
    # Draw the header row
    print("|", end="")
    for i in range(len(column_defs)):
        draw_column(column_defs[i][0], headers[i], "center")
        print("|", end="")
    print("")
    draw_bar(bar_size, "-")
    # draw the table data
    for datum in data:
        print("|", end="")
        for i in range(len(datum)):
            draw_column(column_defs[i][0], datum[i], column_defs[i][1])
            print("|", end="")
        print("")
        draw_bar(bar_size, "-")

def draw_column(width:int, value:any, direction:str):
    """
    Builds a string for the column and prints it without a newline.

    INPUTS:
        width The width of the column in characters
        value The item to be displayed
        direction The alignment
    """
    if direction == "center":
        align = "^"
    elif direction == "right":
        align = ">"
    else:
        align = "<"
    # build the string
    out = f"{value:{align}{width}}"
    # display the output
    print(out, end="")




def draw_bar(bar_size:int, bar_character:str)->str:
    """
    Displays a horizontal line of the specified character.

    INPUTS:
        bar_size The width of the line in characters
        bar_character The character to use for the bar
    """
    bar = bar_character * bar_size
    print(bar)




