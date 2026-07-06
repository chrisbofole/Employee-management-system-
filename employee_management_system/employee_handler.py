#!/usr/bin/env python3
#   FILE    employee_handler.py
#   DATE    2025-10-15 (ISO-8601 format)
#   AUTHOR  Chris bofole
#   DESCRIPTION
"""
This module contains functions for working with employee records.


MOD DATE:   2025-10-29
MOD BY:     Chris Bofole
MOD DESCRIPTION:
    Implement logic for handle_add_employee() and handle_show_all_employees().

"""

import employee_store
import employee_ui
import ui_helper

def handle_add_employee():
    """
    Handles the choice to add an employee.
    """
    ui_helper.show_section_title("Add an Employee")
    employee = employee_ui.get_employee_data()
    try:
        
      employee_store.store_employee(employee)
      ui_helper.show_message("\nEmployee record stored.")
    except IOError as err:
        ui_helper.show_message(f"\nERROR: There was error saving: {str(err)}.\n")
    ui_helper.press_enter_key_to_continue()

def handle_show_all_employees():
    """
    Handles the choice to show all employees.
    """
    ui_helper.show_section_title("Show All Employees")
    try:
            
        employees = employee_store.get_employee_list()
        if len(employees) == 0: # empty
            ui_helper.show_message("\nThere are no employee records to show.")
        else:
            employee_ui.show_employee_table(employees)
    except Exception as err:
        ui_helper.show_message(f"\nThere was an error reading records: {str(err)}.\n")
    ui_helper.press_enter_key_to_continue()

def handle_view_employee():
    """
    Handles the choice to view an employee.
    """
    ui_helper.show_section_title("View an Employee")
    try:
            
        found = get_an_employee()
        id = found[0]
        employee = found[1]
        if len(employee) == 0:
            ui_helper.show_message(f"nThere were no employee with ID{id}.")
        else:
            employee_ui.show_single_employee(employee)
    except Exception as err:
        ui_helper.show_message(f"\nThere was an error reading record: {str(err)}.\n")     
    ui_helper.press_enter_key_to_continue()

def handle_update_employee():
    """
    Handles the choice to update an employee.
    """
    ui_helper.show_section_title("Update an Employee")
    try:
        found = get_an_employee()
        id = found[0]
        employee = found[1]
        if len(employee) == 0:
            ui_helper.show_message(f"nThere were no employee with ID{id}.")
        else:
            updated = employee_ui.get_updated_employee_data(employee)
            if employee_store.update_employee_by_id(updated):
                ui_helper.show_message(f"\nupdated employee with ID: {id}")
            else:
                ui_helper.show_message(f"\ncould not update employee with ID: {id}")
    except Exception as err:
        ui_helper.show_message(f"\nThere was an error reading record: {str(err)}.\n")    
    ui_helper.press_enter_key_to_continue()

def handle_delete_employee():
    """
    Handles the choice to delete an employee.
    """
    ui_helper.show_section_title("Delete an Employee")
    try:
        found = get_an_employee()
        id = found[0]
        employee = found[1]
        if len(employee) == 0:
            ui_helper.show_message(f"nThere were no employee with ID{id}.")
        else:
            if employee_store.remove_employee_by_id(id):
                ui_helper.show_message(f"\nDelete employee ID: {id}")
            else:
                ui_helper.show_message(f"nCould not delete the employee with ID: {id}")
    except Exception as err:
        ui_helper.show_message(f"\nThere was an error reading record: {str(err)}.\n")
    ui_helper.press_enter_key_to_continue()




def get_an_employee()-> list:
    """ ask the user for the employee ID and attempts to find an employee with
    the matching ID. It returns a list containing the entered ID and the found employee.
    If no employee matched, the found employee list will be an empty list
    RETURNS:
        list A list entered ID and the found employee
    RAISES:
        FileNotfoundError
        ValueError
        """
        
 # get the employee ID from the user
    id = employee_ui.get_employee_id()
# Try to get an employee record
    found = employee_store.get_employee_by_id(id)
# Return a list with id and found
    return[id, found]
    
