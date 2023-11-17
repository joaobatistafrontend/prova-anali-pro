from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import ArtForm
from .models import ArtModel




@login_required
def home(request):
    if request.method == 'POST':
        form = ArtForm(request.POST, request.FILES)
        if form.is_valid():
            art_instance = form.save(commit=False)
            art_instance.user = request.user
            art_instance.save()
            return redirect('home')
    else:
        form = ArtForm()

    arts = ArtModel.objects.all()  # Obter todas as ARTs do usuário

    return render(request, 'home.html', {'form': form, 'arts': arts})





def singup(request):
     if request.method == 'POST':
          form = CustomUserCreationForm(request.POST)
          if form.is_valid():
               form.save()
               return redirect ('home')
     else:
          form = CustomUserCreationForm()
     return render(request, 'singup.html', {'form':form})