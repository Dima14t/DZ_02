from django.db import models


# Create your models here.
class Reviews(models.Model):
    RATING_CHOICES = (
        ('1', "Плохо"),
        ('2', "Неочень"),
        ('3', "Удовлетворительно"),
        ('4', "Хорошо"),
        ('5', "Отлично"),

         )
    review = models.TextField()
    reviewer = models.CharField(max_length=250)
    rating = models.TextField(choices= RATING_CHOICES)
    is_published = models.BooleanField(default=False)
    date_writing = models.DateTimeField(auto_now_add=True)

