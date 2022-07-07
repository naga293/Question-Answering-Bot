from django.db import models

class Question(models.Model):#creating required models
    question = models.TextField(null=False)
    wiki_terms = models.CharField(max_length=200,null=False)
    answer = models.CharField(max_length=200)
    prediction_score=models.FloatField(default=0)

