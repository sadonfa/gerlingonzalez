from django.shortcuts import render
from .models import Skills, Client, Review

# Create your views here.

def about(request):

    skills = Skills.objects.all()
    clients = Client.objects.all()
    review_obj = Review.objects.all()

    return render(request, "about.html", {
        'title': 'Sobre Mi',
        'skills': skills,
        'clients': clients,
        'reviews': review_obj
    })

def form(request):    

    if request.method == 'POST':
        
        name = request.POST['name']
        subject = request.POST['subject']
        email = request.POST['email']
        messege = request.POST['messege']

        review = Review(
            name = name,
            subject = subject,
            email = email,
            messege = messege
        )

        review.save()

    return render(request, "formulario.html", {
        'title': 'Formulario',
        
    })