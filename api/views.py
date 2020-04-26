from django.shortcuts import render

from api.models import User, Question
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from api.serializers import UserSer, QuestionSer

@api_view(['GET', 'POST'])
def questions(request):
    if request.method == 'POST':
        user = User.objects.get(name=request.data.get('author'))
        Question.objects.create(
            user = user,
            title = request.data.get('title'),
            text = request.data.get('text')
        )
        return JsonResponse({"":""},safe=False)

    elif request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSer(questions, many=True)
        return JsonResponse(serializer.data, safe=false)

