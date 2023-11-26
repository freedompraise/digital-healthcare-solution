# API Documentation


### User Authentication and Authorization

#### Register User

- **Endpoint:** `/api/register/`
- **Method:** `POST`
- **Authentication:** Not required
- **Description:** Register a new user (either patient or healthcare provider).

**Request Body:**

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "your_secure_password",
  "user_type": "PT"  // Use "PT" for Patient or "HP" for Healthcare Provider
}
```

**Response:**

```json
{
  "message": "User registered successfully."
}
```

#### Obtain Authentication Token

- **Endpoint:** `/api/token/obtain/`
- **Method:** `POST`
- **Authentication:** Not required
- **Description:** Obtain an authentication token for an existing user.

**Request Body:**

```json
{
  "email": "john@example.com",
  "password": "your_secure_password"
}
```

**Response:**

```json
{
  "token": "your_access_token",
  "user_type": "PT"  // User type can be "PT" for Patient or "HP" for Healthcare Provider
}
```

#### Patient Detail

- **Endpoint:** `/api/patient/`
- **Method:** `GET`
- **Authentication:** Token-based (Include the obtained token in the request headers)
- **Description:** Retrieve details of the authenticated patient.

**Response (Success):**

```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "user_type": "PT",
}
```

**Response (Failure):**

```json
{
  "detail": "Authentication credentials were not provided."
}
```

#### Healthcare Provider Detail

- **Endpoint:** `/api/healthcare_provider/`
- **Method:** `GET`
- **Authentication:** Token-based (Include the obtained token in the request headers)
- **Description:** Retrieve details of the authenticated healthcare provider.

**Response (Success):**

```json
{
  "id": 1,
  "name": "Dr. Smith",
  "email": "dr.smith@example.com",
  "user_type": "HP",
  "clinic_affiliation": "General Hospital",
  "specialization": "Cardiology",
  "license_id_information": "12345"
}
```

**Response (Failure):**

```json
{
  "detail": "Authentication credentials were not provided."
}
```

#### Healthcare Provider Patients List

- **Endpoint:** `/api/healthcare_provider/patients/`
- **Method:** `GET`
- **Authentication:** Token-based (Include the obtained token in the request headers)
- **Description:** Retrieve a list of patients under the authenticated healthcare provider.

**Response (Success):**

```json
[
  {
    "id": 2,
    "name": "Jane Doe",
    "email": "jane@example.com",
    "user_type": "PT",
  },
  // Other patients...
]
```

**Response (Failure):**

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### Frontend Integration

- After obtaining the authentication token, store it securely in the frontend e.g., in a secure HTTP-only cookie.
- Use the stored token to authenticate API requests by including it in the `Authorization` header.
- Based on the returned user type during authentication, dynamically decide whether to call patient or healthcare provider endpoints.

If you have specific questions about the frontend implementation or need further clarification, feel free to ask!