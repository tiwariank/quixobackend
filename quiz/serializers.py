from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import QuizModel,QuestionModel,OptionModel


class Total_quizSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizModel
        fields = ['quiz_id', 'quiz', 'quiz_type']


class Questions_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionModel
        fields = ['question_id','quiz_id','question','question_type']


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionModel
        fields = ['option_id', 'question_id', 'option', 'option_type', 'option_type']        
