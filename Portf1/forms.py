from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ProjectsList,MoreInfo,WorkExperience

class RegisterForm(UserCreationForm):
 email = forms.EmailField()
 
 
 class Meta:
  model = User
  fields = ["username", "email", "password1", "password2"]


class ProjectsListForm(forms.ModelForm):
 
 class Meta:
  model=ProjectsList
  fields=["title","short_desc", "description", "technology"]
  widgets = {
          'description': forms.Textarea(attrs={'rows':4, 'cols':40}),
        }


class MoreInfoForm(forms.ModelForm):
 
 class Meta:
  model=MoreInfo
  fields=["firstname", "lastname", "collegename","major","college_start_year","college_end_year", "collegecgpa","Highschoolname","high_school_start_year","high_school_end_year","Highschoolcgpa"]
 
 
class WorkExperienceForm(forms.ModelForm):
 
 class Meta:
  model=WorkExperience
  fields=["company","role","years","start_year","end_year"]