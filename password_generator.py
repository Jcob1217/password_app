import string
import random

# Function validating user's input and returning password characteristics
def criteria_input():
    valid_answers = ["y", "n"]

    while True:
        try:
            length = int(input("Enter the minimal password length: "))
            break
        except ValueError:
            print("Value must be an Integer!")

    while True:
        has_capital = input("Does the password require at least one capital? (y/n): ").lower()
        if has_capital not in valid_answers:
            print("Value must be either y or n!")
        else:
            break

    while True:
        has_numbers = input("Does the password require numbers (y/n): ").lower()
        if has_numbers not in valid_answers:
            print("Value must be either y or n!")
        else:
            break

    while True:
        has_special = input("Does the password include any special characters (y/n): ").lower()
        if has_special not in valid_answers:
            print("Value must be either y or n!")
        else:
            break

    return (length, has_numbers, has_special, has_capital)


def generate_password(length, has_numbers, has_special, has_capital):
    # Creating empty password
    password = ""
    # Creating variable options that stores all signs that can be used in password
    options = string.ascii_letters

    criteria_1 = False
    criteria_2 = False
    criteria_3 = False
    criteria_4 = False
    meets_all_criteria = False

    # Checking if user wants to use given criterion in password
    if has_capital != "y":
        criteria_2 = True

    if has_numbers == "y":
        # Appending options with numbers
        options += string.digits
    else:
        criteria_3 = True

    if has_special == "y":
        # Appending options with special characters
        options += string.punctuation
    else:
        criteria_4 = True

    while meets_all_criteria == False or len(password) < length:
        new_char = str(random.choice(options))

        # Checking if new character fulfill given criteria
        if new_char in string.ascii_letters:
            criteria_1 = True
        if new_char in string.ascii_uppercase:
            criteria_2 = True
        elif new_char in string.digits:
            criteria_3 = True
        elif new_char in string.punctuation:
            criteria_4 = True
        
        # Mathematical product of all criteria boolean value
        meets_all_criteria = (criteria_1 and criteria_2 and criteria_3 and criteria_4)

        # Appending new character to password
        password += new_char

    return password

def main():
    criteria = criteria_input()
    password = generate_password(*criteria)
    print(password)

if __name__ == "__main__":
    main()
