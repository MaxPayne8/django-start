from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return HttpResponse("<b>welcome!!<b>")

def homePage(request):
    data={'title' : 'Home New' , 'bdata': 'Hello! How are you?', 'clist':['React' , 'Tailwind', 'Django']}
    return render(request, "index.html")

def contact(request):
    return HttpResponse("8368852177")

def employee(request):
    return HttpResponse("employee")

def employeeDetails(request,empId):
    return HttpResponse(empId)