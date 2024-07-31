from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app) 

config = {
    'host': 'localhost',
    'user': 'pledgx_user',
    'password': '',
    'database': 'pledgx',
    'port': 3306
}

def create_connection():
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None

@app.route('/submit-user', methods=['POST'])
def submit_form():
    data = request.json
   
    # validation
    if not data["firstName"]:
        return jsonify({"Error": "firstName must have a value."}), 400
    if not data["lastName"]:
        return jsonify({"Error": "lastName must have a value."}), 400
    if not data["phoneNumber"]:
        return jsonify({"Error": "phoneNumber must have a value."}), 400
    if not data["jobTitle"]:
        return jsonify({"Error": "jobTitle must have a value."}), 400    
    if not data["country"]:
        return jsonify({"Error": "country must have a value."}), 400
    
    return jsonify("Success"), 200

def fetch_all():
    connection = create_connection()
    try:
        if connection.is_connected():
                print("Connected to MySQL database")
                
                # Create a cursor object using the cursor() method
                cursor = connection.cursor(dictionary=True)
                
                # Prepare SQL query to fetch all rows from the users table
                sql_query = "SELECT * FROM users"
                
                # Execute the SQL query
                cursor.execute(sql_query)
                
                # Fetch all rows using fetchall() method
                rows = cursor.fetchall()
                
                # Print each row
                for row in rows:
                    print(row)
                
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



if __name__ == '__main__':
    fetch_all()
    app.run(port=3000, debug=True)
    