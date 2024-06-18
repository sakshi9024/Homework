from django.shortcuts import render,HttpResponse, redirect

from .models import Student

def index(request):
    data = Student.objects.all()
    print(data)
    return render(request,"table.html",{'Data':data})

def getform(request):
    if request.method=="POST":
       
        name = request.POST['uname']
        email = request.POST['uemail']
        age = request.POST['uage']
        address = request.POST['uaddress']
        phone_no = request.POST['uphone_no']
        date = request.POST['udate']
        Student(name=name, email=email, age=age, address=address,  phone_no=phone_no, date=date).save()
        return redirect('/')        
    return render(request,'form.html')

def delete(request,id):
    data = Student.objects.filter(id=id)
    data.delete()
    return redirect('/')

def update(request,id):
    if request.method=="POST":
        data = Student.objects.get(id=id)
        data.name = request.POST['uname']
        data.email = request.POST['uemail']
        data.age = request.POST['uage']
        data.address = request.POST['uaddress']
        data.phone_no = request.POST['uphone_no']
        data.date = request.POST['udate']
        data.save()
        return redirect('/')
    else:
        data = Student.objects.get(id=id)
    return render(request,'update.html',{'data':data})
    