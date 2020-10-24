from django.shortcuts import render

def chatbot(request):
    return render(request, 'chat/chatbot.html')
    
