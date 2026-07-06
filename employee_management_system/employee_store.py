#!/usr/bin/env python3
#   FILE    employee_store.py
#   DATE    2025-10-29 (ISO-8601 format)
#   AUTHOR  Chris bofole
#   DESCRIPTION
"""
This module handles the storage of the employee records.  This version uses 
a list for storage, so the data goes away when you close the program.

In MVC, this part of the Model

MOD DATE: 2025-11-05
MOD BY: cHRIS Bofole
MOD DESCRIPTION:
    Added .get_employee_by_id()

MOD DATE: 2025-11-12
MOD BY: CHRIS BOFOLE
MOD DESCRIPTION:

"""
FILE_NAME = "employee.cvs"

"""The name """


ID_IDX = 0

LNAME_IDX = 1

FNAME_IDX = 2

DEPT_IDX = 3

SALARY_IDX = 4


def store_employee(employee:list):
    """
    Appends the employee record to the primary file.

    INPUTS:
        employee A list representing an employee record
    """
    line = convert_record_to_string(employee)
    # open the file in append mode and write the line 
    with open(FILE_NAME, "a") as out_file:
        out_file.write(line)
    

def get_employee_list()->list:
    """
    Returns the primary list of employees.

    RETURNS:
        list A list of employee records
    """
    employees = []
    with open(FILE_NAME,"r") as in_file:
        for line in in_file:
            fields = line.split(",")
            id = int(fields[ID_IDX])
            last_name = fields[LNAME_IDX]
            first_name = fields[FNAME_IDX]
            dept = fields[DEPT_IDX]
            salary = round(float(fields[SALARY_IDX]), 2)
            employees.append([id, last_name, first_name, dept, salary])
    return employees


def get_employee_by_id(id: int)-> list:
    """ loop through the list of employees and returns"""
    
    desired = []
    employees = get_employee_list()
    for employee in employees:
        if employee[ID_IDX] == id:
            desired = employee
            break 
    return desired
def update_employee_by_id(employee: list)-> bool:
    """ get the list employee, loop trough them and update the one with the 
    matching ID. Return True if there was as match and False otherwise."""
    
    result = False
    id = employee[ID_IDX]
    keep = []
    employees = get_employee_list()
    for emp in employees:
        if emp[ID_IDX] == id:
            result = True
            keep.append(employee)
        else:
            keep.append(emp)
    if result:
        save_employee_list(keep)
    
    return result

def save_employee_list(employees: list):
    """ describe the function """
    
    with open(FILE_NAME, "w") as out_file:
        for employee in employees:
            line = convert_record_to_string(employee)
            out_file.write(line)
            
def remove_employee_by_id(id: int)-> bool:
    """ Get a list of employee and save all of them except for the one 
    with the matching ID. Returns True if found, False otherwise."""
    
    result = False
    keep = []
    employees = get_employee_list()
    for employee in employees:
        if employee[ID_IDX] == id:
            result = True
        else:
            keep.append(employee)
    if result:
        save_employee_list(keep)
        
    return result            
    
    
    
    
    
def convert_record_to_string(employee: list)-> str:
    """ describe the function """
    
    
    line = f"{employee[ID_IDX]},{employee[LNAME_IDX]},{employee[FNAME_IDX]}," + \
        f"{employee[DEPT_IDX]}, {employee[SALARY_IDX]:.2f}\n"
    return line