from django.shortcuts import render
from .models import Portfolio
# Create your views here.

def portfolio(request):

    portfolio = Portfolio.objects.all()

    return render(request, 'portfolio.html', {
        'title': 'Portafolio',
        'portfolios': portfolio
    })