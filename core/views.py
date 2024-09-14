from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

from django.core.mail import EmailMessage, EmailMultiAlternatives, send_mail

# Create your views here.

def home(request):
    return render(request, "home.html", {
        'title': 'Home'
    })

def contact(request):
    return render(request, "contact.html", {
        'title': 'Contacto'
    })


def detail(request):
    if request.method == 'POST':

        fullname = request.POST['fullname']  
        mail = request.POST['email']
        message = request.POST['subject']

         # Creamos el correo
        email = EmailMessage(
            "La Caffettiera: Nuevo mensaje de contacto",
            "De {} <{}>\n\nEscribió:\n\n{}".format(fullname, mail, message),
            settings.EMAIL_HOST_USER,
            ["sadonfa@gmail.com"],
            reply_to=[mail]
        )

        # Lo enviamos y redireccionamos
        try:
            email.send()
            # Todo ha ido bien, redireccionamos a OK
            return redirect(reverse('home')+"?ok")
        except:
            # Algo no ha ido bien, redireccionamos a FAIL
            return redirect(reverse('home')+"?fail")

    return render(request, 'detail.html',{
        'title': 'Detalles'
    } )