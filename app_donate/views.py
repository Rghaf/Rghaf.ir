from django.shortcuts import render
from app_donate.models import Donatepage

# Create your views here.

def donate(request):
    ctx = {}
    ctx['Donate'] = Donatepage.objects.first()
    return render(request, 'donate.html', ctx)
