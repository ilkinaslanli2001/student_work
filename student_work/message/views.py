from django.shortcuts import render
from .forms import MessageForm


def index(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('Wrong method')
    form = MessageForm()
    data = {
        'form': form,
    }
    return render(request, 'messages/index.html', data)
