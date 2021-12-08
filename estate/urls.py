from django.urls import path
from . import views

urlpatterns = [
    path('soumettre-propriete/', views.SubmitPropretyView.as_view(), name='submit_property'),
]