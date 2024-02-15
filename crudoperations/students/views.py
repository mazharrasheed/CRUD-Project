from django.shortcuts import render

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
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']
            pw=form.cleaned_data['password']
            reg=Student(name=nm,email=em,password=pw)
            reg.save()
            form=RegistrationForm()
    else:
        form=RegistrationForm()
        mydata=Student.objects.filter(is_deleted=False)

    data={'form':form,'mydata':mydata}
    return render(request,"index.html",data)
