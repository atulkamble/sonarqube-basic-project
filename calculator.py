import hashlib
import subprocess


# Simple function
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# BUG:
# No validation for division by zero
def divide(a, b):
    return a / b


# VULNERABILITY:
# eval() executes arbitrary Python code
def unsafe_eval(expression):
    return eval(expression)


# SECURITY HOTSPOT:
# shell=True can allow command injection
def execute_command(command):
    subprocess.run(command, shell=True)


# VULNERABILITY:
# MD5 is a weak cryptographic algorithm
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()


# SECURITY ISSUE:
# Hardcoded credentials
def login(username, password):
    admin_username = "admin"
    admin_password = "Admin@123"

    if username == admin_username and password == admin_password:
        return True
    else:
        return False


# CODE SMELL / TECHNICAL DEBT:
# Too many parameters
def create_user(
    name,
    email,
    phone,
    address,
    city,
    state,
    country,
    password,
    age,
    department,
):
    print(name)
    print(email)
    print(phone)
    print(address)
    print(city)
    print(state)
    print(country)
    print(password)
    print(age)
    print(department)


# CODE SMELL:
# Duplicate conditions
def check_number(number):
    if number > 10:
        print("Greater than 10")

    if number > 10:
        print("Number is large")


# CODE SMELL:
# Broad exception handling
def risky_operation():
    try:
        value = 10 / 0
        return value
    except Exception:
        pass


# TECHNICAL DEBT
# TODO should eventually be implemented
def process_payment():
    # TODO: Implement payment processing
    pass
