from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.
def foodpage(request):
    data = [
        {
            'id':1,
            'name':'alo',
            'des':'sdfksfood',
            'fee':1000
        },
        {
            'id':2,
            'name':'alo',
            'des':'sdfksfood',
            'fee':1000
        },
        {
            'id':3,
            'name':'alo',
            'des':'sdfksfood',
            'fee':1000
        },
    ]
    return render(request,'system/service.html',{'info':data})  




def aboutpage(request,id):
    return render(request,'system/service.html',{'id':id})

def delivarypage(request):
    return render(request,'system/delivary.html')
