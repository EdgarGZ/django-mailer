# Django
from django.urls import path, include

# Views
import mail.views as views

# ApiView urls
app_name='mail'
apiview_urls = [
    path(
        route='send/mail/',
        view=views.SendMailAPIView.as_view(),
        name='send_mail'
    ),
]

urlpatterns = apiview_urls
