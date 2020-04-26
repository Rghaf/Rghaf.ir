from django.shortcuts import render
from app_resume.models import Resume

# Create your views here.

def resumepage(request):
    ctx = {}
    ctx['Resume'] = Resume.objects.all().order_by("id")
    return render(request , 'resume.html', ctx)