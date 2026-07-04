#!/usr/bin/env python3
#   file    employee_program.py
#   date    2025-09-15
#   author  Chris bofole
#   DESCRIPTION
"""
This is the starting version of the employee program.

Inputs
id int entered by user
last_name string entered by user
first_name string entered by user
dept string entered by user
salary float entered by user

OUTPUTS
A header row showing the names of data columns.
A data row with the employee data with following columns:
1) dept 15 characters wide left justified
2) id 10 characters wide centered
3) full name 50 characters wide left justified
4) salary 15 characters wide right justified

"""

CONSOLE_WIDTH = 80
"""
The width of the console in characters.
"""

def main():
    """
    get employee data and draw a table
    """
    # Define the prompt strings
    id_prompt = "Please enter the employee ID: "
    last_name_prompt = "Please enter the last name: "
    first_name_prompt = "Please enter the first name: "
    dept_prompt = "Please enter the department: "
    salary_prompt = "Please enter the salary: "
    # string for outputs 
    table_name = "Employee Data"
    bar = "-" * CONSOLE_WIDTH
    dept_header = "DEPARTMENT"
    id_header = "ID"
    emp_name_header = "EMPLOYEE NAME"
    salary_header = "SALARY"
    program_complete = "Program Complete"
    program_title = "*** Employee Program ***"
    print(f"\n{program_title:^{ CONSOLE_WIDTH}}\n")
    # Inputs
    id = int(input(id_prompt))
    last_name = input(last_name_prompt)
    first_name = input(first_name_prompt)
    dept = input(dept_prompt)
    salary = float(input(salary_prompt))
    # Process
    full_name = last_name + ", " + first_name
    # Outputs
    dept_width = 12
    print(f"\n{table_name:^{CONSOLE_WIDTH}}")
    print(bar)
    print(f"|{dept_header:^{dept_width}s} | {id_header:10s} | " \
          f"{emp_name_header:^30s} | {salary_header:^15s} |")
    print(bar)
    print(f" |{dept:<{dept_width}s} | {id:^10d} | " \
          f"{full_name:<30s} | {salary:<15.2f} |")
    print(bar)
    # tell the user the program is complete
    print(f"\n{program_complete}.")
    
    
if __name__ == "__main__":
    main()