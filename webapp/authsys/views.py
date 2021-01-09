from django.shortcuts import render

# Create your views here.
def pageLogin(request):
    return render(request, 'authsys/login.html')

def pageRegister(request):
    pass

def pageAuthError(request):
    pass

