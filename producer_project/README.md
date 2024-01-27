# Overview:
The Producer App generates and sends bank transaction data to the Consumer App through API calls. It provides API endpoints to submit transactions and retrieve processed results.

# Components:

   # Models:

BankTransaction: Django model representing bank transactions with fields like account number, transaction amount, transaction date, and processed data.
Serializers:

BankTransactionSerializer: Serializes BankTransaction model for API responses.
Views:

BankTransactionViewSet: Django REST Framework viewset for managing bank transactions.
webhook_receiver: Django REST Framework view that handles incoming POST requests from the Consumer App.
# API Endpoints:

    /api/transactions/: RESTful API endpoint for managing bank transactions.
    /api/webhook_receiver/: 'POST' endpoint for sending processed data back to the Consumer App.
# Tests:

  Unit tests for API views and webhook handling are available in tests.py.
# Settings:

   Celery is configured in tasks.py.
# Usage:

on a teminal :
   1/create a virtual environment : 
   
    python -m venv venv_producer
    
  2/Activate the virtual environment :
  
    venv\Scripts\activate  //// if on Unix or MacOS : source venv/bin/activate
    
 3/Install dependencies :
 
   pip install Djangorestframework celery django-celery_results requests
   
 4/create Django project and application 
 
   django-admin startproject producer_project
   
 5/locate to the created project 
 
   cd producer_project 
   
 6/ open the code on vscode :
 
   . code 

# RabbitMQ downloading :

before downloadingt rabbitMQ , 
just make sure you have successfully installed Erlang/OTP from   https://www.erlang.org/downloads
after configuring Erlang/OTP (run the .exe file ) you can inastall the RabbitMQ 
from  https://www.rabbitmq.com/download.html
  to make sure rabbitMQ is installed successfuly , open rabbitMQ Server -start and run this command:

    rabbitmqctl status
         
# Run migrations : 
    python manage.py makemigrations 
    python manage.py migrate
    
# Start Django development server: 
    python manage.py runserver
# versions:
   python : 3.11.5
   
   django : 5.0.1
   
   celery : 5.3.6

   rabbitMQ : 3.12.12.0
   
   Erlang/OTP : 26.2.1.0
