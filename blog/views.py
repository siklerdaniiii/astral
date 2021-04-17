from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from django.contrib import messages
from .models import Blog, BlogCategory, BlogOwner
from .forms import  BlogForm, BlogCategoryForm, BlogOwnerForm
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def index(request):
    try:
        blogs = Blog.objects.all()
    except Blog.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'blog/index.html', {'blogs':blogs})

@login_required
def details(request):
    return HttpResponse('ewfe')

@login_required
def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False) 
            x.save()
            messages.success(request, 'Sikeresen létrehozva!')
            return redirect('blog_index')
    else:
        form = BlogForm()
    return render(request, 'blog/create.html', {'form': form})

@login_required
def update(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('blog_index')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/update.html', {'form': form})

@login_required
def delete(request, pk):
    query = Blog.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('blog_index')



# CATEGORY
@login_required
def index_category(request):
    try:
        categories = BlogCategory.objects.all()
    except BlogCategory.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'blog/index_category.html', {'categories':categories})

@login_required
def details_category(request):
    return HttpResponse('ewfe')

@login_required
def create_category(request):
    if request.method == 'POST':
        form = BlogCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False) 
            x.save()
            messages.success(request, 'Sikeresen létrehozva!')
            return redirect('blog_category_index')
    else:
        form = BlogCategoryForm()
    return render(request, 'blog/create_category.html', {'form': form})

@login_required
def update_category(request, pk):
    category = BlogCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogCategoryForm(request.POST, request.FILES, instance=category)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('blog_category_index')
    else:
        form = BlogCategoryForm(instance=category)
    return render(request, 'blog/update_category.html', {'form': form})

@login_required
def delete_category(request, pk):
    query = BlogCategory.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('blog_category_index')

# OWNER
@login_required
def index_owner(request):
    try:
        owners = BlogOwner.objects.all()
    except BlogOwner.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'blog/index_owner.html', {'owners':owners})


@login_required
def details_owner(request):
    return HttpResponse('ewfe')

@login_required
def create_owner(request):
    if request.method == 'POST':
        form = BlogOwnerForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False) 
            x.save()
            messages.success(request, 'Sikeresen létrehozva!')
            return redirect('blog_owner_index')
    else:
        form = BlogOwnerForm()
    return render(request, 'blog/create_owner.html', {'form': form})

@login_required
def update_owner(request, pk):
    owner = BlogOwner.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogOwnerForm(request.POST, request.FILES, instance=owner)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('blog_owner_index')
    else:
        form = PostOwnerForm(instance=owner)
    return render(request, 'blog/update_owner.html', {'form': form})

@login_required
def delete_owner(request, pk):
    query = BlogOwner.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('blog_owner_index')