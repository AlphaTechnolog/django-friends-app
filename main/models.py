from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)

    def __str__(self):
        return self.name