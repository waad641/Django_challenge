# Import necessary modules and classes from Django and DRF(Django Rest Framework)
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import BankTransaction
from .serializers import BankTransactionSerializer
from django.shortcuts import render

# Define a DRF viewset for transactions using ModelViewSet
class BankTransactionViewSet(viewsets.ModelViewSet):
    
    # Set the queryset to include all BankTransaction objects
    queryset = BankTransaction.objects.all()
    
    # Set the serializer class for serialization/deserialization
    serializer_class = BankTransactionSerializer

# Define an API view for receiving webhooks via 'POST' request
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def webhook_receiver(request):
    # Extract processed data and transaction ID from the request data
    processed_data = request.data.get('processed_data')
    transaction_id = request.data.get('transaction_id')

    try:
        # Retrieve the corresponding transaction from the database
        transaction = BankTransaction.objects.get(id=transaction_id)
        
        # Update the transaction's processed data
        transaction.processed_data = processed_data
        transaction.save()
        
        # Respond with a JSON success message
        return JsonResponse({'status': 'success'})
    except BankTransaction.DoesNotExist:
        
        # Respond with a JSON error message if the transaction is not found
        return JsonResponse({'status': 'error', 'message': 'Transaction not found'})

# Define a new DRF API view for listing transactions
class TransactionListView(APIView):
    # Set permission classes to enforce authentication
    permission_classes = [IsAuthenticated]

    # Handle 'GET' requests to retrieve and serialize all transactions
    def get(self, request):
        # Retrieve all transactions from the database
        transactions = BankTransaction.objects.all()
        # Serialize transactions using the specified serializer
        serializer = BankTransactionSerializer(transactions, many=True)
        # Respond with the serialized data in the API response
        return Response(serializer.data)

# The existing HTML rendering view for the transaction list
def transaction_list_html(request):
    # Retrieve all transactions from the database
    transactions = BankTransaction.objects.all()
    # Render the HTML template with the transactions
    return render(request, 'producer_app/transaction_list.html', {'transactions': transactions})

