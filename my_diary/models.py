from django.db import models
from django.utils import timezone

class Diary(models.Model):
    title = models.CharField(max_length = 100)
    date_written = models.DateTimeField(default=timezone.now)
    story = models.TextField()
    
    class Meta:
        verbose_name_plural = "Diaries"

    def __str__(self):
        return f'{self.title}, {self.date_written}'