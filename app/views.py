from django.shortcuts import render

# Create your views here.
def parent(request):
    return render(request,'parent.htm')
def child(request):
    return render(request,'child.htm')