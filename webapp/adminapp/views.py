from django.shortcuts import render, redirect

# Create your views here.
def pageAdminIndex(request):
    
    if request.user.is_authenticated:
        if request.user.is_staff: ## может быть изменить на суперузер, пока хз 
            return render(request, 'adminapp/index.html') 
        else:
            return redirect('workerapp')
    else:
        return redirect('autherror')