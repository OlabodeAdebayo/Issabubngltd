from rest_framework import serializers

from .models import QuoteRequest


class QuoteRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuoteRequest

        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "service",
            "project_location",
            "message",
            "status",
            "created_at",
            "email_sent",
            "email_sent_at",
        ]

        read_only_fields = [
            "id",
            "status",
            "created_at",
            "email_sent",
            "email_sent_at",
        ]

    def validate_full_name(self, value):
        value = value.strip()

        if len(value) < 2:
            raise serializers.ValidationError(
                "Please provide your full name."
            )

        return value

    def validate_email(self, value):
        value = value.strip().lower()

        if not value:
            raise serializers.ValidationError(
                "Please provide your email address."
            )

        return value

    def validate_phone(self, value):
        value = value.strip()

        if len(value) < 7:
            raise serializers.ValidationError(
                "Please provide a valid phone number."
            )

        return value

    def validate_service(self, value):
        value = value.strip()

        if not value:
            raise serializers.ValidationError(
                "Please select a service."
            )

        return value

    def validate_project_location(self, value):
        return value.strip()

    def validate_message(self, value):
        value = value.strip()

        if len(value) < 10:
            raise serializers.ValidationError(
                "Please provide more detail about the project."
            )

        return value
