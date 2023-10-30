# User data dictionary to store user details (for simplicity, not recommended for production)
user_data = {}
# Variable to track the logged-in user
logged_in_user = None  

# Function to register a new user
def register_user():
    while True:
        try:
            # Prompt the user to enter a username
            username = input("Enter a username: ")

            if username in user_data:
                print("Username already exists. Please choose a different one.")
                continue

            password = input("Enter a password: ")
            user_data[username] = password
            print("Registration successful. You can now log in.")
            break
        except KeyboardInterrupt:
            print("\nRegistration canceled.")
            break

# Function to log in a user
def login_user():
     # Use the global variable to track the logged-in user
    global logged_in_user 

    while True:
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")

            if username in user_data and user_data[username] == password:
                # Set the logged-in user
                logged_in_user = username  
                print("\n...............................\n" +
                      "Login successful. Welcome, " + username + "!\n" +
                      "...............................\n"
                      )
                break
            else:
                print("\n * * * * * * * * * * * * * * * * * * * * *  * * * ")
                print("Invalid username or password. Please try again.")
                print(" * * * * * * * * * * * * * * * * * * * * *  * * *\n ")
        except KeyboardInterrupt:
            print("\nLogin canceled.")
            break

# Function to log out a user
def logout_user():
    # Use the global variable to track the logged-in user
    global logged_in_user  
    if logged_in_user is not None:
        print("\n...........................................")
        print(f"You are logged out, {logged_in_user}.✋🏻")
        print("...........................................")
        # Reset the logged-in user
        logged_in_user = None  
    else:
        print("You are not logged in.\n")

# Main program
while True:
    print("\n-------------------------------")
    print("User Registration and Login System")
    print("-------------------------------\n")

    if logged_in_user is None:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
    else:
        print("...............................")
        print(f"Logged in as: {logged_in_user} ➡️➡️↘️")
        print("...............................\n")
        print("1. Exit")
        print("2. Logout")

    print("\n-------------------------------")

    # Adjust the menu prompt based on the login state
    if logged_in_user is None:
        choice = input("Select an option (1, 2, 3): ")
    else:
        choice = input("Select an option (1, 2): ")

    if choice == '1':
        if logged_in_user is None:
            register_user()
        else:
            # Option to exit when logged in
            print("\n😀 Goodbye! 😀\n")
            break
    elif choice == '2':
        if logged_in_user is None:
            login_user()
        else:
            logout_user()
    elif choice == '3':
        print("\n Goodbye! \n")
        break
    else:
        print(" * * * * * * * * * * * * * * * * * * * * * ")
        print("Invalid choice. Please select 1, 2, or 3.")
        print(" * * * * * * * * * * * * * * * * * * * * * ")
