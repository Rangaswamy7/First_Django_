from django.shortcuts import render,redirect
from .models import rangu,rangu2
from django.http import HttpResponse
# Create your views here.
#def fun(request):

    if request.method == 'POST':

        a= request.POST.get("name")

        b= request.POST.get("address")

        c= request.POST.get("empID")
        d= rangu(name=a,address=b,empID=c)

        d.save()

        print(a)

        print(b)

        print(c)

       

    else:

        return render(request,"page4.html",context={})

    return HttpResponse("printed on Console, please Check!!")