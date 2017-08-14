from django.shortcuts import render

# Create your views here.
from .models import Board
from .forms import MyModelForm
from django.utils import timezone


def index(request):
    list = Board.objects.order_by('-pub_date')[:3]
    context = {"list": list}
    if request.method == "POST":
        form = MyModelForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
    form = MyModelForm()
    return render(request, 'billboard/index.html', {'form': form, 'list': list})
