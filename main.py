import psycopg2
import os
from dotenv import load_dotenv

def populate_table(cursor):
    # Create the USERS table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS USERS (
        user_id int PRIMARY KEY,
        username varchar(50),
        email varchar(50)
    );
    """)

    # Create the ORDERS table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ORDERS (
        order_id int PRIMARY KEY,
        user_id int,
        order_amount float,
        order_date date,
        FOREIGN KEY (user_id) REFERENCES USERS(user_id)
    );
    """)

    # Insert data into USERS table
    cursor.execute("""
    INSERT INTO USERS(user_id, username, email) 
    VALUES (1, 'Alice', 'alice@mail.com') 
    ON CONFLICT (user_id) DO NOTHING;
    """)
    cursor.execute("""
    INSERT INTO USERS(user_id, username, email) 
    VALUES (2, 'Bob', 'bob@mail.com') 
    ON CONFLICT (user_id) DO NOTHING;
    """)

    # Insert data into ORDERS table
    cursor.execute("""
    INSERT INTO ORDERS(order_id, user_id, order_amount, order_date) 
    VALUES (101, 1, 50.00, '2024-01-10'), 
           (102, 2, 100.00, '2024-01-15'),
           (103, 1, 75.00, '2024-02-01') 
    ON CONFLICT (order_id) DO NOTHING;
    """)

def total_amount_per_user(cursor):
    # First query: Total order amount by user
    query1 = """
    SELECT u.username, SUM(o.order_amount) as total_order_amount
    FROM orders o
    JOIN users u ON o.user_id = u.user_id
    GROUP BY u.user_id;
    """
    cursor.execute(query1)
    total_orders = cursor.fetchall()
    
    print("Total order amounts by user:")
    for user in total_orders:
        print(f"Username: {user[0]}, Total Order Amount: {user[1]}")

def user_spent_50_up(cursor):
    # Second query: Users who have placed orders greater than $50
    query2 = """
    SELECT DISTINCT u.user_id, u.username
    FROM users u
    JOIN orders o ON u.user_id = o.user_id
    WHERE o.order_amount > 50;
    """
    cursor.execute(query2)
    users_over_50 = cursor.fetchall()
    
    print("\nUsers who placed orders greater than 50:")
    for user in users_over_50:
        print(f"User ID: {user[0]}, Username: {user[1]}")

def init_connection_params():
    # Load environment variables from .env file
    load_dotenv()
    
    return {
        "host": os.getenv("POSTGRES_HOST"),
        "dbname": os.getenv("POSTGRES_DBNAME"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "port": os.getenv("POSTGRES_PORT"),
    }

def main():
    try:
        # Create a connection to the database
        connection = psycopg2.connect(**init_connection_params())
        cursor = connection.cursor()

        populate_table(cursor)
        total_amount_per_user(cursor)
        user_spent_50_up(cursor)
        
    except Exception as error:
        print(f"Error: {error}")

    finally:
        # Save changes
        connection.commit()
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

main()