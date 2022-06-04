from django.shortcuts import render, HttpResponse


def about(request):
    # return HttpResponse('Hi, My Name Is Mohsen Enayat')
    return render(request, 'about.html')


def home(request):
    # return HttpResponse('This Is Home Page')
    return render(request, 'home.html')
