import os

from django.urls import path
from django.views.generic import TemplateView

app_name = 'web'

urlpatterns = [
    path('send', TemplateView.as_view(
        template_name="web/send-gift.html",
        extra_context={
            'BACKEND_DARILKA_API': os.getenv("BACKEND_DARILKA_API"),
            'BACKEND_VERIFICATION_CODE_API': os.getenv("BACKEND_VERIFICATION_CODE_API")},
    )),
    path('receive', TemplateView.as_view(
        template_name="web/receive-gift.html",
        extra_context={
            'BACKEND_BOOK_API': os.getenv("BACKEND_BOOK_API"),
            'BACKEND_DARILKA_API': os.getenv("BACKEND_DARILKA_API")},
    )),
]
