from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import BankTransaction
from .serializers import BankTransactionSerializer
from django.shortcuts import render

# existing DRF viewset for transactions
class BankTransactionViewSet(viewsets.ModelViewSet):
    queryset = BankTransaction.objects.all()
    serializer_class = BankTransactionSerializer

# API view for receiving webhooks
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def webhook_receiver(request):
    # Extract processed data and transaction ID from the request
    processed_data = request.data.get('processed_data')
    transaction_id = request.data.get('transaction_id')

    try:
        # Retrieve the corresponding transaction from the database
        transaction = BankTransaction.objects.get(id=transaction_id)
        # Update the transaction's processed data
        transaction.processed_data = processed_data
        transaction.save()
        return JsonResponse({'status': 'success'})
    except BankTransaction.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Transaction not found'})

# New DRF API view for listing transactions
class TransactionListView(APIView):
    # Set permission classes to enforce authentication
    permission_classes = [IsAuthenticated]

    # Handle GET requests to retrieve and serialize all transactions
    def get(self, request):
        transactions = BankTransaction.objects.all()
        serializer = BankTransactionSerializer(transactions, many=True)
        return Response(serializer.data)

# Your existing HTML rendering view for transaction list
def transaction_list_html(request):
    # Retrieve all transactions from the database
    transactions = BankTransaction.objects.all()
    # Render the HTML template with the transactions
    return render(request, 'producer_app/transaction_list.html', {'transactions': transactions})
