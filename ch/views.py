from django.shortcuts import render

# Create your views here.
def Index(request, *args, **kwargs):
    return render(request, 'index.html')