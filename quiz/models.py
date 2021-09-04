from django.db import models
from datetime import datetime

# Create your models here.


class Total_quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    quiz_title = models.TextField()
    inner_css = models.CharField(max_length=200, null=True, blank=True)
    outer_css = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.quiz_title



class Options(models.Model):
    option_id = models.AutoField(primary_key=True)
    option_value1 = models.CharField(max_length=200, null=True, blank=True)
    option_value2 = models.CharField(max_length=200, null=True, blank=True)
    option_value3 = models.CharField(max_length=200, null=True, blank=True)
    option_value4 = models.CharField(max_length=200, null=True, blank=True)
    option_value5 = models.CharField(max_length=200, null=True, blank=True)
    # correct_option = models.CharField(max_length=200, null=True, blank=True)
    optionThemeStyleCss = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return "options"


class Questions_table(models.Model):
    quiz_id = models.ForeignKey(Total_quiz, on_delete=models.CASCADE)
    question_id = models.IntegerField()
    quest_str = models.TextField()
    option_type = models.CharField(max_length=200)
    option_id = models.ForeignKey(Options, on_delete=models.CASCADE)
    questionThemeStyleCss = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return "questions"





