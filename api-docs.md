# API Documentation

## Connection Check

Checks if a connection can be established to a specified IP address and port.

- **URL:** `/connection/check`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "ip_address": "string",
    "port": "number"
  }
  ```
- **Success Response:**
  - **Code:** 200
  - **Content:** `{ "status": "Connection successful" }`
- **Error Response:**
  - **Code:** 400
  - **Content:** `{ "error": "IP address and port are required" }`
  - **Content:** `{ "status": "Connection failed", "error": "error message" }`

## Add User

Adds a new user to the system.

- **URL:** `/add_user`
- **Method:** `POST`
- **Request Body:**
  ```json
  {
    "user_name": "string"
  }
  ```
- **Success Response:**
  - **Code:** 201
  - **Content:** `{ "message": "User {user_name} added successfully" }`
- **Error Response:**
  - **Code:** 400
  - **Content:** `{ "error": "user_name is required" }`
  - **Code:** 500
  - **Content:** `{ "error": "error message" }`