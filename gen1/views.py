from django.shortcuts import render

# Create your views here.

def myfirstpage(request):
    return render(request, 'FirstPage.html')
