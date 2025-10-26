#!/usr/bin/python3
"""
A Python script to create the database 'alx_book_store' in MySQL.
"""

import mysql.connector
from mysql.connector import Error

try:
    # Connect to MySQL Server (adjust host, user, password if needed)
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='cadillac@2005'  # <-- replace with your actual MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error while connecting to MySQL: {e}")

finally:
    # Safely close cursor and connection
    if 'cursor' in locals() and cursor is not None:
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
