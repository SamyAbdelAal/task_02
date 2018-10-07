from django.shortcuts import render

# Create your views here.
context= {"msg":"Hello World!"}
def homepage(request):
    return render(request, 'home.html',context)