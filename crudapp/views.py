from django.shortcuts import render,redirect
from crudapp.models import book
from crudapp.forms import bookform
# Create your views here.
def read(request):
	book1=book.objects.all()
	return render(request,'app/sample.html',{'b':book1})
def insert(request):
	form=bookform()
	if request.method=='POST':
		form=bookform(request.POST)
		if form.is_valid():
			form.save()
	return render(request,'app/insert.html',{'form':form})
def delete(request,id):
	bo=book.objects.get(id=id)
	bo.delete()
	return redirect('/result')	
def update(request,id):
	Book=book.objects.get(id=id)
	if request.method=='POST':
		form=bookform(request.POST,instance=Book)
		if form.is_valid():
			form.save()
		return redirect('/result')
	return render(request,'app/update.html',{'b':Book})
