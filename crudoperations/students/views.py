from django.shortcuts import render ,redirect
from django.db.models import Q

from .forms import RegistrationForm
from .models import Student

# Create your views here.


def index(request):

    mydata={}
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        mydata=Student.objects.filter(is_deleted=False)
        validform=form.is_valid()
        if validform:
            # nm=form.cleaned_data['name']
            # em=form.cleaned_data['email']
            # pw=form.cleaned_data['password']
            # reg=Student(name=nm,email=em,password=pw)
            form.save()
            form=RegistrationForm()
    else:
        form=RegistrationForm()
        mydata=Student.objects.filter(is_deleted=False)
    data={'form':form,'mydata':mydata}
    return render(request,"index.html",data)

def delete_data(request,id):

    stu=Student.objects.get(id=id)
    stu.is_deleted=True
    stu.save()
    return redirect('home')

def edit_data(request,id):
    
    data={}
    if request.method=='POST':
        stu=Student.objects.get(id=id)
        form=RegistrationForm(request.POST,instance=stu)
        if form.is_valid():
            form.save()
    else:
        stu=Student.objects.get(id=id)
        form=RegistrationForm(instance=stu)
    data={'form':form,'stu':stu}
    return render(request,'update.html',data)

def search_data(request):
    data={}
    if request.method=='POST':
        query=request.POST.get('searchquery') # "searchquery" come from name of the serch input
        mydata=Student.objects.filter(Q(name__icontains=query)|Q(email__icontains=query),is_deleted=False)
        form=RegistrationForm()   
    else:
        mydata=Student.objects.all()
        form=RegistrationForm()
    data={'form':form,'mydata':mydata,'value':query}
    return render(request,'index.html',data)
