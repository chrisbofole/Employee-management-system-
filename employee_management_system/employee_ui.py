#!/usr/bin/env python3
#   FILE    employee_ui.py
#   DATE    2025-10-29 (ISO-8601 format)
#   AUTHOR  Chris Bofole
#   DESCRIPTION
"""
This module is for the user interface for employee-specific interactions.

In MVC, this is part of the View.

MOD DATE: 2025-11-05
MOD By: Chris bofole
MOD DESCRIPTION:

        Add get_employee_id(), show_single_employee(),get_updated_employee_data()  
"""

import ui_helper
import employee_store as es

def get_employee_data()->list:
    """
    Ask the user for the data needed for an employee record and return the 
    data as a list.

    The record is:
        employee id, last name, first name, department, annual salary

    RETURNS:
        list The employee record as a list
    """
    id = ui_helper.get_user_positive_int("Please enter the employee ID:")
    last_name = ui_helper.get_user_string("Please enter the last name:")
    first_name = ui_helper.get_user_string("Please enter the first name:")
    dept = ui_helper.get_user_string("Please enter the department:")
    salary = ui_helper.get_user_float("Please enter the annual salary:")
    employee = [id, last_name, first_name, dept, salary]
    return employee

def show_employee_table(employees:list):
    """
    Displays a list of employees as a table.

    INPUTS:
        employees A list of employee records
    """
    widths = [(5,"center"),(40,"left"),(20,"left"),(20,"right")]
    headers = ["ID","NAME","DEPARTMENT","SALARY"]
    emp_list = []
    for employee in employees:
        current = []
        current.append(employee[0]) # ID
        current.append(employee[1] + ", " + employee[2]) # Name
        current.append(employee[3])
        current.append(f"{employee[4]:.2f}")
        emp_list.append(current)
    ui_helper.draw_table(widths, headers, emp_list)
    
def get_employee_id()->int:
    """ gets an employee ID from the user.
    RETURNS: 
        int The ID  entered by the user"""
    id = ui_helper.get_user_positive_int("\nPlease enter th employee ID: ") 
    return id  

def show_single_employee(employee: list):
    """ display the single employee record in a table """
    
    show_employee_table([employee])     
def get_updated_employee_data(employee:list)-> list:
    """" """
    
    ui_helper.show_message("\nPress Enter to keep the existing value.")
    id = employee[es.ID_IDX]
    
    # get last name
    
    prompt = f"Please enter the last name({employee[es.LNAME_IDX]}): "
    last_name = ui_helper.get_user_string(prompt)
    if len(last_name) == 0:
        last_name = employee[es.LNAME_IDX]
        
    # get first name
    
    prompt = f"Please enter the first name ({employee[es.FNAME_IDX]}): "
    first_name = ui_helper.get_user_string(prompt)
    if len(first_name) == 0:
        first_name = employee[es.FNAME_IDX]
        
    # get department
    
    prompt = f"Please enter the department ({employee[es.DEPT_IDX]}): "
    dept = ui_helper.get_user_string(prompt)
    if len(dept) == 0:
        dept = employee[es.DEPT_IDX]
        
    # get the salary
    
    prompt = f"Please enter the annual salary ({employee[es.SALARY_IDX]:.2f}): "
    try:
        salary = ui_helper.get_user_float(prompt)
    except ValueError:
        # canceled, so use the existing value
        salary = employee[es.SALARY_IDX]
    # Return the new values
    return[id, last_name, first_name, dept, salary]
   