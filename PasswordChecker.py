import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    if not re.search(r"[A-Z]", password):
        return "Weak"
    if not re.search(r"[a-z]", password):
        return "Weak"
    if not re.search(r"[0-9]", password):
        return "Weak"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Weak"
    return "Strong"

password = input("Enter your password: ")
print("Password strength:", check_password_strength(password))
