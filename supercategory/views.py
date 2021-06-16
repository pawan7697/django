from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import category,subcategory,Supercategory

# Create your views here.

def addSupercateory(request):
	categorys = category.objects.all()
	subcategorys = subcategory.objects.all()

	return render(request,'admin/addSupercateory.html',{'catData': categorys,'subcatData': subcategorys })

def ajaxsubcategory(request):

	if request.method =="POST":

		catids = request.POST.get('categoryID')
		subcatID = subcategory.objects.filter(category_name_id=catids).values()

		return render(request,'ajax/subcategory.html', { 'Cdata': subcatID })


		#catID = request.POST.get(categoryID)
		return HttpResponse(catids)
def SupercategorySubmit(request):

	if request.method =="POST":

		category_ids = int(request.POST.get('category_id'))
		subcatID_ids = int(request.POST.get('subcategory_id'))
		sup = request.POST.get('Super')

		users= Supercategory.objects.create(category_name_id=category_ids,subcategory_name_id=subcatID_ids,supercategory_name=sup,status=1)

		#return HttpResponse('success')
		return redirect('/SupercategoryView/')

def SupercategoryView(request):

	data = Supercategory.objects.all().values('supercategory_name','subcategory_name__subcategory_name','id','category_name__category_name')
	return render(request,'admin/supercatView.html',{ 'supercat': data })

#	return HttpResponse(data)



	
