LITTLE LEMON RESTAURANT API - BACK-END DEVELOPER CAPSTONE

Requirements
- Python 3.11
- pipenv
- MySQL Server
- Insomnia REST client (for manual API checks)

SETUP
1. Create a MySQL database:
   CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

2. Open this folder in VS Code. In the terminal:
   pipenv install
   pipenv shell

3. Configure MySQL credentials before running Django.

Windows PowerShell:
   $env:DB_NAME="littlelemon"
   $env:DB_USER="root"
   $env:DB_PASSWORD="YOUR_MYSQL_PASSWORD"
   $env:DB_HOST="127.0.0.1"
   $env:DB_PORT="3306"

macOS/Linux:
   export DB_NAME=littlelemon
   export DB_USER=root
   export DB_PASSWORD='YOUR_MYSQL_PASSWORD'
   export DB_HOST=127.0.0.1
   export DB_PORT=3306

4. Apply database migrations and run tests:
   python manage.py makemigrations
   python manage.py migrate
   python manage.py test

5. Start server:
   python manage.py runserver

Browser
- Home: http://127.0.0.1:8000/
- Menu API: http://127.0.0.1:8000/api/menu/
- Bookings API: http://127.0.0.1:8000/api/bookings/
- Registration: http://127.0.0.1:8000/api/register/
- Obtain token: http://127.0.0.1:8000/api-token-auth/
- Current user: http://127.0.0.1:8000/api/users/me/
- Django admin: http://127.0.0.1:8000/admin/

API ENDPOINTS FOR INSOMNIA

1. GET /api/menu/
   Public. Lists menu items (paginated).

2. GET /api/menu/{id}/
   Public. Gets one menu item.

3. POST /api/menu/
   Authenticated. JSON body example:
   {"title":"Greek Salad","price":"12.50","inventory":10}

4. PUT /api/menu/{id}/
   Authenticated. Update a menu item with all fields.

5. PATCH /api/menu/{id}/
   Authenticated. Update selected fields.

6. DELETE /api/menu/{id}/
   Authenticated. Delete a menu item.

7. POST /api/register/
   Public. JSON body:
   {"username":"student1","email":"student1@example.com","password":"StrongPass123"}
   Returns a user record and token.

8. POST /api-token-auth/
   JSON body:
   {"username":"student1","password":"StrongPass123"}
   Returns {"token":"..."}.

9. GET /api/users/me/
   Header:
   Authorization: Token YOUR_TOKEN

10. GET /api/bookings/
    Authenticated. Lists the current user's bookings. Staff users can list all bookings.

11. POST /api/bookings/
    Authenticated. JSON body:
    {"name":"Student","no_of_guests":2,"booking_date":"2030-01-01T19:00:00Z"}

12. GET /api/bookings/{id}/
    Authenticated. Retrieves a booking visible to the current user.

13. PUT/PATCH /api/bookings/{id}/
    Authenticated. Updates a booking visible to the current user.

14. DELETE /api/bookings/{id}/
    Authenticated. Deletes a booking visible to the current user.

AUTHENTICATION
Use the registration endpoint or create a user with:
python manage.py createsuperuser
Then POST username/password to /api-token-auth/. For protected endpoints, set header:
Authorization: Token YOUR_TOKEN

GITHUB SUBMISSION
- Commit all project files, including this Readme.txt, and push them to GitHub.
- Do not commit passwords, secret keys, virtual environments, or database files.
- Paste the GitHub repository URL in Coursera's submission form.

NOTE
This is a self-contained capstone implementation prepared from the assignment rubric, not the original course starter repository. Run and test it locally with your MySQL setup before submitting. If your course's provided starter code expects different endpoint names or additional features, adapt the routes accordingly.
