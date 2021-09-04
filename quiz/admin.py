from django.contrib import admin

# Register your models here.
from .models import Total_quiz, Options, Questions_table

admin.site.register((Total_quiz, Questions_table, Options))
