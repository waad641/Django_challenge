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
