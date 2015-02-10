from django.db import models

# Create your models here.
class Suggestion(models.Model):
    suggestion = models.CharField(max_length = 200)
    type = models.CharField(max_length = 200)

def addtodatabase(suggestions, type):
    for suggestion in suggestions:
        s = Suggestion()
        s.suggestion = suggestion
        s.type = type
        s.save()

