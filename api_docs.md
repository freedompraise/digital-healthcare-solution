### Authentication Endpoints

#### 1. Obtain Token

- **Endpoint:** `/api/token/obtain`
- **Method:** POST
- **Description:** Obtain an authentication token by providing valid credentials.
- **Request Body:**

  - `email` (string): User's email address
  - `password` (string): User's password

- **Example Request:**
  ```json
  {
    "email": "user@example.com",
    "password": "securepassword"
  }
  ```
- **Example Response (Success):**

  ```json
  {
    "access": "eyJ0e...your_access_token_here...Fg",
    "refresh": "eyJ0e...your_refresh_token_here...Iw",
    "user_type": "PT"  # User type: "PT" for Patient or "HP" for Healthcare Provider
  }
  ```

- **Example Response (Error):**
  ```json
  {
    "detail": "Invalid credentials"
  }
  ```

#### 2. Refresh Token

- **Endpoint:** `/api/token/refresh`
- **Method:** POST
- **Description:** Refresh an expired authentication token by providing a valid refresh token.
- **Request Body:**

  - `refresh` (string): Refresh token obtained during the initial login.

- **Example Request:**

  ```json
  {
    "refresh": "eyJ0e...your_refresh_token_here...Iw"
  }
  ```

- **Example Response (Success):**

  ```json
  {
    "access": "eyJ0e...your_new_access_token_here...Fg"
  }
  ```

- **Example Response (Error):**
  ```json
  {
    "detail": "Token is invalid or expired"
  }
  ```

#### Registration

Endpoint: `/api/register/`  
Method: `POST`  
Description: Registers a new user (either patient or healthcare provider).

Request:

```json
{
  "name": "John Doe",
  "email": "example@email.com",
  "password": "your_password",
  "user_type": "PT" // Specify user type as "PT" for Patient or "HP" for Healthcare Provider
}
```

Response:

```json
{
  "message": "User registered successfully."
}
```

### User Profile Endpoints

#### Patient Profile

Endpoint: `/api/patients/{patient_id}/`  
Method: `GET`  
Description: Retrieves the profile of a patient.

#### Healthcare Provider Profile

Endpoint: `/api/healthcare-providers/{provider_id}/`  
Method: `GET`  
Description: Retrieves the profile of a healthcare provider.

### Usage in Frontend

Upon successful login, use the `user_type` from the token response to determine the type of user and direct them to the appropriate profile endpoint.

Example (JavaScript):

```javascript
// Assuming you have the authentication token and user type stored after login
const authToken = "your_authentication_token";
const userType = "PT"; // or "HP"

// Determine the profile endpoint based on user type
const profileEndpoint =
  userType === "PT" ? "/api/patients/" : "/api/healthcare-providers/";

// Fetch the user profile using the determined endpoint
fetch(profileEndpoint, {
  method: "GET",
  headers: {
    Authorization: `Bearer ${authToken}`,
    "Content-Type": "application/json",
  },
})
  .then((response) => response.json())
  .then((profileData) => {
    // Handle the user profile data
    console.log("User Profile Data:", profileData);
  })
  .catch((error) => {
    // Handle errors
    console.error("Error fetching user profile:", error);
  });
```
