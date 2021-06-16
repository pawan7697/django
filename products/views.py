from django.shortcuts import render
from django.http import HttpResponse
from category.models import category
from subcategory.models import subcategory
from supercategory.models import Supercategory
from .models import products
#from .models import UploadFileForm
from .forms import ImageForm


# Create your views here.

def addproducts(request):

	categorys = category.objects.all()
	subcategorys = subcategory.objects.all()
	supers = Supercategory.objects.all()
	return render(request,'newadmin/addproducts.html',{'cat':categorys,'subcat': subcategorys,'supers': supers})

	#return HttpResponse('ok')

def productSubmit(request):

	if request.method =="POST":
		#mm = UploadFileForm(request.POST, request.FILES)

		cat_values = request.POST.getlist('cat[]')
		sub_values = request.POST.getlist('subcats[]')
		super_values = request.POST.getlist('supercat[]')
		pname = request.POST.get('pname')
		pprice = request.POST.get('pprice')
		sellprice = request.POST.get('sellprice')
		desc = request.POST.get('desc')
		simg = request.FILES['simg']
		
    

		
		a = products.objects.create(category_name=cat_values,subcategory_name=sub_values,supercategory_name=super_values,product_name=pname,product_desc=desc,product_Smallimg=simg,product_img_nameB='m2',product_code='axe13',product_price=pprice,product_sell_price=sellprice,status=1)

	#	print((service_values))

	#	cat[] = request.POST.get('cat')


		return HttpResponse('success')


