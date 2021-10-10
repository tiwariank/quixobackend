from django.db import models
from datetime import datetime

# Create your models here.


class QuizModel(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    quiz = models.TextField()
    quiz_type = models.CharField(max_length=20)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.quiz        


class QuestionModel(models.Model):
    question_id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    question = models.TextField()
    question_type = models.CharField(max_length=20)
    ans = models.TextField(blank=True,null=True)
    def __str__(self):
        return self.question

class OptionModel(models.Model):
    option_id = models.AutoField(primary_key=True)
    question_id = models.ForeignKey(QuestionModel, on_delete=models.CASCADE)
    quiz_id = models.ForeignKey(QuizModel, on_delete=models.CASCADE)
    option = models.TextField()
    option_type = models.CharField(max_length=20)
    
    def __str__(self):
        return self.option






# class Total_quiz(models.Model):
#     quiz_id = models.AutoField(primary_key=True)
#     quiz_title = models.TextField()
#     inner_css = models.CharField(max_length=200, null=True, blank=True)
#     outer_css = models.CharField(max_length=200, null=True, blank=True)
#     pub_date = models.DateTimeField(default=datetime.now, blank=True)

#     def __str__(self):
#         return self.quiz_title



# class Options(models.Model):
#     quiz_id = models.ForeignKey(Total_quiz, on_delete=models.CASCADE)
#     option_id = models.AutoField(primary_key=True)
#     option_value1 = models.CharField(max_length=200, null=True, blank=True)
#     option_value2 = models.CharField(max_length=200, null=True, blank=True)
#     option_value3 = models.CharField(max_length=200, null=True, blank=True)
#     option_value4 = models.CharField(max_length=200, null=True, blank=True)
#     option_value5 = models.CharField(max_length=200, null=True, blank=True)
#     correct_option = models.CharField(max_length=200, null=True, blank=True)
#     optionThemeStyleCss = models.CharField(max_length=200, null=True, blank=True)
#     # pub_date = models.DateTimeField(default=datetime.now, blank=True)


#     # def __str__(self):
#     #     return (self.option_id )


# class Questions_table(models.Model):
#     quiz_id = models.ForeignKey(Total_quiz, on_delete=models.CASCADE)
#     question_id = models.IntegerField()
#     quest_str = models.TextField()
#     option_type = models.CharField(max_length=200)
#     option_id = models.ForeignKey(Options, on_delete=models.CASCADE)
#     questionThemeStyleCss = models.CharField(max_length=200, null=True, blank=True)
#     pub_date = models.DateTimeField(default=datetime.now, blank=True)

#     # def __str__(self):
#     #     return self.quest_str





