from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.
class ProjectsList(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
 title = models.CharField(max_length=300,null=True,blank=False)
 short_desc=models.CharField(max_length=100,null=True,blank=False)
 description = models.TextField(null=True,blank=False)
 technology = models.CharField(max_length=20,null=True,blank=False)
 def __str__(self):
  return self.title


class MoreInfo(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=False)
 firstname=models.CharField(max_length=300, null=True,verbose_name="first name",blank=False)
 lastname=models.CharField(max_length=300, null=True,verbose_name="last name",blank=False)
 collegename=models.CharField(max_length=200,null=True,verbose_name="college name",blank=False)
 major=models.CharField(max_length=200,null=True,blank=False)
 collegecgpa=models.FloatField(null=True,verbose_name="college cgpa",blank=False)
 college_start_year=models.IntegerField(null=True,blank=False)
 college_end_year=models.IntegerField(null=True,blank=False)
 Highschoolname=models.CharField(max_length=200,null=True,verbose_name="high school name",blank=False)
 Highschoolcgpa=models.FloatField(null=True,verbose_name="high school cgpa",blank=False)
 high_school_start_year=models.IntegerField(null=True,blank=False)
 high_school_end_year=models.IntegerField(null=True,blank=False)
 def __str__(self):
  return self.firstname
 def clean(self):
  if self.college_start_year and self.college_end_year:
   if self.college_start_year>self.college_end_year:
    raise ValidationError({"college_start_year":("start year must be before end year."),
	                       "college_end_year": ("start year must be before end year.")})
  if self.high_school_start_year and self.high_school_end_year:
   if self.high_school_start_year>self.high_school_end_year:
    raise ValidationError({"high_school_start_year":("start year must be before end year."),
	                       "high_school_end_year": ("start year must be before end year.")}) 
  
  
class WorkExperience(models.Model):
 user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=False)
 company=models.CharField(max_length=300,null=True,blank=False)
 role=models.CharField(max_length=300, null=True,blank=False)
 years=models.IntegerField(null=True,blank=False)
 start_year=models.IntegerField(null=True,blank=False)
 end_year=models.IntegerField(null=True,blank=False)
 def __str__(self):
  return self.company
 def clean(self):
  if self.start_year and self.end_year:
   if self.start_year>self.end_year:
    raise ValidationError({"start_year":("start year must be before end year."),
	                       "end_year": ("start year must be before end year.")})
  if self.end_year-self.start_year!=self.years:
   raise ValidationError({"years": ("The no.of.years doesn't match start year and end year")})
 
	
 
 

   

	


   

    
	 




                                  
								  