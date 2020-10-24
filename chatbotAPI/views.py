
#Importing necessary libraries for making the API
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render


#Importing the model
def predict(question):
    return "please use a model"


@api_view(['GET'])
def index_page(request):
    return_data = {
        "error" : "0",
        "message" : "Successful",
    }
    return Response(return_data)

@api_view(["POST"])
def predict_answer(request):
    try:
        question = request.data.get('question',None)
        fields = [question]
        if not None in fields:
            answer = predict(question)
            predictions = {
                'error' : '0',
                'message' : 'Successfull',
                'question': question,
                'answer' : answer,
            }
        else:
            predictions = {
                'error' : '1',
                'message': 'Invalid Parameters'                
            }
    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }
    
    return Response(predictions)
