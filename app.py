# ============================================================
# SONARQUBE PRACTICE PROJECT
#
# Intentionally contains:
# - Bugs
# - Vulnerabilities / Security Issues
# - Security Hotspots
# - Code Smells
# - Uncovered Code
# - Duplicated Code
#
# FOR TRAINING ONLY
# ============================================================

import os
import subprocess
import hashlib
import random


# ============================================================
# BUGS
# ============================================================

def divide_numbers(a, b):
    # BUG PRACTICE:
    # Possible division by zero
    return a / b


def get_first_character(name):
    # BUG PRACTICE:
    # Empty string can cause IndexError
    return name[0]


def get_item(items, position):
    # BUG PRACTICE:
    # Position is not validated
    return items[position]


def calculate_average(numbers):
    # BUG PRACTICE:
    # Empty list causes division by zero
    return sum(numbers) / len(numbers)


# ============================================================
# VULNERABILITIES / SECURITY ISSUES
# ============================================================

def execute_user_command(command):
    # SECURITY:
    # User-controlled command passed directly to OS shell
    os.system(command)


def execute_shell_command(command):
    # SECURITY:
    # shell=True with external input is dangerous
    subprocess.run(command, shell=True)


def login(username, password):

    # SECURITY:
    # Hard-coded password
    admin_password = "Admin@123456"

    if username == "admin" and password == admin_password:
        print("Login successful")
    else:
        print("Login failed")


# ============================================================
# SECURITY HOTSPOTS
# ============================================================

def generate_token():

    # SECURITY HOTSPOT:
    # random is not suitable for security-sensitive tokens

    token = random.randint(100000, 999999)

    return token


def hash_password(password):

    # SECURITY HOTSPOT:
    # MD5 is weak for password hashing

    result = hashlib.md5(password.encode())

    return result.hexdigest()


def delete_file(filename):

    # SECURITY-SENSITIVE FILE OPERATION

    os.remove(filename)


# ============================================================
# CODE SMELLS
# ============================================================

def calculate_price(price, quantity):

    # CODE SMELL:
    # Unused variable

    unused_message = "Calculating price"

    total = price * quantity

    # CODE SMELL:
    # Deep nested conditions

    if total > 100:
        if total > 200:
            if total > 300:
                if total > 400:
                    if total > 500:
                        print("Large order")

    return total


def check_score(score):

    # CODE SMELL:
    # Repetitive conditions

    if score > 10:
        print("Greater than 10")

    if score > 20:
        print("Greater than 20")

    if score > 30:
        print("Greater than 30")

    if score > 40:
        print("Greater than 40")

    if score > 50:
        print("Greater than 50")

    if score > 60:
        print("Greater than 60")


def very_long_function(number):

    # CODE SMELL:
    # Function intentionally contains unnecessary/repetitive logic

    result = number

    result = result + 1
    result = result + 2
    result = result + 3
    result = result + 4
    result = result + 5
    result = result + 6
    result = result + 7
    result = result + 8
    result = result + 9
    result = result + 10

    if result > 10:
        print("10")

    if result > 20:
        print("20")

    if result > 30:
        print("30")

    if result > 40:
        print("40")

    if result > 50:
        print("50")

    return result


# ============================================================
# DUPLICATED CODE - BLOCK 1
# ============================================================

def employee_report():

    name = "Atul"
    employee_id = 101
    department = "Cloud"
    company = "Cloudnautic"
    location = "Pune"
    country = "India"
    role = "Engineer"
    salary = 50000

    print("=================================")
    print("Employee Information")
    print("=================================")
    print("Name:", name)
    print("Employee ID:", employee_id)
    print("Department:", department)
    print("Company:", company)
    print("Location:", location)
    print("Country:", country)
    print("Role:", role)
    print("Salary:", salary)
    print("=================================")
    print("Report Generated Successfully")
    print("=================================")


# ============================================================
# DUPLICATED CODE - BLOCK 2
# ============================================================

def manager_report():

    name = "Manager"
    employee_id = 102
    department = "Cloud"
    company = "Cloudnautic"
    location = "Pune"
    country = "India"
    role = "Manager"
    salary = 80000

    print("=================================")
    print("Employee Information")
    print("=================================")
    print("Name:", name)
    print("Employee ID:", employee_id)
    print("Department:", department)
    print("Company:", company)
    print("Location:", location)
    print("Country:", country)
    print("Role:", role)
    print("Salary:", salary)
    print("=================================")
    print("Report Generated Successfully")
    print("=================================")


# ============================================================
# DUPLICATED CODE - BLOCK 3
# ============================================================

def developer_report():

    name = "Developer"
    employee_id = 103
    department = "Cloud"
    company = "Cloudnautic"
    location = "Pune"
    country = "India"
    role = "Developer"
    salary = 60000

    print("=================================")
    print("Employee Information")
    print("=================================")
    print("Name:", name)
    print("Employee ID:", employee_id)
    print("Department:", department)
    print("Company:", company)
    print("Location:", location)
    print("Country:", country)
    print("Role:", role)
    print("Salary:", salary)
    print("=================================")
    print("Report Generated Successfully")
    print("=================================")


# ============================================================
# COVERAGE PRACTICE
# ============================================================

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def square(number):
    return number * number


def cube(number):
    return number * number * number


def percentage(value, total):
    return (value / total) * 100


def calculate_tax(amount):
    return amount * 0.18


def calculate_discount(amount):
    return amount * 0.10


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("SonarQube Practice Project")

    print(add(10, 5))

    print(divide_numbers(10, 2))

    print(get_first_character("SonarQube"))

    print(get_item(["AWS", "Azure", "DevOps"], 1))

    print(calculate_average([10, 20, 30]))

    login("admin", "Admin@123456")

    print("Token:", generate_token())

    print("Hash:", hash_password("password123"))

    calculate_price(100, 10)

    check_score(70)

    very_long_function(10)

    employee_report()

    manager_report()

    developer_report()
