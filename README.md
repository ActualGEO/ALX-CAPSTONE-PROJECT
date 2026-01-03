ALX-CAPSTONE-PROJECT

Django Polls App 🗳️

[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, fully functional polling web application built with Django. Users can create polls, vote once per poll, and view real-time results. Includes user authentication, proper vote tracking, and a **REST API** built with Django REST Framework.

Inspired by the official Django tutorial but extended with authentication, one-vote-per-user enforcement, and API endpoints.

## Table of Contents

- [Features](#features)
- [Models](#models)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Development Timeline](#development-timeline)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication**
  - Register, login, and logout.
  - Only authenticated users can create polls and vote.

- **Poll Management**
  - Create polls with a question and multiple choices.
  - Polls can be active or inactive.

- **Voting**
  - One vote per user per poll (enforced by unique constraint).
  - Real-time vote updates.

- **Results**
  - View vote counts and percentages after voting.

- **REST API**
  - Full CRUD for polls and secure voting via API.
  - Token or session authentication.

- **Admin Panel**
  - Full CRUD for polls via Django admin.

## Models

Here are the core Django models:

```python
# polls/models.py

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # Cached vote count

    def __str__(self):
        return self.choice_text

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'question')
        constraints = [
            models.UniqueConstraint(fields=['user', 'question'], name='unique_vote_per_user_per_question')
        ]

    def __str__(self):
        return f"{self.user.username} voted '{self.choice}' on '{self.question}'"

Database SchemaFour core entities:Question – Poll question, publication date, active status.
Choice – Options with cached vote count (FK to Question).
User – Django's built-in User model.
Vote – Individual votes with unique constraint (user_id, question_id).

API EndpointsThe app includes a REST API powered by Django REST Framework.AuthenticationUses TokenAuthentication (or SessionAuthentication for browsable API).
Register and obtain token via /api/auth/ (or use DRF's built-in token view).

EndpointsMethod
Endpoint
Description
Authentication Required
GET
/api/polls/
List all active polls
No
GET
/api/polls/<id>/
Retrieve a specific poll with choices
No
GET
/api/polls/<id>/results/
Get vote results for a poll
No
POST
/api/polls/
Create a new poll (admin/user)
Yes
POST
/api/polls/<id>/vote/
Submit a vote (choice_id required)
Yes
GET
/api/users/me/votes/
List polls the current user has voted on
Yes

Example Vote Request (POST):json

{
  "choice_id": 3
}

Response on success:json

{
  "detail": "Vote recorded successfully.",
  "results": {
    "choice_text": "Option A",
    "votes": 12,
    "percentage": 60.0
  },
  "total_votes": 20
}

The browsable API is available at the same endpoints when running the development server.Project Structure

polls_app/
├── polls/
│   ├── models.py
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # Includes API views
│   ├── urls.py
│   ├── templates/polls/
│   └── ...
├── accounts/                   # Authentication app
├── mysite/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── manage.py
└── requirements.txt

Requirements
Python 3.14
Django 6.0
Django REST Framework




djangorestframework>=3.14

Installation & Adding the repo:bash

git remote add origin https://github.com/ActualGEO/ALX-CAPSTONE-PROJECT.git
git branch -M main
git push -u origin main


Set up virtual environment:bash

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

Install dependencies:bash

pip install -r requirements.txt

Run migrations:bash

python manage.py makemigrations
python manage.py migrate

Create superuser:bash

python manage.py createsuperuser

Start server:bash

python manage.py runserver

Web app: http://127.0.0.1:8000/polls/
API root: http://127.0.0.1:8000/api/

UsageSign up / log in via web or API.
Create polls via admin or API.
Vote through the web interface or API.
View results instantly.

Development TimelineWeek 1: Planning & ideas
Week 2: ER Diagram
Week 3: Authentication
Week 4: Models, views, templates
Week 5: Testing & debugging
Extra: API implementation with DRF

