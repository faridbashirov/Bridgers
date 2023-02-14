from rest_framework import serializers
from .models import RequestQuote

class RequestQuoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = RequestQuote
        fields = 'name', 'email','services'
   