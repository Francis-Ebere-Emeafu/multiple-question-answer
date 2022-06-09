from optparse import Option
from django.db import models

# Create your models here.

class Option(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)

    def __str__(self):
        return f"Answer: {self.content} = {self.correct}"
    

class Question(models.Model):
    content = models.CharField(max_length=200)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content
    
    def get_answers(self):
        return self.option_set.all()


class Quiz(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    num_of_questions = models.IntegerField(default=1)
    duration = models.IntegerField(help_text="Duration of quiz in seconds", default=60)

    def __str__(self):
        return self.name













