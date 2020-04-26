from django.urls import path 
from api import views

urlpatterns = [
    path('questions/', views.questions),
    path('answers/', views.AnswerVi.as_view()),
    
]