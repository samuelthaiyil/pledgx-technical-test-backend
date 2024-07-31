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
def submit_user():
    data = request.json

    # Validation
    if not data.get("firstName"):
        return jsonify({"Error": "firstName must have a value."}), 400
    if not data.get("lastName"):
        return jsonify({"Error": "lastName must have a value."}), 400
    if not data.get("phoneNumber"):
        return jsonify({"Error": "phoneNumber must have a value."}), 400
    if not data.get("jobTitle"):
        return jsonify({"Error": "jobTitle must have a value."}), 400
    if not data.get("country"):
        return jsonify({"Error": "country must have a value."}), 400

    try:
        connection = create_connection()
        if connection.is_connected():
            cursor = connection.cursor(dictionary=True)
            
            cursor.execute("SELECT * FROM users ORDER BY id LIMIT 1")
            first_row = cursor.fetchone()
            
            if first_row:
                update_query = """
                UPDATE users SET first_name = %s, last_name = %s, phone_number = %s, job_title = %s, country = %s WHERE id = %s
                """
                cursor.execute(update_query, (
                    data["firstName"],
                    data["lastName"],
                    data["phoneNumber"],
                    data["jobTitle"],
                    data["country"],
                    first_row['id']
                ))
                connection.commit()
                
                return jsonify("Success"), 200
            else:
                return jsonify({"Error": "Table has no rows to update."}), 404
                
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"Error": str(e)}), 500
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/get-user', methods=['GET'])
def get_user():
    connection = create_connection()
    try:
        if connection.is_connected():
                print("successfully connected to db")
        
                cursor = connection.cursor(dictionary=True)
                sql_query = "SELECT * FROM users"
                cursor.execute(sql_query)
                
                user = cursor.fetchone()

                if user:
                    return user, 200
                else:
                    return jsonify({"error": "user not found"}), 404
    
    except Error as e:
        print(f"error connecting to db: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        

if __name__ == '__main__':
    app.run(port=3000, debug=True)
    