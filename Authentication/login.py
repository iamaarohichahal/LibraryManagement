users = {}

def register():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists.")
        return
    password = input("Enter a new password: ")
    users[username] = password
    print("User registered successfully!")

def login():
    username = input("Enter your username: ")
    if username not in users:
        print("Username not found. Please register first.")
        return
    password = input("Enter your password: ")
    if users[username] == password:
        print("Login successful! Welcome to the digital library.")
    else:
        print("Incorrect password. Please try again.")

def main():
    while True:
        print("Welcome to the Digital Library")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the main function
main()