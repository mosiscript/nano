from django.shortcuts import render, redirect

from .forms import EnrollForm
from .models import Enroll


def index(request):
    if request.method == 'POST':
        form = EnrollForm(request.POST)
        if form.is_valid():
            Enroll.objects.create(
                    name = form.cleaned_data['name'],
                    email = form.cleaned_data['email'],
                    mobile = form.cleaned_data['mobile'],
                )
            return redirect('enroll:enroll')
    else:
        form = EnrollForm()
        return render(request, 'enroll/index.html')

    return render(request, 'enroll/index.html', {'form':form})


