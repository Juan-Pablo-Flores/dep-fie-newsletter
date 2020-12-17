from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SubscriberForm
from django.contrib import messages

@login_required
def home(request):
    return render(request, 'emails/home.html')


def register(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('name')
            messages.success(request, f'Has sido registrado exitosamente, {name}')
            return redirect('emails-success')
    else:
        form = SubscriberForm()
    return render(request, 'users/register.html', {'form': form})

def success(request):
    return render(request, 'users/success.html')