ALX-CAPSTONE-PROJECT

Django Polls AppA simple yet fully functional web-based polling application built with Django. Users can create polls, vote on active polls (once per poll), and view real-time results. The app includes user authentication and prevents duplicate voting through a dedicated cote model. login, and logout functionality.
Only authenticated users can create polls and vote.

Features 
1.Poll ManagementAuthenticated users can create new polls with a question and multiple choices.
2.Polls can be marked as active or inactive.
3.VotingAuthenticated users can vote on active polls.
4.Each user can vote only once per poll (enforced via unique constraint on user_id + question_id).
5.ResultsReal-time vote counts displayed after voting or on a dedicated results page.


API REST API endpoints for polls, choices, and votes using Django REST Framewor

Database Schema (ER Diagram Summary)The application uses four main models:Questionid (Primary Key)
question_text (CharField)
pub_date (DateTimeField)
is_active (BooleanField)

Choiceid (Primary Key)
choice_text (CharField)
votes (IntegerField – cached vote count)
question_id (ForeignKey → Question)

UserBuilt-in Django User model extended or used as-is (fields: id, username, email, etc.)

Vote (tracks individual votes)id (Primary Key)
timestamp (DateTimeField)
user_id (ForeignKey → User)
question_id (ForeignKey → Question)
choice_id (ForeignKey → Choice)
Unique constraint: (user_id, question_id) – ensures one vote per user per poll

Project Structure

polls/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
├── models.py
├── tests.py
├── urls.py
├── views.py
├── templates/polls/
│   ├── index.html           
│   ├── detail.html          
│   ├── results.html        # Results page
│   └── ...
accounts/                       # Authentication views/templates
mysite/
├── settings.py
├── urls.py
├── wsgi.py
└── ...
manage.py

Requirements
Python 3.8+
Django 4.x or 5.x
(Optional) Django REST Framework for API endpoints



Django>=4.2
djangorestframework  # if API is implemented

Installation & SetupClone the repository:bash

git clone https://github.com/yourusername/django-polls-app.git
cd django-polls-app

Create a virtual environment:bash

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:bash

pip install -r requirements.txt

Apply migrations:bash

python manage.py makemigrations
python manage.py migrate

Create a superuser (for admin access):bash

python manage.py createsuperuser

Run the development server:bash

python manage.py runserver

Visit http://127.0.0.1:8000/polls/ to see the list of polls.

UsageRegister or log in at /accounts/signup/ or /accounts/login/.
Create a new poll via the admin panel (/admin/) or a dedicated create poll view.
Browse active polls on the home page and cast your vote.
View results immediately after voting or via the results link.

API Endpoints (if implemented)GET /api/polls/ – List all polls
GET /api/polls/<id>/ – Poll detail
POST /api/polls/<id>/vote/ – Submit a vote (authenticated)

Development Plan (Original Timeline)
Week 1: Planning and idea mapping
Week 2: ER Diagram design
Week 3: Authentication system
Week 4: Models, views, templates, and URL mapping
Week 5: Testing and deployment 



