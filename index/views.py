from django.contrib import auth
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from django.core.mail import message, send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.files import File

# Create your views here.

def home(request):
    context={
        'notappr':11,
        'inprog':43,
        'solved':312,
    }
    context['total']=context['inprog']+context['notappr']+context['solved']
    return render(request,'index.html',context)


def contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        mssg=request.POST['mssg']
        obj=contactusmodel(name=name,email=email,subject=subject,mssg=mssg)
        obj.save()
        send_mail(
            name+' wants to contact us..!',
            "name: "+name+', email: '+email+", subject: "+subject+", message: "+mssg,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_HOST_USER]
        )
        return redirect("/")
    context={
        'notappr':11,
        'inprog':43,
        'solved':312,
    }
    context['total']=context['inprog']+context['notappr']+context['solved']
    return render(request,'index.html',context)
        


from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import os
def fetch_resources(uri, rel):
    path = os.path.join(uri.replace(settings.STATIC_URL, ""))
    return path

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)#, link_callback=fetch_resources)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def filecomplaintform(request):
    if request.method == 'POST':
        context = {
            'firstName':request.POST.get('firstName'),
            'lastName':request.POST.get('lastName'),
            'contactNo':request.POST.get('contactNo'),
            'email':request.POST.get('email'),
            'location':request.POST.get('location'),
            'subject':request.POST.get('subject'),
            'idno':request.POST.get('idno'),
            'image':request.FILES.get('image'),
            'vedio':request.FILES.get('vedio'),
            'message':request.POST.get('message'),
            'id':request.FILES.get('id')
        }
        comp = complaint(
            user_name=request.user,
            victims_fname=context['firstName'],
            victims_lname=context['lastName'],
            contact_no = context['contactNo'],
            email =context['email'],
            location = context['location'],
            subject = context['subject'],
            idproof_number = context['idno'],
            message = context['message'],
            idprooof = context['id'],
            image = context['image'],
            vedio = context['vedio']
        )
        
        e=EmailMessage('complaint filed successfully!',
            'Your form was submitted successfully, our organization will reach to ASAP. Kindly be patience. Thank you for using our website. -- team FEMZO ',
            settings.EMAIL_HOST_USER,
            [context['email']]
        )
        e.content_subtype='html'
        temp=get_template('responses.html')
        html=temp.render(context)
        res=BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), res)
        pdf = res.getvalue()
        filename = 'Responses_' + context['firstName'] + '.pdf'
        e.attach(filename,pdf,'application/pdf')
        e.attach(context['id'].name,context['id'].read(),context['id'].content_type)
        e.attach(context['vedio'].name,context['vedio'].read(),context['vedio'].content_type)
        e.attach(context['image'].name,context['image'].read(),context['image'].content_type)
        e.send()
        comp.save()
        return redirect("filecomplaintform")
    return render(request,'filecomplaint.html')

def signinupform(request):
    if request.method == 'POST':
        if 'register' in request.POST:
            
            context = {
                'username':request.POST.get('username'),
                'password':request.POST.get('password'),
                'email':request.POST.get('email'),
                'name':request.POST.get('name')
            }
            obj = User.objects.create_user(
                first_name=context['name'],
                username = context['username'],
                password = context['password'],
                email = context['email'],
            )
            obj.save()
            send_mail(
                'complaint filed successfully!',
                'Your form was submitted successfully, our organization will reach to ASAP. Kindly be patience. Thank you for using our website. -- team FEMZO ',
                settings.EMAIL_HOST_USER,
                [context['email']],
                fail_silently=True
            )
        elif 'login' in request.POST:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("home")
            else:
                messages.info(request,'Invalid credentials')
                return redirect("signinupform")
    return render(request,'SignInUp.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

def responses(request):
    return render(request,"responses.html")


def search_psdetails(request):
    if(request.method=="POST"):
        name=request.POST.get("name")
        address=request.POST.get("address")
        if(name=='' and address==''):
            #messages.error(request,"Empty Input Fields!!")
            return redirect("search")
        elif(name==''):
            obj=policeDetails.objects.filter(address=address)
        elif(address==''):
            obj=policeDetails.objects.filter(sname=name)
        else:
            obj=policeDetails.objects.filter(sname=name,address=address)
        context={'count':obj}
        # if not obj:
        #     messages.error(request,"Search Not Found!")
        return render(request,"policedetails.html",context)
    return render(request,"policedetails.html")
def view_psdetails(request):
    lst=(policeDetails.objects.all())
    context={'count':lst}
    return render(request,"policedetails.html",context)
def reset_psdetails(request):
    return redirect("/")
def policedetails(request):
    flag=False
    if request.user=='admin':
        flag=True
    return render(request,"policedetails.html",{'flag':flag})
def tactics(request):
    return render(request,"tactics.html")