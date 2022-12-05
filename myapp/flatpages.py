from django.shortcuts import render

def flatpages(request):
    return render(request, 'flatpages.html')