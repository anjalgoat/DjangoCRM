#------------------import for function------------------
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

#------------------import for API endpoint views------------------------
from rest_framework import generics
from .serializers import RecordSerializer




#--------------- Create your views here.---------------
def home(request):
    #See all records
    records = Record.objects.all()


    #check to see if loggin_in
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,"Congrats You logged in")
            return redirect('home')
        else:
            messages.success(request, "Invalid Credentials.You should check in on some of those fields below.")
            return redirect('home')
    else:
        return render(request, 'crmapp/home.html',{'records':records})


def logout_user(request):
    logout(request)
    return render(request,'crmapp/home.html',{})

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user= authenticate(username=username,password=password )
            login(request,user)
            messages.success(request,"Congrats for registration")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'crmapp/register_user.html',{'form': form} )
    return render(request, 'crmapp/register_user.html',{'form': form} )


def customer_record(request, pk):
    if request.user.is_authenticated:
        #View records
        customer_record = Record.objects.get(id=pk)
        return render(request, 'crmapp/record.html',{'customer_record': customer_record} )
    else:
        messages.success(request, 'Login first')
        return redirect('home')

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Record Deleted successfully")
        return redirect('home')
    else:
        messages.success(request, 'Login first')
        return redirect('home')
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, 'Record Added Successfuly')
                return redirect('home')
        return render(request, 'crmapp/add_record.html',{'form':form})
    
    else:
        messages.success(request, 'Login first')
        return redirect('home')

def update_record(request, pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form  = AddRecordForm(request.POST or None, instance= current_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Updated Successfuly')
            return redirect('home')
        return render(request, 'crmapp/update_record.html',{'form':form})
    else:
        messages.success(request, 'Login first')
        return redirect('home')
    

#----------------------------API Endpoint views code---------------------------------

class RecordList(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

class RecordDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer