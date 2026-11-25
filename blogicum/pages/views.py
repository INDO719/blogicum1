"""Представления статических страниц сайта."""

from django.shortcuts import render

# Create your views here.


def about(request):
    """Отображает страницу «О проекте»."""

    return render(request, 'pages/about.html')


def rules(request):
    """Отображает страницу с правилами."""

    return render(request, 'pages/rules.html')
