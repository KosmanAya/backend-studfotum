from django.shortcuts import render

from api.models import User, Question, Answer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from api.serializers import UserSer, QuestionSer, AnswerSer
from rest_framework.views import APIView
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
        return JsonResponse(serializer.data, safe=False)


class AnswerVi(APIView):
    def post(self, request):
        question = Question.objects.get(id=request.data.get('question'))
        user = User.objects.get(name=request.data.get('author'))
        Answer.objects.create(
            question = question,
            user = user,
            text = request.data.get('text')
        )
        return JsonResponse({"":""},safe=False)

    def get(self, request):
        answers = Answer.objects.all()
        serializer = AnswerSer(answers, many=True)
        return JsonResponse(serializer.data, safe=False)