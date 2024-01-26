Consumer App Documentation

Overview:
The Consumer App is responsible for receiving bank transaction data from the Producer App, processing it asynchronously using Celery, and updating the database with the processed results. It communicates with the Producer App through API calls.

Components:

Tasks:

process_bank_transaction: Asynchronous Celery task that processes bank transaction data and updates the database.
Views:

webhook_receiver: Django REST Framework view that handles incoming POST requests from the Producer App and triggers the Celery task.
Models:

BankTransaction: Django model representing bank transactions with fields like account number, transaction amount, transaction date, and processed data.
API Endpoints:

/api/webhook_receiver/: POST endpoint for receiving transaction data from the Producer App.
Tests:

Unit tests for views and Celery tasks are available in tests.py.
Settings:

Celery is configured in tasks.py.
Usage:

Run Celery worker: celery -A consumer_project worker -l info
Start Django development server: python manage.py runserver
