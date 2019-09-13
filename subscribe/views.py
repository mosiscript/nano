from django.shortcuts import render

from .forms import SubscribeForm
from .models import Subscribe

def index(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            Subscribe.objects.create(email = form.cleand_data['email'])