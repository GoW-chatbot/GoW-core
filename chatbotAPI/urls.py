from django.urls import path
from chatbotAPI import views

urlpatterns = [
    path('predict/', views.predict_answer, name='chatbotAPI'),
]