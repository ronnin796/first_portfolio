from django.http import HttpResponse
from django.shortcuts import render

from .models import Education

# Create your views here.
def home(request):
    return render(request,'base/home.html')

def education(request):
    education_list = Education.objects.all()
    return render(request,'base/education.html',{'education_list': education_list})