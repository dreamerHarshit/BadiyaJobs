from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^company/', views.CompanyList.as_view()),
    url(r'^job_english', views.Job_englishList.as_view()),
    url(r'^job_hindi/', views.Job_hindiList.as_view()),
    url(r'^Job_hinglish/', views.Job_hinglishList.as_view()),
    url(r'^roles/', views.RoleList.as_view()),
]