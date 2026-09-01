# ============================================================
# SONARQUBE BASIC PRACTICE PROJECT
#
# Intentionally contains:
# - Security Hotspots
# - Code Smells
# - Coverage gaps
# - Duplicated Code
#
# FOR TRAINING / PRACTICE ONLY
# ============================================================

import os
import subprocess
import hashlib
import random


# ============================================================
# BASIC BUG-LIKE PRACTICE
# ============================================================

def divide_numbers(a, b):
    # No zero validation
    return a / b


def get_first_character(name):
    # Empty string can cause IndexError
    return name[0]


def get_item(items, position):
    # Invalid position can cause IndexError
    return items[position]


def calculate_average(numbers):
    # Empty list can cause division by zero
    return sum(numbers) / len(numbers)


# ============================================================
# SECURITY PRACTICE
# ============================================================

def execute_user_command(command):
    # Security-sensitive command execution
    os.system(command)


def execute_shell_command(command):
    # shell=True is security-sensitive
    subprocess.run(command, shell=True)


def login(username, password):
    # Hard-coded password for practice
    admin_password = "Admin@123456"

    if username == "admin" and password == admin_password:
        print("Login successful")
    else:
        print("Login failed")


# ============================================================
# SECURITY HOTSPOTS
# ============================================================

def generate_token():
    # random should not be used for security tokens
    token = random.randint(100000, 999999)

    return token


def hash_password(password):
    # MD5 is weak for password hashing
    result = hashlib.md5(password.encode())

    return result.hexdigest()


def execute_backup():
    # shell=True should be reviewed
    subprocess.run(
        "echo Creating backup",
        shell=True
    )


# ============================================================
# CODE SMELLS
# ============================================================

def calculate_price(price, quantity):

    # Unused variable
    unused_message = "Calculating price"

    total = price * quantity

    # Deeply nested code
    if total > 100:
        if total > 200:
            if total > 300:
                if total > 400:
                    if total > 500:
                        print("Large order")

    return total


def check_score(score):

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

def report_one():

    print("================================")
    print("Cloud Training Report")
    print("================================")
    print("Course: Cloud DevOps")
    print("Trainer: Atul")
    print("Location: Pune")
    print("Mode: Online")
    print("Technology: AWS")
    print("Technology: Azure")
    print("Technology: Linux")
    print("Technology: Git")
    print("Technology: Jenkins")
    print("Technology: Docker")
    print("Technology: Kubernetes")
    print("Technology: Terraform")
    print("Technology: Ansible")
    print("Technology: SonarQube")
    print("Status: Active")
    print("Duration: 3 Months")
    print("Environment: Training")
    print("Project: DevOps Practice")
    print("================================")
    print("Report Generated Successfully")
    print("================================")


# ============================================================
# DUPLICATED CODE - BLOCK 2
# ============================================================

def report_two():

    print("================================")
    print("Cloud Training Report")
    print("================================")
    print("Course: Cloud DevOps")
    print("Trainer: Atul")
    print("Location: Pune")
    print("Mode: Online")
    print("Technology: AWS")
    print("Technology: Azure")
    print("Technology: Linux")
    print("Technology: Git")
    print("Technology: Jenkins")
    print("Technology: Docker")
    print("Technology: Kubernetes")
    print("Technology: Terraform")
    print("Technology: Ansible")
    print("Technology: SonarQube")
    print("Status: Active")
    print("Duration: 3 Months")
    print("Environment: Training")
    print("Project: DevOps Practice")
    print("================================")
    print("Report Generated Successfully")
    print("================================")


# ============================================================
# DUPLICATED CODE - BLOCK 3
# ============================================================

def report_three():

    print("================================")
    print("Cloud Training Report")
    print("================================")
    print("Course: Cloud DevOps")
    print("Trainer: Atul")
    print("Location: Pune")
    print("Mode: Online")
    print("Technology: AWS")
    print("Technology: Azure")
    print("Technology: Linux")
    print("Technology: Git")
    print("Technology: Jenkins")
    print("Technology: Docker")
    print("Technology: Kubernetes")
    print("Technology: Terraform")
    print("Technology: Ansible")
    print("Technology: SonarQube")
    print("Status: Active")
    print("Duration: 3 Months")
    print("Environment: Training")
    print("Project: DevOps Practice")
    print("================================")
    print("Report Generated Successfully")
    print("================================")


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

    print("===== SonarQube Practice Project =====")

    print("Addition:", add(10, 5))

    print("Division:", divide_numbers(10, 2))

    print("First Character:", get_first_character("SonarQube"))

    print(
        "Selected Item:",
        get_item(["AWS", "Azure", "DevOps"], 1)
    )

    print(
        "Average:",
        calculate_average([10, 20, 30])
    )

    login(
        "admin",
        "Admin@123456"
    )

    print(
        "Generated Token:",
        generate_token()
    )

    print(
        "Password Hash:",
        hash_password("password123")
    )

    calculate_price(
        100,
        10
    )

    check_score(70)

    very_long_function(10)

    execute_backup()

    report_one()

    report_two()

    report_three()
