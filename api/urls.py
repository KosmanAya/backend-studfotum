from django.urls import path 
from api import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('questions/', views.questions),
    path('questions/<int:id>/', views.like),
    path('admin/<int:id>/', views.AdminView.as_view()),
    path('answers/', views.AnswerVi.as_view()),
    path('login/', obtain_jwt_token)
    
]