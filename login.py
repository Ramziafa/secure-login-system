import mysql.connector
import hashlib

# Function to create a new user
def create_user(username, password):
    # Establish a connection to the MariaDB database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",  # Replace with your MariaDB username
        password="your_mysql_password",  # Replace with your MariaDB password
        database="user_auth"
    )
    cursor = connection.cursor()

    # Hash the password before storing it
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    try:
        # Insert user data into the 'users' table
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, password_hash))
        connection.commit()
        print("Registration successful!")
    except mysql.connector.IntegrityError:
        print("Username already exists. Please choose a different username.")
    finally:
        connection.close()

# Function to authenticate a user
def authenticate_user(username, password):
    # Establish a connection to the MariaDB database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",  # Replace with your MariaDB username
        password="your_mysql_password",  # Replace with your MariaDB password
        database="user_auth"
    )
    cursor = connection.cursor()

    # Hash the password to match the stored hash
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    cursor.execute("SELECT * FROM users WHERE username = %s AND password_hash = %s", (username, password_hash))
    user = cursor.fetchone()

    connection.close()

    if user:
        return True
    else:
        return False

# Other functions for change password and user deletion can be added here

# User Interface
def user_interface():
    while True:
        print("Welcome to the CyberSec Authentication System!")
        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            create_user(username, password)
        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if authenticate_user(username, password):
                print("Login successful!")
            else:
                print("Invalid username or password. Please try again.")
        elif choice == "3":
            print("Logout successful!")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    user_interface()