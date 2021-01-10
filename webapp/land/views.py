from django.shortcuts import render

# Create your views here.
def pageIndex(request):
    return render(request, 'land/index.html')