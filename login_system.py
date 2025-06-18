# TODO - Create a login system (userId & password). Also lock the user out after 3 unsuccessful attempts

# Track the number of remaining attempts
MAX_ATTEMPTS = 3

# Need to loop over three times, cause it's the maximum amount of tries
while MAX_ATTEMPTS > 0:
    print(f"\n Login Attempt ({MAX_ATTEMPTS} remaining)\n" + "-" * 30)

    # Taking inputs
    user_id = input("Enter the user ID (e.g., user@123): ")
    password = input("Enter the password (e.g., pass123): ")

    # Checker to see if credentials match
    if user_id == "user@123" and password == "pass123":
        print("\nLogged in successfully! Welcome.\n")
        break
    else:
        # Decrement number of attempts for each failed one
        print("\nInvalid credentials. Please try again.")
        MAX_ATTEMPTS -= 1

else:
    print("\nLogin failed. Maximum attempts exceeded.\n")
