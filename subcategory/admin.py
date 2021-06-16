from django.contrib import admin
from .models import subcategory
class SubCategoryAdmin(admin.ModelAdmin):
	list_display=('category_name','subcategory_name','status')

# Register your models here.
admin.site.register(subcategory,SubCategoryAdmin)

