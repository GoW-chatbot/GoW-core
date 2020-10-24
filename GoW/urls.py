from django.conf.urls import include
from django.urls import path


urlpatterns = [
    path('', include('chat.urls')),
    path('chatAPI/', include('chatbotAPI.urls')),
]
