from flask import Flask
import psycopg2

app = Flask(__name__)

# db_params = {
#     'dbname': 'your_database',
#     'user': 'your_username',
#     'password': 'your_password',
#     'host': 'your_host',
#     'port': 'your_port'
# }

# def connect_to_database():
#     connection = psycopg2.connect(host="127.0.0.1", port = 5432,database="postgres", user="", password="120698")
#     return connection


@app.route('/')
def index():
    # Connect to the database
    connection = psycopg2.connect(host="127.0.0.1", port = 5432,database="postgres", user="postgres", password="120698")

    # Create a cursor
    cursor = connection.cursor()

    # Execute a sample query
    cursor.execute("SELECT version();")

    # Fetch the result
    result = cursor.fetchone()
    print(result)
    # Close the cursor and connection
    cursor.close()
    connection.close()
    
    # Return the result as a response
    return f"PostgreSQL Database Version: {result[0]}"
