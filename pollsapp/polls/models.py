from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=150)
    pub_date = models.DateField()

    def __str__(self) -> str:
        return self.question_text

class Choise(models.Model):
    question= models.ForeignKey(Question, on_delete=models.CASCADE)
    choise_text= models.CharField(max_length=100)
    votes =models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.choise_text