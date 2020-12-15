# Django
from django.shortcuts import render
from django.core.mail import send_mail

# Django rest framework
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

# Serializers
from mail.serializers import MailSerializer

# Settings
from mailer.settings import EMAIL_HOST 


# Create your views here.
class SendMailAPIView(APIView):
    """
        Send Mail APIView
        This endpoint handles the incoming email request.
        Methods:
        - POST
        Serializer:
        - None
    """
    permission_classes = [AllowAny,]

    def post(self, request, *args, **kwargs):
        mail_serializer = MailSerializer(data=request.data)

        if mail_serializer.is_valid():
            try:
                send_mail(
                    f'{request.data.get("subject")}',
                    f'{request.data.get("message")}\n\nFrom: {request.data.get("name")} <{request.data.get("email")}>',
                    EMAIL_HOST,
                    ['edgar.omars.goze@gmail.com'],
                    fail_silently=False,
                )
                return Response(data={'success': True, 'message': 'Message sent successfully'}, status=status.HTTP_200_OK)
            except Exception as e:
                print(e)
                return Response(data={'success': False, 'message': 'Mail wasn\'t sent'}, status=status.HTTP_400_BAD_REQUEST)

        print(mail_serializer.erros)
        return Response(data={'success': False, 'message': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)
