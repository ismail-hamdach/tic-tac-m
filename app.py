from flask import Flask, jsonify, request
import socket

from addUser import addUser, deleteUser  # Corrected import statement


app = Flask(__name__)


@app.route('/connection/check', methods=['POST'])
def check_connection():
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