from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from django.contrib import messages
from .models import Plan, Member
from .forms import  PlanForm, MemberForm
from django.contrib.auth.decorators import login_required
# Create your views here.



@login_required
def plan_index(request):
    try:
        plans = Plan.objects.all()
    except Plan.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'memberships/plan_index.html', {'plans':plans})

@login_required
def plan_create(request):
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False) 
            x.save()
            messages.success(request, 'Sikeresen létrehozva!')
            return redirect('plan_index')
    else:
        form = PlanForm()
    return render(request, 'memberships/plan_create.html', {'form': form})

@login_required
def plan_update(request, pk):
    plan = Plan.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES, instance=plan)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('plan_index')
    else:
        form = PlanForm(instance=plan)
    return render(request, 'memberships/plan_update.html', {'form': form})

@login_required
def plan_delete(request, pk):
    query = Plan.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('plan_index')


#Member views

@login_required
def member_index(request):
    try:
        members = Member.objects.all()
    except Member.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'memberships/index.html', {'members':members})

@login_required
def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            x = form.save(commit=False) 
            x.save()
            messages.success(request, 'Sikeresen létrehozva!')
            return redirect('member_index')
    else:
        form = MemberForm()
    return render(request, 'memberships/create.html', {'form': form})

@login_required
def member_update(request, pk):
    member = Member.objects.get(pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('member_index')
    else:
        form = MemberForm(instance=member)
    return render(request, 'memberships/update.html', {'form': form})

@login_required
def member_delete(request, pk):
    query = Member.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('member_index')