from django.contrib import admin

# Register your models here.
from question.models import Question, Quiz, Option

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['content', 'option']


@admin.register(Quiz)
class QuiznAdmin(admin.ModelAdmin):
    list_display = ['name', 'num_of_questions', 'duration']


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ['content', 'correct']