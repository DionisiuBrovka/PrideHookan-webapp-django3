from django.shortcuts import render, redirect

# Create your views here.
def pageWorkerIndex(request):
    if request.user.is_authenticated:
        if request.user.is_staff: ## может быть изменить на суперузер, пока хз 
            return redirect('adminindex')
        else:
            return render(request, 'workerapp/index.html')
    else:
        return redirect('autherror')
     