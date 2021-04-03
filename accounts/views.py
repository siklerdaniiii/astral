from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from django.contrib import messages
from .models import Account
from .forms import  AccountForm
from django.contrib.auth.decorators import login_required


@login_required
def account_list(request):
    try:
        accounts = Account.objects.all()
    except Account.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'accounts/index.html', {'accounts':accounts})

@login_required
def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False) 
            x.save()
            messages.success(request, 'Sikeresen létrehozva!')
            return redirect('account_list')
    else:
        form = AccountForm()
    return render(request, 'accounts/create.html', {'form': form})

@login_required
def account_update(request, pk):
    account = Account.objects.get(pk=pk)
    if request.method == 'POST':
        form = AccountForm(request.POST, request.FILES, instance=account)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('account_list')
    else:
        form = AccountForm(instance=account)
    return render(request, 'accounts/update.html', {'form': form})

@login_required
def account_delete(request, pk):
    query = Account.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('account_list')