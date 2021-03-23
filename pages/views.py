from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from django.contrib import messages
from .models import Page
from .forms import  PageForm
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def index(request):
    try:
        pages = Page.objects.all()
    except Page.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'pages/index.html', {'pages':pages})


@login_required
def details(request):
    return HttpResponse('ewfe')

@login_required
def create(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False) 
            x.save()
            messages.success(request, 'Sikeresen létrehozva!')
            return redirect('page_index')
    else:
        form = PageForm()
    return render(request, 'pages/create.html', {'form': form})

@login_required
def update(request, pk):
    page = Page.objects.get(pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('page_index')
    else:
        form = PageForm(instance=page)
    return render(request, 'pages/update.html', {'form': form})

@login_required
def delete(request, pk):
    query = Page.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('page_index')