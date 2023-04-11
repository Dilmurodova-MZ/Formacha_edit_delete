from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

def home(request):
    if 'q' in request.GET:
        qidirish = request.GET['q']
        table    = Table.objects.filter(name__icontains = qidirish )
    else:
        table = Table.objects.all()
    # table = Table.objects.all()
    context = {
        'table':table,
    }
    return render(request,'index.html', context)

def ochish(request ,post_id):
    post = get_object_or_404(Table, pk=post_id)
    context ={
        'post':post,
    }
    return render(request, 'table.html', context)

def Add(request):
    forma = TableForm(request.POST)
    if request.method == "POST":
        if forma.is_valid(): #tekshirish
            forma.save()
            return redirect('home') # redirect qaytarib yuborish
    else:
        forma = TableForm()
    context = {
        'forma':forma
    }
    return render(request,'add.html', context)
              
    
    