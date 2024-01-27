# Django challenge :
The project is a Django-based web application that facilitates asynchronous 
communication between a Consumer App and a Producer App through RESTful APIs. 
The Consumer App is responsible for receiving and processing bank transaction data 
sent by the Producer App. It utilizes Celery for asynchronous task processing and
updates its database with the processed results. The Producer App generates and 
sends bank transaction data to the Consumer App through API calls, offering 
endpoints for submitting transactions and retrieving processed information. The
seamless interaction between these two apps showcases a distributed system 
architecture, providing a flexible and scalable solution for handling financial 
transactions. The project aims to demonstrate best practices in Django development
API integration, and asynchronous task execution.

This repository focus on the :
# Producer App:

   1/Web Server: Manages incoming HTTP requests.
Exposes API endpoints for CRUD operations on transactions.
Listens to a webhook endpoint for processed data from the Consumer App.

   2/Django REST Framework (DRF):
Implements a viewset for CRUD operations on transactions.
Implements a webhook receiver to update transactions with processed data.

  3/Django Database:
Stores transaction data.

   4/Celery Worker:
Performs asynchronous processing for tasks initiated by the Consumer App.
# Communication Flow:

*User interacts with the Consumer App's web interface.
*Consumer App sends transaction data to the Producer App for storage.
*Producer App stores the transaction in the database and initiates asynchronous processing.
*Celery worker in the Consumer App processes the transaction asynchronously.
*Once processing is complete, the Celery worker in the Consumer App sends processed data to the Producer App's webhook.
*Producer App updates the transaction in the database with the processed data.

# External Services:

  1/Celery Broker (RabbitMQ ):
  
Manages the message queue for Celery tasks.

  2/Django Database Server:
  
Hosts the databases for both Consumer and Producer Apps.
