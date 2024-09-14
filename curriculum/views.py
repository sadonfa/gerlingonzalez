from django.shortcuts import render
from .models import Certificate, Knowledges, SkillsCode, SkillsDesing, Training, Experience

# Create your views here.

def curriculum(request):

    certificates = Certificate.objects.all()
    knowledges = Knowledges.objects.all()
    skills_code = SkillsCode.objects.all()
    skills_desing = SkillsDesing.objects.all()
    training = Training.objects.all()
    experience = Experience.objects.all()

    return render(request, "curriculum.html", {
        'title': 'Curriculum',
        'certificates': certificates,
        'knowledges': knowledges,
        'skills_codes': skills_code,
        'skills_desings': skills_desing,
        'trainings': training,
        'experiences': experience
    })