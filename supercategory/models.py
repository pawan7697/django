from django.db import models
from django.conf import settings
from category.models import category
from subcategory.models import subcategory

# Create your models here.
class Supercategory(models.Model):
	category_name = models.ForeignKey(category, on_delete=models.CASCADE)
	subcategory_name = models.ForeignKey(subcategory, on_delete=models.CASCADE)
	supercategory_name = models.CharField(max_length=50, blank=True)
	status = models.IntegerField()
    

    # def __str__(self):
    #     return self.subcategory_name

    # class Meta:
    #     ordering = ['subcategory_name']
