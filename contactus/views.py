from django.shortcuts import render, redirect

from .forms import ContactusForm
from .models import Contactus


def index(request):
    if request.method == 'POST':
        form = ContactusForm(request.POST)
        if form.is_valid():
            Contactus.objects.create(
                    subject = form.cleaned_data['subject'],
                    message = form.cleaned_data['message'],
                    sender = form.cleaned_data['sender'],
                )
            return redirect('contactus:contactus')
    else:
        form = ContactusForm()
        return render(request, 'contactus/index.html')

    return render(request, 'contactus/index.html', {'form':form})






def send(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print('form is created')
        if form.is_valid():
            instance = form.save()
            instance.save()
            return redirect('contactus:contactus')
    else:
        form = ContactForm()

    print('send func is ended')
    return render(request, 'contactus/index.html', {'form':form})
