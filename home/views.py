from django.shortcuts import render, redirect

from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe


def index(request):
    return render(request, 'home/index.html')


def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            print('form is valid')
            Subscribe.objects.create(email = form.cleaned_data['email'])
            return redirect('home:home')

    return redirect('home:home')
