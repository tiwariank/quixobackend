from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Total_quiz, Questions_table, Options


class Total_quizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Total_quiz
        fields = ['quiz_id', 'quiz_title', 'inner_css', 'outer_css', 'pub_date']


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['option_id', 'option_value1', 'option_value2', 'option_value3', 'option_value4', 'option_value5', 'optionThemeStyleCss']


class Questions_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions_table
        fields = ['quiz_id', 'question_id', 'quest_str', 'option_type', 'option_id', 'questionThemeStyleCss', 'pub_date']        
