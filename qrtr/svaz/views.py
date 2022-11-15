from django.shortcuts import render, redirect
from .forms import *


def svaz(request):
    if request.method == 'POST':
        form = SvazForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SvazForm()
    return render(request, 'svaz/svaz.html', {'form': form})
