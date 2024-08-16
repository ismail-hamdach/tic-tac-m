import sys
import os

# Add the directory containing mysqlHelper to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def check_connection(request):
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