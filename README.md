#Healthcare API Backend
This is the backend for a healthcare application, built with Django and Django REST Framework. It provides a secure API for managing user registration, patients, and doctors.

Local Setup and Installation
#1. Prerequisites
Python 3.x

PostgreSQL installed and running.

#2. Initial Setup
Clone the repository:

`git clone https://github.com/mudasirmattoo/healthcare-api-writebyte.git`
`cd healthcare-api-writebyte`

Create and activate a virtual environment:

# For macOS/Linux
`python -m venv env`
source env/bin/activate

# For Windows
`python -m venv env`
`.\env\Scripts\activate`

Install the required packages:

`pip install -r requirements.txt`

#3. Database and Environment Configuration
Set up the PostgreSQL database:

In the project's root directory, create a file named .env.

.env file contents:

`SECRET_KEY='your-strong-secret-key'
DB_NAME=healthcare_db
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_HOST=localhost
DB_PORT=5432`

#4. Final Steps
Run the database migrations:
`python manage.py makeigrations`
`python manage.py migrate`

Create a superuser (admin):
`python manage.py createsuperuser`

Run the server:
`python manage.py runserver`

The API will now be running at http://127.0.0.1:8000/.

API Endpoints
| Endpoint | Method | Description | Auth Required | Admin Required |
| :--- | :--- | :--- | :--- | :--- |
| `/api/auth/register/` | `POST` | Register a new user. | No | No |
| `/api/auth/login/` | `POST` | Log in to get a JWT access token. | No | No |
| `/api/patients/` | `GET` | Get a list of your patients. | Yes | No |
| `/api/patients/` | `POST` | Create a new patient. | Yes | No |
| `/api/patients/<id>/` | `GET` | Get details of a specific patient. | Yes | No |
| `/api/patients/<id>/` | `PUT` | Update a patient's details. | Yes | No |
| `/api/patients/<id>/` | `DELETE`| Delete a patient. | Yes | No |
| `/api/doctors/` | `GET` | Get a list of all doctors. | Yes | No |
| `/api/doctors/` | `POST` | Create a new doctor. | Yes | **Yes** |
| `/api/doctors/<id>/` | `PUT` | Update a doctor's details. | Yes | **Yes** |
| `/api/doctors/<id>/` | `DELETE`| Delete a doctor. | Yes | **Yes** |
| `/api/mappings/` | `POST` | Assign a doctor to one of your patients. | Yes | No |
| `/api/patients/<patient_id>/doctors/` | `GET` | Get all doctors assigned to a specific patient. | Yes | No |


Testing:
Use an API client like Postman for testing. I used postman

Register a user at http://127.0.0.1:8000/api/auth/register/ on browser.
<img width="1107" height="583" alt="image" src="https://github.com/user-attachments/assets/c7893736-fb05-48f8-9f22-d7b6a0e5718a" />
<img width="1105" height="530" alt="image" src="https://github.com/user-attachments/assets/2bcb963a-1dae-4be2-9e39-2ef6debe7b9e" />

a. Create a new POST request to http://127.0.0.1:8000/api/auth/login/
Go to the Body tab, select raw, and choose JSON from the dropdown.
You will get your JWT Access token and refresh token. Copy the access token.

This access token now needs to be sent with every request that follows.

b. Go to the Authorization tab, select Bearer Token from the Type dropdown, and paste your access token into the Token field.

c. Create a Patient (POST /api/patients/)

Log in at /api/auth/login/ with the user's credentials to get an access token.

For all other requests, go to the Authorization tab in Postman, select Bearer Token, and paste the access token.
