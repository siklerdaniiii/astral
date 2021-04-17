from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
from .forms import ContactForm
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    try:
        contacts = Contact.objects.all()
    except Contact.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'contacts/index.html', {'contacts':contacts})

@login_required
def details(request, pk):
    try:
        contact = Contact.objects.get(pk = pk)
    except Contact.DoesNotExist:
        raise Http404("404 | Nem létezik!")
    return render(request, 'contacts/details.html', {'contact':contact})

@login_required
def update(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=contact)
        form.save()
        messages.success(request, 'Sikeresen módosítva!')
        return redirect('contact_index')
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contacts/update.html', {'form': form})

@login_required
def delete(request, pk):
    query = Contact.objects.get(pk=pk)
    query.delete()
    messages.success(request, 'A törlés sikeres!')
    return redirect('contact_index')