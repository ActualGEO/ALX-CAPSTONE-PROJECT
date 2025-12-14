ALX-CAPSTONE-PROJECT

Django Polls App 🗳️

[![Django](https://img.shields.io/badge/Django-5.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple, fully functional polling web application built with Django. Users can create polls, vote once per poll, and view real-time results. Includes user authentication and proper vote tracking to prevent duplicates.

Inspired by the official Django tutorial but extended with authentication and one-vote-per-user enforcement.

## Table of Contents

- [Features](#features)
- [Database Schema](#database-schema)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [API (Planned)](#api-planned)
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

- **Admin Panel**
  - Full CRUD for polls via Django admin.

## Database Schema

The app uses four core models:

1. **Question** – Poll question, publication date, active status.
2. **Choice** – Options with cached vote count.
3. **User** – Django's built-in User model.
4. **Vote** – Tracks individual votes with timestamp and unique constraint `(user_id, question_id)`.

(See your ER diagram for relationships.)

## Project Structure

polls_app/
├── polls/
│   ├── models.py
│   ├── views.py
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

## Requirements

- Python 3.10+
- Django 5.0+

```txt
Django>=5.0
# djangorestframework  # Uncomment when adding API

Installation & SetupClone the repo:bash

git clone https://github.com/yourusername/django-polls-app.git
cd django-polls-app

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

Visit http://127.0.0.1:8000/polls/ to see your polls!UsageSign up / log in.
Create polls via admin or future create view.
Vote on active polls.
View results instantly.

API (Planned)Planning to add REST API endpoints using Django REST Framework for:Listing polls
Voting via POST
Results retrieval

Development TimelineWeek 1: Planning & ideas
Week 2: ER Diagram
Week 3: Authentication
Week 4: Models, views, templates
Week 5: Testing & debugging

ContributingContributions welcome! Fork, create a branch, and submit a pull request.LicenseMIT License (LICENSE) – free to use and modify.

This will render beautifully on GitHub—the TOC links will jump straight to sections when clicked. GitHub also adds an automatic sidebar TOC for extra navigation.

If you add screenshots later, place them in the Features or Usage section for even more impact.

Let me know if you want to add anything else (like a demo GIF placeholder or more badges)! 🚀

34 web pages

