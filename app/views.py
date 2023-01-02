from django.shortcuts import render

# Create your views here.
def operations(request):
    d={'a':11 , 'b':67}
    return render(request,'operations.html',d)