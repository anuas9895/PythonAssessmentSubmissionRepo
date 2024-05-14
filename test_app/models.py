from django.db import models

# Create your models here.

class Repository(models.Model):
    full_name = models.CharField(max_length=500)
    description = models.TextField()
    created_at = models.DateTimeField()
    stargazers_count = models.IntegerField()
    forks = models.IntegerField()

    def __str__(self):
        return self.full_name