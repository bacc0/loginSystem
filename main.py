# User data dictionary to store user details (for simplicity, not recommended for production)
user_data = {}

# Function to register a new user
def register_user():
    username = input("Enter a username: ")
    if username in user_data:
        print("Username already exists. Please choose a different one.")
        return
    password = input("Enter a password: ")
    user_data[username] = password
    print("Registration successful. You can now log in.")

# Function to log in a user
def login_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_data and user_data[username] == password:
        print(
            "\n...............................\n" +
              "Login successful. Welcome, " + 
              username + 
              "!\n" +
              "...............................\n" 
              )
    else:
        print("\n * * * * * * * * * * * * * * * * * * * * *  * * * ")
        print("Invalid username or password. Please try again.")
        print(" * * * * * * * * * * * * * * * * * * * * *  * * *\n ")

# Main program
while True:
    print("\n-------------------------------")
    print("User Registration and Login System")
    print("-------------------------------\n")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("\n-------------------------------")
    choice = input("Select an option (1, 2, 3): ")


    if choice == '1':
        register_user()
    elif choice == '2':
        login_user()
    elif choice == '3':
        print("\n Goodbye! \n")
        break
    else:
        print(" * * * * * * * * * * * * * * * * * * * * * ")
        print("Invalid choice. Please select 1, 2, or 3.")
        print(" * * * * * * * * * * * * * * * * * * * * * ")
