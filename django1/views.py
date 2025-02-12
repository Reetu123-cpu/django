from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.shortcuts import render
from .forms import Usersform
from news.models import News
from contactenquiry.models import contactenquiry
from django.core.mail import send_mail
def dd(request):
    # newsData=News.objects.all()
    # data={
    #     'newsData':newsData

        # 'title':'home new',
        # 'bdata':'welcome to django',
        # 'clist':['php','java','python'],
        # 'numbers':[15,28,7,30,50,14,6],
        # 'studentdata':[
        #     {'name':'anu','p_no':7896541236},
        #     {'name':'aman','p_no':6938527418}
        # ]

        # }
    # send_mail(
    #     "Testing mail",
    #     "Here is te message",
    #     "anubhola8@gmail.com",
    #     ["anubhola1988@gmail.com"],
    #     fail_silently=False,
    # )
    return render(request,"index.html")
def contactus(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"contact.html",{'output': output})

# def userForm(request):
#     try:
#       n1 = int(request.GET['num1'])
#       n2 = int(request.GET['num2'])
#       print=(n1+n2)
#     except:
#      pass
#     return render(request,"userform.html")

# def userForm(request):
#     finalans=0
#     try:
#       n1 = int(request.GET.get('num1'))
#       n2 = int(request.GET.get('num2'))
#       finalans=n1+n2
#     except:
#      pass
#     return render(request,"userform.html",{'output': finalans})



def submitform(request):

       try:
        if request.method == "POST":
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1 + n2
            dict1 = {
                'n1': n1,
                'n2': n2,
                'output': finalans
            }
            return HttpResponse(finalans)

            # url = "/contact/?output={}".format(finalans)  # create url using format method
            # return HttpResponseRedirect('/contact')
            # return HttpResponseRedirect(url)
       except:
        pass
    # return render(request,"userform.html",dict1)

    # return HttpResponse(request)


def userForm(request):
    finalans=0
    fn = Usersform()
    dict1 = {'form':fn}

    try:
      if request.method == "POST":
        n1 = int(request.POST.get('num1'))
        n2 = int(request.POST.get('num2'))
        finalans=n1+n2
        dict1={
            'form':fn,
            'n1':n1,
            'n2':n2,
            'output':finalans
        }
        url = "/contact/?output={}".format(finalans)  #create url using format method
        # return HttpResponseRedirect('/contact')
        return HttpResponseRedirect(url)

    except:
      pass
    return render(request,"userform.html",dict1)

def calculator(request):
    c=''
    try:
        if(request.method=="POST"):
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*":
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    except:
        c="invalid option........"
    return render(request,"calculator.html",{'c':c})

def evenodd(request):
    c=''
    if request.method == "POST":

        n= eval(request.POST.get('num1'))
        if n%2==0:
            c="even no"
        else:
            c="odd no"

    return render(request,"evenodd.html",{'c': c})


# def newsdetails(request,newsid,slug):
def newsdetails(request,slug):

    # newsdetails=News.objects.get(id=newsid)
    newsdetails=News.objects.get(news_slug=slug)

    data1={
        'newsdetails':newsdetails
    }

    return render(request,"newsdetails.html",data1)
def saveenquiry(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phoneno=request.POST.get('phoneno')
        message=request.POST.get('message')
        en=contactenquiry(name=name,email=email,phoneno=phoneno,message=message)
        en.save()
    return render(request,'contact.html')

def recipes(request):
    if request.method=="POST":
        Recepy_name=request.POST.get('Recepy_name')
        Description=request.POST.get('Description')
        # Image=request.POST.get('Image')
        Image=request.FILES.get('Image')
        print(Recepy_name,Description)
        print(Image)
    return render(request,'recipes.html')