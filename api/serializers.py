from rest_framework import serializers
from api import models

class UserSer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = 'id','name','email','status','avatar'

class QuestionSer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user = UserSer()
    title = serializers.CharField()
    text = serializers.CharField()
    likes = serializers.IntegerField()

class AnswerSer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    user = UserSer() 
    text = serializers.CharField() 
    question = QuestionSer()   
