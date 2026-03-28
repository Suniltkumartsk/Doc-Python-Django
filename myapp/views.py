from django.shortcuts import render,redirect
from .models import Userdata,Doctorinfo,Registerinfo
from django.contrib import messages

def index(request):
    return render(request,'index.html')

def login_page(request,method=['GET','POST']):
    if request.method=="POST":
        email_id=request.POST.get('email')
        password=request.POST.get('password')
        user=Userdata.objects.filter(email=email_id,password=password)
        if user.exists():
            request.session['user']=email_id
            return redirect('/home/')
        else:
            messages.error(request,"email and password are inncorrect")
    return render(request,'login.html')

def signup_page(request):
    if request.method=="POST":
        x=request.POST.get('email')
        y=request.POST.get('password')  
        z=request.POST.get('confirm_password')
        userinfo=Userdata.objects.filter(email=x)
        if userinfo.exists():
            messages.error(request,"useralready exists")
        elif y!=z:
            messages.error(request,"password doesnt match")
        else:
            Userdata.objects.create(email=x,password=y)
            return render(request,'login.html')    
    return render(request,'signup.html')

def home(request):
    Doctor =Doctorinfo.objects.all()
    return render(request,'home.html',{'doctors':Doctor})
    
def register(request):
    if request.method=="POST":
        x=request.POST.get('doc_name')
        y=request.POST.get('p_name')  
        z=request.POST.get('p_age')
        h=request.POST.get('p_date')
        a=request.POST.get('gender')
        b=request.POST.get('contact')  
        c=request.POST.get('problem')
        Registerinfo.objects.create(doc_name=x,p_name=y,p_age=z,p_date=h,gender=a,contact=b,problem=c)
        return render(request,'success.html')
    
    return render(request,'register.html')



# Create your views here.