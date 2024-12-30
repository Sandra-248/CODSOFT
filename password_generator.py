import random
import string

def generate_password(length, use_special_chars=True, use_digits=True):
    if length < 1:
        return "Password length must be at least 1 character."

    lower_case_letters = string.ascii_lowercase
    upper_case_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    character_pool = lower_case_letters + upper_case_letters
    if use_digits:
        character_pool += digits
    if use_special_chars:
        character_pool += special_chars

    password = []
    if use_digits:
        password.append(random.choice(digits))
    if use_special_chars:
        password.append(random.choice(special_chars))

    remaining_length = length - len(password)
    password += random.choices(character_pool, k=remaining_length)
    random.shuffle(password)

    return ''.join(password)

try:
    password_length = int(input("Enter the desired password length: "))
    include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    include_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"

    generated_password = generate_password(password_length, include_special_chars, include_digits)
    print(f"Generated Password: {generated_password}")
except ValueError:
    print("Invalid input! Please enter a valid number for the password length.")
