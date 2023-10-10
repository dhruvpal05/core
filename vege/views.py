from django.shortcuts import redirect, render
from .models import *

# Create your views here.

def receipe(request):
    if request.method == "POST":
        data = request.POST

        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')

        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_desc = receipe_desc
        )

    queryset = Receipe.objects.all()
    context = {'receipes':queryset}

    return render(request , "receipes.html",context)

def delete_receipe(request,id):
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipe/')

def update_receipe(request,id):
    queryset = Receipe.objects.get(id=id)

    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_desc = data.get('receipe_desc')
        queryset.receipe_name=receipe_name
        queryset.receipe_desc=receipe_desc

        queryset.save()
        return redirect('/receipe/')

    context = {'receipes':queryset}
    return render(request , "update_receipes.html",context)
 