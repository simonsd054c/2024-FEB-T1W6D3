login_attempts = 5
actual_password = "hello"

while login_attempts > 0:
    password = input("Enter password: ")
    if (password != actual_password):
        print("Wrong Password")
        login_attempts -= 1
        print(f"Remaining attempts: {login_attempts}")
        if (login_attempts == 0):
            print("you ran out of attempts")
    else:
        print("Login successful")
        break