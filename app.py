from calculator import add, subtract, divide, execute_command, unsafe_eval
from calculator import hash_password, login

print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Division:", divide(10, 0))

# Hardcoded credentials - vulnerability / security issue
username = "admin"
password = "Admin@123"

print("Login:", login(username, password))

# Unsafe eval - vulnerability
user_input = input("Enter calculation: ")
print(unsafe_eval(user_input))

# OS command execution - security hotspot
command = input("Enter Linux command: ")
execute_command(command)

# Weak hashing algorithm
print("Password Hash:", hash_password(password))

# Sensitive information exposure
print("Database Password:", password)

# Technical debt / code smell
unused_variable = "This variable is never used"

# Duplicate / unnecessary code
print("Application completed")
print("Application completed")
print("Application completed")
