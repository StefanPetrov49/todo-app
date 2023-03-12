from django.db import models


# Create your models here.

class Task(models.Model):

    title = models.CharField(
        max_length=128,
        null=False,
        blank=False,
    )

    description = models.CharField(
        max_length=512,
        null=False,
        blank=False,
    )

    author = models.CharField(
        max_length=64,
        null=False,
        blank=False,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    start_time = models.DateField()

    completed = models.BooleanField(
        default=False
    )