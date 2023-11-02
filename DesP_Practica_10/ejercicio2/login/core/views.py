from django.shortcuts import render, redirect
#decorador
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# from .forms import CustomUserCreationForm
from .forms import UsuarioForm
from django.contrib.auth import authenticate, login
from .models import Interes, Aficion



#creando vistas
def home(request):
    return render(request, 'core/home.html')
@login_required
def products(request):
    return render(request, 'core/products.html')
def exit(request):
    logout(request)
    return redirect('home')

# def register(request):
#     data = {
#         'form': CustomUserCreationForm()
#     }
#     if request.method == "POST":
#         user_creation_form = CustomUserCreationForm(data=request.POST)

#         if user_creation_form.is_valid():
#             user_creation_form.save()
#             user = authenticate(username = user_creation_form.cleaned_data['username'], password =user_creation_form.cleaned_data['password1'])
#             login(request,user)
#             return redirect('home')
#     return render(request, 'registration/register.html', data)
    
def formulario(request):
    interes_choices = Interes.objects.values_list('name', 'name')
    aficion_choices = Aficion.objects.values_list('name', 'name')

    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UsuarioForm()

    return render(request, 'registration/formulario.html', {'form': form, 'interes_choices': interes_choices, 'aficion_choices': aficion_choices})