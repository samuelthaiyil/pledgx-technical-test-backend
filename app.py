from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app) 

config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '5V@xqzA1/4qU',
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


if __name__ == '__main__':
    connection = create_connection()
    app.run(port=3000, debug=True)
    