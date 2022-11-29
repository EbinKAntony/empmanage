from django.shortcuts import render, redirect
from empmanage.forms import UserAdminCreationForm
from empmanage.models import *
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.contrib.auth import  login,logout
from django.contrib.auth.decorators import login_required

#### login page and function ####

def loginpage(req):
    if req.method == 'POST':
        email = req.POST.get('email')
        password = req.POST.get('password')
        try:
            user = CustomUser.objects.get(email = email)
            if user.check_password(password):
                if user is not None:
                    login(req, user)
                    return redirect('empadd')
                else:
                    return redirect('loginpage')
        except:
            return redirect('loginpage')
    return render(req, 'login.html')


#### employee details page ####
@login_required(login_url = 'login')
def addempdet(req):
    return render(req, 'addempdet.html')

#### salary details page ####
@login_required(login_url = 'login')
def addsalarydet(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        code = req.POST.get('empcode')
        age = req.POST.get('age')
        context = {
            "nameemp":name,
            "empcode":code,
            "age":age,
        }
        
    return render(req, 'salary.html',context)


##### Emp list  ######
@login_required(login_url = 'login')
def emplist(req):
    empdet = Employee.objects.all()
    context = {
        "empdet":empdet,
    }
    return render(req, 'employeelist.html',context)


####create Employee ####
@login_required(login_url = 'login')
def empcreate(req):
    if req.method == 'POST':
        name = req.POST.get('name')
        code = req.POST.get('empcode')
        age = req.POST.get('age')
        salary = req.POST.get('salary')
        emp = Employee.objects.create(name = name,code = code,age = age,salary= salary)
        
        return redirect('emplist')
    
#### Update Employee ####    
@login_required(login_url = 'login')
def empupdate(req,id):
    emp = Employee.objects.get(id = id)
    if req.method == 'POST':
        name = req.POST.get('name')
        code = req.POST.get('empcode')
        age = req.POST.get('age')
        salary = req.POST.get('salary')
        
        empdet = Employee.objects.get(id = id)
        empdet.name = name
        empdet.code = code
        empdet.age = age
        empdet.salary = salary
        empdet.save()
        return redirect('emplist')
    
    context = {"emp":emp}    
    return render(req, 'editemployee.html',context)

#### Delete Employee ####  
@login_required(login_url = 'login') 
def deleteemp(req,id):
    emp = Employee.objects.get(id = id)
    emp.delete()
    return redirect('emplist')

#### logout User ####
def logoutuser(req):
    
	logout(req)
	return redirect('login')
    

        
        


