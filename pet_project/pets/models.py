from django.db import models

class Dog(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    is_vaccinated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.breed})"
