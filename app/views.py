from django.shortcuts import redirect, render
from .forms import WidgetForm
from django.http import HttpResponse


def home(request):
    form = WidgetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return HttpResponse('form not valid')
    context = {
        'form': form
    }
    return render(request, 'app/home.html', context)


