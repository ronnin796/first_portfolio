from django.http import HttpResponse
from django.shortcuts import render

from .models import Education , Skill , Expertise

# Create your views here.
def home(request):
    return render(request,'base/home.html')

def education(request):
    education_list = Education.objects.all()
    return render(request,'base/education.html',{'education_list': education_list})

def skills(request):
    # Assuming you have a Skill model to fetch skills from the database
    skills = Skill.objects.all()  # Uncomment this line if you have a Skill model
    expertise = Expertise.objects.all()  # Uncomment this line if you have an Expertise model
    context = {
        'skills_list': skills,  
        'expertise_list': expertise,  }
    
    return render(request,'base/skills.html' , context)  