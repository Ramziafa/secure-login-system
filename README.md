# Secure User Authentication System with Python and MariaDB

This is a simple user authentication system built with Python and MariaDB for secure user registration and login.

## Getting Started

1. Clone this repository to your local machine.

2. Install the required dependencies:
pip install mysql-connector-python

3. Ensure you have MariaDB installed and running. Create a database named "user_auth" in your MariaDB instance.

4. Edit the Python script (`login.py`) with your MariaDB username and password to establish a connection to the database.

5. Run the Python script to start the user interface:
python login.py


## Features

- Secure password hashing using SHA-256.
- User registration and login with error handling for duplicate usernames.
- Simple user interface for easy interaction.


