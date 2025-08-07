##Healthcare API Backend
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

Step 1: Register a user at http://127.0.0.1:8000/api/auth/register/ on browser.
<img width="1107" height="583" alt="image" src="https://github.com/user-attachments/assets/c7893736-fb05-48f8-9f22-d7b6a0e5718a" />
<img width="2444" height="1172" alt="1" src="https://github.com/user-attachments/assets/c8c89d96-dec4-4282-8cf5-0bb66edb15ed" />

a. Create a new POST request to http://127.0.0.1:8000/api/auth/login/
Go to the Body tab, select raw, and choose JSON from the dropdown.
You will get your JWT Access token and refresh token. Copy the access token.
<img width="1734" height="1234" alt="login" src="https://github.com/user-attachments/assets/e58fc2cd-bcdb-41aa-839b-3d5d6e2e52e6" />

This access token now needs to be sent with every request that follows.

b. Go to the Authorization tab, select Bearer Token from the Type dropdown, and paste your access token into the Token field.

Step 2: a. Create a Patient (POST /api/patients/)
<img width="1107" height="748" alt="image" src="https://github.com/user-attachments/assets/897d26ac-d6f3-45d9-b72a-3e47d1b20487" />

b. Get All Your Patients (GET /api/patients/)
<img width="1104" height="775" alt="image" src="https://github.com/user-attachments/assets/6fa731f7-16f5-4583-9f2b-48a114f041cb" />

c. Update a Patient (PUT /api/patients/<id>/)
<img width="1104" height="748" alt="image" src="https://github.com/user-attachments/assets/2ab76570-caad-4cb6-af29-f29eb86b40ef" />

Step 3: Doctor & Mapping APIs (As an Admin)
Log in as Admin: Repeat Step 1, but use the username and password for the superuser you created. Copy the new admin access token.

a. Create a Doctor (POST /api/doctors/)
<img width="1801" height="1220" alt="access key" src="https://github.com/user-attachments/assets/08441e23-9368-48a8-9026-494e03e46067" />
<img width="1106" height="750" alt="image" src="https://github.com/user-attachments/assets/1814c6a8-abd1-4013-8ec3-9d37f91e5c94" />

b. Assign a Doctor to a Patient (POST /api/mappings/)
<img width="1104" height="728" alt="image" src="https://github.com/user-attachments/assets/56eaf69b-84fd-46b9-b65e-aa25094863c4" />

Step 4: To get the mapping details (GET /api/mappings/<mapping_id>/)
<img width="1104" height="745" alt="image" src="https://github.com/user-attachments/assets/d38f1fe1-f631-4dc8-b41d-6cc2cee71489" />

Step 5: GET /api/patients/<patient_id>/doctors/ - Get all doctors assigned to a specific patient
<img width="1107" height="743" alt="image" src="https://github.com/user-attachments/assets/b435269e-9210-44d1-ba37-34a017c9d653" />

