from rest_framework import serializers
from .models import BankTransaction

class BankTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        # Define the serializer's meta information
        model = BankTransaction  # Specify the model to be serialized
        fields = '__all__'  # Serialize all fields present in the BankTransaction model



# This serializer is using the Django Rest Framework's ModelSerializer.
# It automatically generates serialization logic based on the BankTransaction model.

# Meta class is used to provide additional information to the serializer.
# In this case, it specifies the model to be serialized (BankTransaction) and 
# indicates that all fields from the model should be included in the serialization.
