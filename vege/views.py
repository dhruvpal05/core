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
 