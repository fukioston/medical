from django.shortcuts import render
from medical.settings import g

def symptom_info(request):
    return render(request, 'medical_info/symptom_info.html')
def get_symptom_info(request):
    return True