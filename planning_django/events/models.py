from django.db import models # type: ignore

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


# Create your models here.
