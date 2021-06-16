from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class products(models.Model):
	category_name = ArrayField(models.CharField(max_length=100), blank=True)
	subcategory_name = ArrayField(models.CharField(max_length=100), blank=True)
	supercategory_name = ArrayField(models.CharField(max_length=100), blank=True)
	product_name = models.CharField(max_length=100, blank=True)
	product_desc = models.CharField(max_length=500, blank=True)
	product_img_nameS = models.CharField(max_length=100, blank=True)
	product_img_nameB = models.CharField(max_length=100, blank=True)
	product_Smallimg = models.ImageField(upload_to='myupload/')
	product_Bigimg = models.ImageField(upload_to='fullimages/')
	product_code = models.CharField(max_length=100, blank=True)
	product_price = models.CharField(max_length=50, blank=True)
	product_sell_price = models.CharField(max_length=50, blank=True)
	status = models.IntegerField()

    
    
    
    
    
    
    
	


