from django.db import models

class WidgetModel(models.Model):
    name = models.CharField(max_length=400)
    age = models.IntegerField()


    def __str__(self):
        return self.name