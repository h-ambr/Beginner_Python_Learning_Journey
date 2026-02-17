# PASSWORD SAFETY CHECKER

#requirement 1 = minimum 12 characters
is_running = True
symbols = "@!$£*&^?/#%"
while is_running:
    password = input("Enter your password: ")
    if len(password) < 12:
        print("Your password has less than 12 characters!")
        #requirement 2 = needs symbols
    elif not any (char in symbols for char in password):
        print("Your password must include at least one symbol!")
        #requirement 3 = needs uppercase letters
    elif not any (char.isupper() for char in password):
        print("Your password must include uppercase letters")
        #requirement 4 = needs lowercase letters
    elif not any(char.islower() for char in password):
        print("Your password must include lowercase letters")
        #requirement 5 = needs digits
    elif not any(char.isdigit() for char in password):
        print("Your password must include digits")
    else:
        print("Password accepted ✅")
        is_running = False
