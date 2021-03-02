from django.shortcuts import render

# Create your views here.

def redirect_success_page(request):
    return render(request, 'success_page.html')