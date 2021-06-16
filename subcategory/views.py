from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponse
from .models import category,subcategory
#from django.contrib.auth.models import User

# Create your views here.

def addSubcategory(request):

   catdata = category.objects.all()

   return render(request,'admin/addSubcategory.html',{'categorys': catdata})
   

  # return HttpResponse('g')

def submitSubcategory(request):

   if request.method =="POST":

      category_names = int(request.POST.get('category'))

      subcategorys = request.POST.get('subcategory')

      user = subcategory.objects.create(category_name_id=category_names, subcategory_name=subcategorys,status=1)
      return redirect('/subcategoryView/')

     # return HttpResponse('success')

   else:

      return HttpResponse('fail')

def subcategoryView(request):

   data = subcategory.objects.all().values('subcategory_name','id','category_name__category_name')
   #mm = subcategory.objects.select_related()
  # print(mm)
  # print(data)
   return render(request,'admin/subcateoryview.html', { 'all_data':data })
  # return HttpResponse(data)  

def subcategoryEdit(request,ids):

   catids = subcategory.objects.filter(id=ids).values()
   catdata = category.objects.all()
   
   return render(request,'admin/subcategoryEdit.html', { 'all_data':catids ,'idss':ids,'categorys': catdata})
   
def subcategoryUpadte(request):

   if request.method == "POST":

      idssd = int(request.POST.get('idss'))

      categoryID = request.POST.get('categoryID')

      subcategory_name = request.POST.get('subcategoryname')

      user = subcategory.objects.filter(id=idssd).update(category_name_id=categoryID,subcategory_name=subcategory_name)
      
      return redirect('/subcategoryView/')

   else:
   
      return HttpResponse('fail')   




