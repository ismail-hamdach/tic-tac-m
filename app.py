from flask import Flask, jsonify, request
from flasgger import Swagger
import socket

from addUser import addUser, deleteUser  # Corrected import statement

app = Flask(__name__)
swagger = Swagger(app)  # Initialize Swagger

@app.route('/connection/check', methods=['POST'])
def check_connection():
    """
    Check connection to a given IP address and port
    ---
    parameters:
      - name: ip_address
        in: body
        type: string
        required: true
        example: "192.168.1.1"
      - name: port
        in: body
        type: integer
        required: true
        example: 8080
    responses:
      200:
        description: Connection successful
        schema:
          type: object
          properties:
            status:
              type: string
              example: "Connection successful"
      400:
        description: Bad request
        schema:
          type: object
          properties:
            error:
              type: string
              example: "IP address and port are required"
    """
    data = request.json
    ip_address = data.get('ip_address')
    port = data.get('port')
    
    if not ip_address or not port:
        return jsonify({"error": "IP address and port are required"}), 400
    
    try:
        sock = socket.create_connection((ip_address, port), timeout=5)
        sock.close()
        return jsonify({"status": "Connection successful"})
    except socket.error as e:
        return jsonify({"status": "Connection failed", "error": str(e)}), 400

@app.route('/add_user', methods=['POST'])
def api_add_user():
    """
    Add a new user
    ---
    parameters:
      - name: user_name
        in: body
        type: string
        required: true
        example: "john_doe"
      - name: ip_address
        in: body
        type: string
        required: true
        example: "192.168.1.1"
      - name: port
        in: body
        type: integer
        required: true
        example: 8080
    responses:
      201:
        description: User added successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "User john_doe added successfully"
            data:
              type: object
              properties:
                user_id:
                  type: integer
                  example: 1
                user_name:
                  type: string
                  example: "john_doe"
                privilege:
                  type: string
                  example: "admin"
                password:
                  type: string
                  example: "securepassword"
      400:
        description: Bad request
        schema:
          type: object
          properties:
            error:
              type: string
              example: "user_name, ip_address and port are required"
      500:
        description: Internal server error
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Error message"
    """
    user_name = request.json.get('user_name')
    ip_address = request.json.get('ip_address')
    port = request.json.get('port')
    if not user_name or not ip_address or not port:
        return jsonify({"error": "user_name, ip_address and port are required"}), 400

    try:
        user_id, user_name, privilege, password = addUser(user_name, ip_address, port)
        
        return jsonify({"message": f"User {user_name} added successfully", "data": {
            "user_id": user_id,
            "user_name": user_name,
            "privilege": privilege, 
            "password": password
        }}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/delete_user', methods=['DELETE'])
def api_delete_user():
    """
    Delete a user by ID
    ---
    parameters:
      - name: user_id
        in: body
        type: integer
        required: true
        example: 1
    responses:
      200:
        description: User deleted successfully
        schema:
          type: object
          properties:
            message:
              type: string
              example: "User with ID 1 deleted successfully"
      400:
        description: Bad request
        schema:
          type: object
          properties:
            error:
              type: string
              example: "user_id is required"
      500:
        description: Internal server error
        schema:
          type: object
          properties:
            error:
              type: string
              example: "Error message"
    """
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"error": "user_id is required"}), 400

    try:
        deleteUser(user_id)  # Call the deleteUser function
        return jsonify({"message": f"User with ID {user_id} deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)