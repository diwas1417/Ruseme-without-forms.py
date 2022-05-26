from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import resume
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        yyy=request.user

    
        if request.method == "POST":
            
            name = request.POST.get('name')
            dob = request.POST.get('dob')
            gender = request.POST.get('gender')
            pin = request.POST.get('pin')
            mobile = request.POST.get('mobile')
            email = request.POST.get('email')
            job_city = request.POST.get('job_city')
            school = request.POST.get('school')
            university = request.POST.get('university')
            degree = request.POST.get('degree')
            skill = request.POST.get('skill')
            about_you = request.POST.get('about_you')
            experience = request.POST.get('experience')
            hobbies = request.POST.get('hobbies')

            xxx = resume(name=name, dob=dob, gender=gender, pin=pin,
                        mobile=mobile, email=email, job_city=job_city, school=school, university=university, degree=degree, skill=skill, about_you=about_you, experience=experience, hobbies=hobbies)
            xxx.created_by=yyy
            xxx.save()
            
        return render(request, 'myfirst/home.html')
    else:
        return HttpResponseRedirect('/login/')    

def register(request):
    if request.method=="POST":
        fm=UserCreationForm(request.POST)
        if fm.is_valid:
            fm.save()

            return HttpResponseRedirect('/login/')

    else:
        fm=UserCreationForm()
    return render(request,'myfirst/register.html',{'fm':fm})        

def user_login(request):
    fm=AuthenticationForm(request=request,data=request.POST)    
    if fm.is_valid():
        xxx=fm.cleaned_data['username']
        yyy=fm.cleaned_data['password']
        user = authenticate(username=xxx, password=yyy)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
    else:
        fm=AuthenticationForm()

    return render(request,'myfirst/login.html',{'fm':fm})        

def info(request):
    cvs=resume.objects.filter(created_by=request.user.id).filter(is_void=False)
    return render(request,'myfirst/mycvs.html',{'cvs':cvs})  

def delete(request,id):
    if request.method=="POST":
        xxx=resume.objects.get(pk=id)
        xxx.is_void=True
        xxx.save()
        return HttpResponseRedirect('/')


def profile(request,id):
    candidate = resume.objects.get(pk=id)
    return render(request, 'myfirst/final.html', {'can': candidate})        
    


def pdf_report_create(request, id):
    candidate = resume.objects.get(pk=id)
    template_path = 'myfirst/pdf.html'
    context = {'can': candidate}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="candidate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')