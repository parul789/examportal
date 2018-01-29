from . import models
from rest_framework import serializers


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ('id', 'ques_text', 'choice_1', 'choice_2', 'choice_3', 'choice_4')


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Exam
        fields = ('id', 'name','examnee')


class ResponseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Response
        fields = ('id', 'user', 'response_field','exam_fkey','question_fkey',)


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Response
        fields = ('response_field',)
