from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return HttpResponse("<h1> Breaking Bad <h1/>")



def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1> Albuquerque, New Mexico <h1/>")



def about_view(request, *args, **kwargs):
    return HttpResponse("<h1> Walter White & Jesse Pinkman <h1/>")


def careers_view(request, *args, **kwargs):
    return HttpResponse("<h1> Pharmacists <h1/>")
