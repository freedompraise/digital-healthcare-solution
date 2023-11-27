# Digital Healthcare Solution API

## Overview

This repository contains the backend code for the Digital Healthcare Solution API. It is built using Django and Django REST Framework to provide functionality for user registration, authentication, and various endpoints for patients and healthcare providers.

## Features

- User registration for patients and healthcare providers.
- Token-based authentication for secure API access.
- Endpoints for retrieving details of authenticated patients and healthcare providers.
- Endpoint for healthcare providers to retrieve a list of patients under their care.

## Prerequisites

- Python 3.x
- Django 3.x
- Django REST Framework
- cloudinay api

## Getting Started

1. Clone the repository:

```bash
git clone https://github.com/freedompraise/digital-healthcare-solution.git
cd digital-healthcare-solution
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure your environment:

   - Copy the `.env.example` file to `.env` and set the necessary environment variables.

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

The API will be accessible at `http://127.0.0.1:8000/`.

## API Endpoints

The details of the endpoints can be found in the [API_DOCUMENTATION](/api_docs.md)

## Frontend Integration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
