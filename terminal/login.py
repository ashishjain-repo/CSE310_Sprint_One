import hashlib

#Hash the password in a hash format
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


#Validate Username and Pass
def validate_username_password(username, password, min_length=5, max_length=10):
    errors = []
    if not username.strip():
        errors.append("Username cannot be empty.")
    if not password.strip():
        errors.append("Password cannot be empty.")
    if " " in password:
        errors.append("Password cannot contain spaces.")
    if len(password) < min_length or len(password) > max_length:
        errors.append(f"Password must be between {min_length} and {max_length} characters.")
    return errors

def Validate_password (password,min_length=5, max_length=10):
    errors = []
    if not password.strip():
        print("Password cannot be empty.")
        return False
    if " " in password:
        print("Password cannot contain spaces.")
        return False
    if len(password) < min_length or len(password) > max_length:
        print(f"Password must be between {min_length} and {max_length} characters.")
        return False
    else:
        return True