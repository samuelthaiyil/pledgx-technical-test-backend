from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 

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
    app.run(port=3000, debug=True)