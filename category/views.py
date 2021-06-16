from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import category




# Create your views here.

def categorys(request):
   context = {}

   return render(request,'admin/category.html', context)

  # return HttpResponse('g')

def submitcategory(request):

   if request.method == 'POST':

      category_name = request.POST.get('category')
      #print(category_name)

      user = category.objects.create(category_name=category_name,status=1)
      # user.save()
      return redirect('/categoryView/')

      #return HttpResponse(category_name)

   else:

      return HttpResponse('fail')

def categoryView(request):

   all_entries=category.objects.all()

   return render(request,'admin/category_view.html', { 'all_data':all_entries })
   
  # return HttpResponse(all_entries)

def categoryEdit(request,ids):
   # print(ids)

   catids = category.objects.filter(id=ids).values()
  # print(catids)

 #  return HttpResponse('h')

   return render(request,'admin/categoryEdit.html',{'ids': catids})

def categoryUpdate(request):

   if request.method =="POST":

      category_name = request.POST.get('category')
      idss = request.POST.get('cat_ids')
      user = category.objects.filter(id=idss).update(category_name=category_name)
    #  user = category.objects.create(category_name=category_name,id=idss)
      return redirect('/categoryView/')

     # return HttpResponse(category_name)


      


    
