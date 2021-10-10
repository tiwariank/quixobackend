from django.contrib import admin

# Register your models here.
from .models import QuizModel, QuestionModel, OptionModel

admin.site.register((QuizModel, QuestionModel, OptionModel))
