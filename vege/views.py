# Core/vege/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Receipe
from .forms import RegisterForm, LoginForm

def about(request):
    return render(request, 'about.html')
def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Redirecting to receipes...")
            return redirect('receipes')
        else:
            messages.error(request, "Error in form submission. Please try again.")
    else:
        form = RegisterForm()
    
    return render(request, "register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('receipes')  # Redirect to receipes page after login
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, "login.html")


def confirm_logout(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, 'You have been logged out successfully.')
        return redirect('login')

    return render(request, 'confirm_logout.html')

def receipes(request):
    if not request.user.is_authenticated:
        return redirect('login')

    query = request.GET.get('search', '')
    receipes = Receipe.objects.filter(receipe_name__icontains=query) if query else Receipe.objects.all()

    if request.method == 'POST':
        receipe_name = request.POST.get('receipe_name')
        receipe_description = request.POST.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')

        Receipe.objects.create(
            user=request.user,
            receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        messages.success(request, 'Recipe added successfully!')

    context = {'receipes': receipes, 'search_query': query}
    return render(request, 'receipes.html', context)

def delete_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    receipe.delete()
    messages.success(request, 'Recipe deleted successfully!')
    return redirect('receipes')

def update_receipe(request, id):
    receipe = get_object_or_404(Receipe, id=id)
    if request.method == 'POST':
        receipe.receipe_name = request.POST.get('receipe_name')
        receipe.receipe_description = request.POST.get('receipe_description')
        if request.FILES.get('receipe_image'):
            receipe.receipe_image = request.FILES.get('receipe_image')
        receipe.save()
        messages.success(request, 'Recipe updated successfully!')
        return redirect('receipes')

    return render(request, 'update_receipe.html', {'receipe': receipe})

