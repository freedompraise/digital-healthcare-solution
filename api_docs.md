# Medication Adherence API Documentation

## Register User

### `POST /register/`

Create a new user (either a patient or healthcare provider).

#### Request

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "securepassword",
  "user_type": "PT"
}
```

- `name` (string): Full name of the user.
- `email` (string): Email address of the user.
- `password` (string): User's password.
- `user_type` (string): User type, either "PT" for Patient, "HP" for Healthcare Provider, or "AD" for Administrator.

#### Response

```json
{
  "message": "Patient registered successfully."
}
```

---

## Obtain Token

### `POST /token/obtain`

Obtain an access token by providing valid credentials.

#### Request

```json
{
  "email": "john.doe@example.com",
  "password": "securepassword"
}
```

#### Response

```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9...",
  "user_type": "PT"
}
```

- `access` (string): JWT access token.
- `refresh` (string): JWT refresh token.
- `user_type` (string): Type of the user.

---

## Patient Detail

### `GET /patient/`

Retrieve details of the logged-in patient.

#### Response

```json
{
  "user": {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone_number": "+1234567890",
    "date_of_birth": "1990-01-01",
    "address": "123 Main St",
    "gender": "M",
    "profile_picture": "/images/profile.jpg",
    "user_type": "PT"
  },
  "healthcare_provider": {
    "user": {
      "name": "Dr. Smith",
      "email": "dr.smith@example.com",
      "phone_number": "+9876543210",
      "date_of_birth": "1975-05-15",
      "address": "456 Oak St",
      "gender": "F",
      "profile_picture": "/images/doctor.jpg",
      "user_type": "HP"
    },
    "clinic_affiliation": "City Hospital",
    "specialization": "Cardiology",
    "license_id": "12345"
  },
  "allergies": "Peanuts"
}
```

- `user` (object): Patient's user details.
- `healthcare_provider` (object): Healthcare provider's details associated with the patient.
- `allergies` (string): Patient's allergies.

---

## Healthcare Provider Detail

### `GET /healthcare-provider/`

Retrieve details of the logged-in healthcare provider.

#### Response

```json
{
  "user": {
    "name": "Dr. Smith",
    "email": "dr.smith@example.com",
    "phone_number": "+9876543210",
    "date_of_birth": "1975-05-15",
    "address": "456 Oak St",
    "gender": "F",
    "profile_picture": "/images/doctor.jpg",
    "user_type": "HP"
  },
  "clinic_affiliation": "City Hospital",
  "specialization": "Cardiology",
  "license_id": "12345"
}
```

- `user` (object): Healthcare provider's user details.
- `clinic_affiliation` (string): Affiliated clinic of the healthcare provider.
- `specialization` (string): Specialization of the healthcare provider.
- `license_id` (string): License ID of the healthcare provider.

---

## Healthcare Provider Patients

### `GET /healthcare-provider/patients/`

Retrieve a list of patients associated with the logged-in healthcare provider.

#### Response

```json
[
  {
    "user": {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "phone_number": "+1234567890",
      "date_of_birth": "1990-01-01",
      "address": "123 Main St",
      "gender": "M",
      "profile_picture": "/images/profile.jpg",
      "user_type": "PT"
    },
    "healthcare_provider": {
      "user": {
        "name": "Dr. Smith",
        "email": "dr.smith@example.com",
        "phone_number": "+9876543210",
        "date_of_birth": "1975-05-15",
        "address": "456 Oak St",
        "gender": "F",
        "profile_picture": "/images/doctor.jpg",
        "user_type": "HP"
      },
      "clinic_affiliation": "City Hospital",
      "specialization": "Cardiology",
      "license_id": "12345"
    },
    "allergies": "Peanuts"
  }
  // Additional patient objects
]
```

- List of patient objects, each containing user details, associated healthcare provider details, and patient's allergies.

---

## Update

Patient Details

### `PUT /patient/`

Update details of the logged-in patient.

#### Request

```json
{
  "user": {
    "phone_number": "+1234567890",
    "address": "456 Oak St",
    "profile_picture": "/images/new_profile.jpg"
  },
  "healthcare_provider": {
    "clinic_affiliation": "City Hospital",
    "specialization": "Cardiology",
    "license_id": "54321"
  },
  "allergies": "Tree nuts"
}
```

- Updated patient details.

#### Response

```json
{
  "user": {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "phone_number": "+1234567890",
    "date_of_birth": "1990-01-01",
    "address": "456 Oak St",
    "gender": "M",
    "profile_picture": "/images/new_profile.jpg",
    "user_type": "PT"
  },
  "healthcare_provider": {
    "user": {
      "name": "Dr. Smith",
      "email": "dr.smith@example.com",
      "phone_number": "+9876543210",
      "date_of_birth": "1975-05-15",
      "address": "456 Oak St",
      "gender": "F",
      "profile_picture": "/images/doctor.jpg",
      "user_type": "HP"
    },
    "clinic_affiliation": "City Hospital",
    "specialization": "Cardiology",
    "license_id": "54321"
  },
  "allergies": "Tree nuts"
}
```

- Updated patient details.

---

## Update Healthcare Provider Details

### `PUT /healthcare-provider/`

Update details of the logged-in healthcare provider.

#### Request

```json
{
  "user": {
    "phone_number": "+9876543210",
    "address": "789 Elm St",
    "profile_picture": "/images/new_doctor.jpg"
  },
  "clinic_affiliation": "County Hospital",
  "specialization": "Orthopedics",
  "license_id": "ABCDE"
}
```

- Updated healthcare provider details.

#### Response

```json
{
  "user": {
    "name": "Dr. Smith",
    "email": "dr.smith@example.com",
    "phone_number": "+9876543210",
    "date_of_birth": "1975-05-15",
    "address": "789 Elm St",
    "gender": "F",
    "profile_picture": "/images/new_doctor.jpg",
    "user_type": "HP"
  },
  "clinic_affiliation": "County Hospital",
  "specialization": "Orthopedics",
  "license_id": "ABCDE"
}
```

- Updated healthcare provider details.

---

## List Healthcare Providers

### `GET /healthcare-providers/`

List healthcare providers associated with the logged-in patient.

#### Response

```json
[
  {
    "user": {
      "name": "Dr. Smith",
      "email": "dr.smith@example.com",
      "phone_number": "+9876543210",
      "date_of_birth": "1975-05-15",
      "address": "789 Elm St",
      "gender": "F",
      "profile_picture": "/images/new_doctor.jpg",
      "user_type": "HP"
    },
    "clinic_affiliation": "County Hospital",
    "specialization": "Orthopedics",
    "license_id": "ABCDE"
  }
  // Additional healthcare provider objects
]
```

- List of healthcare provider objects, each containing user details, clinic affiliation, specialization, and license ID.

---

## Important Notes

- All requests to protected endpoints must include a valid JWT token in the Authorization header.
- Tokens can be obtained by calling the `/token/obtain` endpoint with valid credentials.
- Tokens have a limited lifespan and can be refreshed using the `/token/refresh` endpoint.

---
