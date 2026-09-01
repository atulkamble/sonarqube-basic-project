# app.py
# ============================================================
# SonarQube Basic Practice Project
#
# Practice:
# - Bugs
# - Vulnerabilities
# - Security Hotspots
# - Code Smells
# - Coverage
# - Duplications
#
# WARNING: Intentionally bad/insecure code for SonarQube practice.
# ============================================================

import os
import subprocess


# ============================================================
# 1. BUGS
# ============================================================

def divide(a, b):
    # BUG: No check for division by zero
    return a / b


def get_user(users, index):
    # BUG: Index is not validated
    return users[index]


# ============================================================
# 2. VULNERABILITIES
# ============================================================

def database_connection():
    # VULNERABILITY:
    # Hard-coded credentials should not be stored in source code

    username = "admin"
    password = "admin123"

    print("Username:", username)
    print("Password:", password)


def run_command(user_input):
    # VULNERABILITY:
    # User input is passed directly to the operating system
    # Command injection may be possible

    os.system(user_input)


# ============================================================
# 3. SECURITY HOTSPOTS
# ============================================================

def execute_backup():
    # SECURITY HOTSPOT:
    # shell=True executes the command through a system shell
    # This security-sensitive operation should be reviewed

    subprocess.run(
        "echo Creating backup",
        shell=True
    )


# ============================================================
# 4. CODE SMELLS / TECHNICAL DEBT
# ============================================================

def calculate_total(price, quantity):

    # CODE SMELL:
    # Variable created but never used
    unused_variable = "Not Required"

    total = price * quantity

    # CODE SMELL:
    # Deeply nested conditions reduce readability

    if total > 1000:
        if total > 2000:
            if total > 3000:
                print("Very expensive")

    return total


def check_number(number):

    # CODE SMELL:
    # Repetitive conditional logic

    if number > 10:
        print("Greater than 10")

    if number > 20:
        print("Greater than 20")

    if number > 30:
        print("Greater than 30")

    if number > 40:
        print("Greater than 40")


# ============================================================
# 5. DUPLICATIONS
# ============================================================

def employee_report():

    # DUPLICATED CODE

    name = "Employee"
    department = "IT"
    company = "Cloud Company"

    print("==========================")
    print("Employee Report")
    print("==========================")
    print("Name:", name)
    print("Department:", department)
    print("Company:", company)
    print("==========================")


def manager_report():

    # DUPLICATED CODE

    name = "Manager"
    department = "IT"
    company = "Cloud Company"

    print("==========================")
    print("Employee Report")
    print("==========================")
    print("Name:", name)
    print("Department:", department)
    print("Company:", company)
    print("==========================")


# ============================================================
# 6. COVERAGE
# ============================================================

def add(a, b):
    # Create test case for this function
    return a + b


def subtract(a, b):
    # Leave without test to demonstrate uncovered code
    return a - b


def multiply(a, b):
    # Leave without test to demonstrate uncovered code
    return a * b


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("===== SonarQube Practice Project =====")

    print("Addition:", add(10, 5))

    print("Division:", divide(10, 5))

    database_connection()

    calculate_total(500, 10)

    check_number(50)

    employee_report()

    manager_report()

    execute_backup()
