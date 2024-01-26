from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import BankTransaction

class BankTransactionAPITests(TestCase):
    def setUp(self):
        # Set up an API client and sample transaction data for testing
        self.client = APIClient()
        self.transaction_data = {'account_number': '123456', 'transaction_amount': '100.00'}

    def test_create_transaction(self):
        # Test creating a new BankTransaction through the API
        # Assuming you have a URL name for the transaction list endpoint
        url = reverse('transaction-list') 
        response = self.client.post(url, data=self.transaction_data, format='json')

        # Check if the response indicates a successful creation
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check if the new transaction is saved in the database
        self.assertEqual(BankTransaction.objects.count(), 1)
        # Check if the account number matches the provided data
        self.assertEqual(BankTransaction.objects.get().account_number, '123456')

    def test_webhook_receiver(self):
        # Test the webhook_receiver view with valid transaction ID
        transaction = BankTransaction.objects.create(account_number='123456', transaction_amount='100.00')
        url = reverse('webhook_receiver')
        data = {'processed_data': 'some_data', 'transaction_id': transaction.id}

        # Send a POST request to simulate the webhook call
        response = self.client.post(url, data=data, format='json')

        # Check if the response indicates a successful processing
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the processed data is updated in the corresponding transaction
        self.assertEqual(BankTransaction.objects.get(id=transaction.id).processed_data, 'some_data')

    def test_webhook_receiver_transaction_not_found(self):
        # Test the webhook_receiver view with an invalid transaction ID
        url = reverse('webhook_receiver')
        # Assuming this ID does not exist
        data = {'processed_data': 'some_data', 'transaction_id': 999}

        # Send a POST request with an invalid transaction ID
        response = self.client.post(url, data=data, format='json')

        # Check if the response indicates a not found status
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
