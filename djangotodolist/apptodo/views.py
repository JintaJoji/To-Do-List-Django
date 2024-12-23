from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import Todo
from.models import Task

# Create your views here.
def index(request):
    return HttpResponse("hello")

def listtodo(request):
    if request.method=='POST':
        form=Todo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=Todo()
    return render(request,'todoform.html',{'form':form})

def list(request):
    x=Task.objects.all()
    return render(request,'list.html',{'x':x})

def delete(request,id):
    li=Task.objects.get(pk=id)
    li.delete()
    return redirect('list')
def update(request,id):
    if request.method=='POST':
        li=Task.objects.get(pk=id)
        fm=Todo(request.POST,instance=li)
        if fm.is_valid():
            fm.save()
            return redirect('list')
    else:
        li=Task.objects.get(pk=id)
        fm=Todo(instance=li)
    return  render(request,'updatedtask.html',{'form':fm})