# Django rest framwork
from rest_framework import serializers

class MailSerializer(serializers.Serializer):

    name = serializers.RegexField(
        regex="([a-zA-Z][:blank][a-zA-Z])|^([a-zA-z])",
        min_length=4,
        allow_blank=False
    )

    email = serializers.RegexField(
        regex="[a-z0-9._%+-]+@[a-z0-9.-]+[\\.][a-z]{2,}$",
        allow_blank=False
    )

    subject = serializers.CharField(
        min_length=10,
        allow_blank=False
    )

    message = serializers.CharField(
        min_length=20,
        allow_blank=False
    )
