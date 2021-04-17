from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from django.contrib import messages
from .models import Post, PostCategory, PostOwner
from memberships.models import Plan, Member
from .forms import  PostForm, PostCategoryForm, PostOwnerForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.



@login_required
def index(request):
    try:
        posts = Post.objects.all()
    except Post.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'posts/index.html', {'posts':posts})

def index2(request, uid):
    #Uid alapján lekérdezés full kód!!!!
    #uid = '2423rferfew'
    member = Member.objects.filter(Q(member_uid = uid) and Q(member_status = 1)).order_by('member_since').first()  #rendezve a legutolsó előfizetés szerint
    
    #id alapján megnézem, hogy member e
    is_member = Member.objects.filter(member_uid = uid).last()
    #ha member akkor lekérem azt, hogy aktiv e
    if is_member and is_member.member_status == 1:
        print('Ő member és aktív is')
        #ha aktív akkor lekérem a hozzá tartozó cikkeket, ha nem akkor ingynees tartalmat jeleniti meg neki
        member_plan = is_member.member_plan.plan_slug #aktuális tagság
        print(member_plan)
        posts = Post.objects.filter(Q(post_plan__plan_slug = member_plan) or Q(post_plan__plan_slug = 'free')).distinct()
        print(posts)
    else:
        print('Nem member vagy nem aktiv')
        posts = Post.objects.filter(post_plan__plan_slug = 'free')
        print('Ingyenes psoztok:',posts)
    #
    


    return HttpResponse('e')



@login_required
def details(request):
    return HttpResponse('ewfe')

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False) 
            x.save()
            messages.success(request, 'Sikeresen létrehozva!')
            return redirect('post_index')
    else:
        form = PostForm()
    return render(request, 'posts/create.html', {'form': form})

@login_required
def update(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('post_index')
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/update.html', {'form': form})

@login_required
def delete(request, pk):
    query = Post.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('post_index')


# OWNER
@login_required
def index_owner(request):
    try:
        owners = PostOwner.objects.all()
    except PostOwner.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'posts/index_owner.html', {'owners':owners})


@login_required
def details_owner(request):
    return HttpResponse('ewfe')

@login_required
def create_owner(request):
    if request.method == 'POST':
        form = PostOwnerForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False) 
            x.save()
            messages.success(request, 'Sikeresen létrehozva!')
            return redirect('post_owner_index')
    else:
        form = PostOwnerForm()
    return render(request, 'posts/create_owner.html', {'form': form})

@login_required
def update_owner(request, pk):
    owner = PostOwner.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostOwnerForm(request.POST, request.FILES, instance=owner)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('post_owner_index')
    else:
        form = PostOwnerForm(instance=owner)
    return render(request, 'posts/update_owner.html', {'form': form})

@login_required
def delete_owner(request, pk):
    query = PostOwner.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('post_owner_index')


# CATEGORY
@login_required
def index_category(request):
    try:
        categories = PostCategory.objects.all()
    except PostCategory.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'posts/index_category.html', {'categories':categories})


@login_required
def details_category(request):
    return HttpResponse('ewfe')

@login_required
def create_category(request):
    if request.method == 'POST':
        form = PostCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False) 
            x.save()
            messages.success(request, 'Sikeresen létrehozva!')
            return redirect('post_category_index')
    else:
        form = PostCategoryForm()
    return render(request, 'posts/create_category.html', {'form': form})

@login_required
def update_category(request, pk):
    category = PostCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostCategoryForm(request.POST, request.FILES, instance=category)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('post_category_index')
    else:
        form = PostCategoryForm(instance=category)
    return render(request, 'posts/update_category.html', {'form': form})

@login_required
def delete_category(request, pk):
    query = PostCategory.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('post_category_index')

