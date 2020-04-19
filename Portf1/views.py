from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from .forms import RegisterForm,ProjectsListForm,MoreInfoForm,WorkExperienceForm
from django.contrib.auth.models import User
from .models import ProjectsList,MoreInfo,WorkExperience
# Create your views here.
class HomePageView(TemplateView):
 template_name='home.html'
class successPageView(TemplateView):
 template_name="success.html"
class logSuccessPageView(TemplateView):
 template_name="logSuccess.html"
class errorPageView(TemplateView):
 template_name='errorPage.html'
def register(response):
 if response.method=="POST":
  form=RegisterForm(response.POST)
  if form.is_valid():
   usr=form.save(commit=False)
   usr.save()
   return redirect("/success")
 else:
  form=RegisterForm()
 return render(response, "register.html", {"form":form})
 
def create(request):
 if request.method=="POST":
  form=ProjectsListForm(request.POST)
  if form.is_valid():
   project=form.save(commit=False)
   project.user=request.user
   project.save()
   return redirect('create')
 else:
  form=ProjectsListForm()
 return render(request, "create.html", {'form': form})
 
def addMoreInfo(request):
 if request.method=="POST":
  form=MoreInfoForm(request.POST)
  msg='Enter the details'
  if form.is_valid():
   m=MoreInfo.objects.filter(user=request.user)
   print(type(m))
   if m.exists():
      return redirect("/errorPage") 

   else:
    moreinfo=form.save(commit=False)
    moreinfo.user=request.user
    moreinfo.save()
    return redirect('addmoreinfo')
 else:
  form=MoreInfoForm()
 return render(request, "addmoreinfo.html", {'form': form})

def viewInfo(response):
 moreinfos=MoreInfo.objects.all()
 #print(projects)
 #print(response.user)
 #print(ProjectsList.objects.filter(user=response.user))
 MoreInfo1=MoreInfo.objects.filter(user=response.user)
 args={'moreinfo': MoreInfo1}
 return render(response, "viewInfo.html",args)

def addWorkExper(request):
 if request.method=="POST":
  form=WorkExperienceForm(request.POST)
  if form.is_valid():
   we=form.save(commit=False)
   we.user=request.user
   we.save()
   return redirect('addworkexper')
 else:
  form=WorkExperienceForm()
 return render(request, "addworkexper.html", {'form': form})

def viewWorkExper(response):
 workexper=WorkExperience.objects.all()
 #print(projects)
 #print(response.user)
 #print(ProjectsList.objects.filter(user=response.user))
 workexper1=WorkExperience.objects.filter(user=response.user)
 args={'workexper': workexper1}
 return render(response, "viewWorkInfo.html",args)
  
def view(response):
 projects=ProjectsList.objects.all()
 print(type(projects))
 #print(response.user)
 #print(ProjectsList.objects.filter(user=response.user))
 projects1=ProjectsList.objects.filter(user=response.user)
 args={'projects': projects1}
 return render(response, "view.html",args)
 
def project_detail(response, pk):
 projects=ProjectsList.objects.get(pk=pk)
 args={'projects': projects}
 print(type(projects))
 return render(response, "project_detail.html",args)
 
def FullView(response):
  MoreInfo1=MoreInfo.objects.filter(user=response.user)
  workexper1=WorkExperience.objects.filter(user=response.user)
  projects1=ProjectsList.objects.filter(user=response.user)
  args={'moreinfo':MoreInfo1, 'workexper':workexper1, 'projects':projects1}
  return render(response, "fullview.html", args)
	
