from quiz.serializers import Total_quizSerializer, Questions_tableSerializer, OptionsSerializer
from django.urls import path
from .views import(TotalQuizApiView, QuestionsApiView, OptionsApiView)


urlpatterns = [
    path('quiz', TotalQuizApiView.as_view(), name='total_quiz'),
    path('quiz/<str:quiz_id>', TotalQuizApiView.as_view(), name='total_quiz'),
    path('questions', QuestionsApiView.as_view(), name='total_questions'),
    path('question/<str:quiz_id>', QuestionsApiView.as_view(), name='total_questions'),
    path('options', OptionsApiView.as_view(), name='total_options'),
    path('options/<str:quiz_id>', OptionsApiView.as_view(), name='total_options'),
]
