from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'miapp/index.html')

def pagina1(request):
    return render(request, 'miapp/pagina1.html')

def pagina2(request):
    return render(request, 'miapp/pagina2.html')

def pagina3(request):
    return render(request, 'miapp/pagina3.html')