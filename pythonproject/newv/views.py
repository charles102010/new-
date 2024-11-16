from django.shortcuts import render
from newv.models import student
# Create your views here.

def Home(request):
    return render(request,"home.html")


    
def Register(reqeust):
    if reqeust.method=='POST':
        name=reqeust.POST.get('name')
        email=reqeust.POST.get('email')
        phone=reqeust.POST.get('phone')
        age=reqeust.POST.get('age')
        address=reqeust.POST.get('address')
        abc=student(NAME=name,Email=email,Phone=phone,AGE=age,Address=address)
        abc.save()
    return render(reqeust,"register.html")
 