from django.urls import path

from .views import *

urlpatterns = [
  path("success/", successPageView.as_view(),name="success"),
  path("logSuccess/",logSuccessPageView.as_view(), name="logSuccess"),
   path("register/", register, name="register"),
	path('', HomePageView.as_view(), name='home'),
	path('create/', create,name="create"),
	path("view/", view, name="view"),
	path("<int:pk>/", project_detail, name="project_detail"),
	path("addmoreinfo/", addMoreInfo, name='addmoreinfo'),
	path("viewmoreinfo/", viewInfo, name='viewmoreinfo'),
	path("addworkexper/", addWorkExper, name='addworkexper'),
	path("viewworkexper/", viewWorkExper, name='viewworkexper'),
	path("fullview/", FullView, name='fullview'),
	path("errorPage/", errorPageView.as_view(), name='errorPage'),
]