from django.db import models

# Create your models here.
class category(models.Model):
    category_name = models.CharField(max_length=50)
    status = models.IntegerField()

    def __str__(self):
        return self.category_name
