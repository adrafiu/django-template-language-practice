from django.shortcuts import render


# Create your views here.
def home(request):

    context = {"name": "Name: Md. Abdur Rafeu", "address": "Address: Bogura"}

    return render(request, "myapp/home.html", context)


def about(request):
    return render(request, "myapp/about.html")
