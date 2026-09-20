from rest_framework import serializers
from .models import QuoteRequest

class QuoteRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteRequest
        fields = ['id','full_name','email','phone','service','project_location','message','status','created_at']
        read_only_fields = ['id','status','created_at']

    def validate_full_name(self, value):
        value = value.strip()
        if len(value) < 2:
            raise serializers.ValidationError('Please provide your full name.')
        return value

    def validate_phone(self, value):
        value = value.strip()
        if len(value) < 7:
            raise serializers.ValidationError('Please provide a valid phone number.')
        return value

    def validate_message(self, value):
        value = value.strip()
        if len(value) < 10:
            raise serializers.ValidationError('Please provide more detail about the project.')
        return value
