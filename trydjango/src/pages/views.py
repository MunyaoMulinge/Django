from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "flush This is my about",
        "my_numb": 711223344,
        "my_list": ["Tithe", "Donations", "Projects", "KGB"]
    }
    return render(request, "about.html", my_context)


def careers_view(request, *args, **kwargs):
    return render(request, "careers.html", {})

