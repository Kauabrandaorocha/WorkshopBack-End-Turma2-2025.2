from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home2.html')

def tela(request):
    return render(request, 'home.html')