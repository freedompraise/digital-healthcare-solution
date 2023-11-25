### Authentication Endpoints

#### Login (Obtain Token)

Endpoint: `/api/login/`  
Method: `POST`  
Description: Obtains an authentication token for the user.

Request:

```json
{
  "username": "example@email.com",
  "password": "your_password"
}
```

Response:

```json
{
  "token": "your_authentication_token",
  "user_type": "PT" // User type can be "PT" (Patient) or "HP" (Healthcare Provider)
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
