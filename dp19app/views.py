
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
#Whatsnew: in this we have added propic in the form.py and made changes in the respective html file by replacing {{form|crispy}} with{{ form.first_name|as_crispy_field }}
#so that we can style our webpage with the boootstrap classes and also we can access images in this project
def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")


def base(request):
    return render(request,"base.html")



def home(request):
    return render(request,"dp19app/home.html")



def profile(request):
    name="akshay"
    return render(request,"dp19app/profile.html",{'name':name})



def get_demo(request):
    name=request.GET.get('name')
    return render(request,"get_demo.html",{'name':name})



def post_demo(request):
    if request.method=="POST":
        name=request.POST.get('name')
        return HttpResponse("<h1>Thanks for submission Mr./Ms. {}</h1>".format(name))
    return render(request,"post_demo.html")



def register(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        phoneno=request.POST.get("phone_no")
        pwd=request.POST.get("pwd")
        date=request.POST.get("birthday_day")
        month=request.POST.get("birthday_month")
        year=request.POST.get("birthday_year")
        gender=request.POST.get("sex")
        if gender=='1':
            gender="Female"
        else:
            gender="Male"
        send_mail("Thank you for registration", "mr/ms.{} {}\n Thanks for registerinng with us".format(first_name,last_name),"abhidenim10@gmail.com",[email,],fail_silently=True)
        return redirect("home")
    return render(request,"dp19app/register.html")



from django.core.files.storage import FileSystemStorage

def multiplesel(request):
    if request.method=="POST":
        foods=request.POST.getlist("food")
        languages=request.POST.getlist("language")
        return HttpResponse("<h1>{}{}</h1>".format(foods,languages))
    return render(request,"multisel.html")



def imgupld(request):
    return render(request,"img_upld.html")



def imgdis(request):#for one image
    file_url=False
    if request.method=="POST" and request.FILES:
        image=request.FILES['immg']
        fs=FileSystemStorage()
        file=fs.save(image.name,image)
        file_url=fs.url(file)
    return render(request,"imgdisplay.html",context={'file_url':file_url})




from django.core.files.storage import FileSystemStorage
from dp19app.utilities import store_image

def imgdisl(request):#for two images
    file_url=False
    if request.method=="POST" and request.FILES:
        image1=request.FILES['immg1']
        image2=request.FILES['immg2']
        file_urls=map(store_image,[image1,image2])
    return render(request,"imgdisplay.html",context={'file_urls':file_urls})

from dp19app import forms

def builtin(request):
    if request.method=="POST":
        form=forms.SampleForm(request.POST,request.FILES) 
        if form.is_valid():
            first_name=form.cleaned_data.get('first_name')
            last_name=form.cleaned_data.get('last_name')
            email=form.cleaned_data.get('email')
            phno=form.cleaned_data.get('phno')
            pwd=form.cleaned_data.get('pwd')
            birth_day=form.cleaned_data.get('birth_day')
            birth_month=form.cleaned_data.get('birth_month')
            birth_year=form.cleaned_data.get('birth_year')
            gender=form.cleaned_data.get('gender')
            languages=form.cleaned_data.get('languages')
            propic=form.cleaned_data.get('propic')
            store_image(propic)
            data=form.cleaned_data
            context=data
            return render(request,"display_data.html",context=data)
    form=forms.SampleForm()
    return render(request,'builtin.html',{'form':form})
