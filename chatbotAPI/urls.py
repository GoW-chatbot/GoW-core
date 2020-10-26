from django.urls import path
from chatbotAPI import views

# The URL of the API
urlpatterns = [
    path('predict/', views.predict_answer, name='chatbotAPI'),
]