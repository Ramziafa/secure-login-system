# Secure User Authentication System with Python and MariaDB

This is a simple user authentication system built with Python and MariaDB for secure user registration and login.

## Getting Started

1. Clone this repository to your local machine.
- git clone https://github.com/Ramziafa/secure-login-system.git
2. Install the required dependencies:
- pip install mysql-connector-python

3. Ensure you have MariaDB installed and running.
4. Create a database named "user_auth" in your MariaDB instance:
```sql
CREATE DATABASE user_auth;
USE user_auth;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
```
5. Edit the Python script (`login.py`) with your MariaDB username and password to establish a connection to the database.
6. Run the Python script to start the user interface:
- python login.py


## Features

- Secure password hashing using SHA-256.
- User registration and login with error handling for duplicate usernames.
- Simple user interface for easy interaction.
- For a more detailed guide on how to set up and use the Secure User Authentication System, check out [my blog post](https://www.ramzitech.be/2023/07/building-secure-user-authentication.html).

