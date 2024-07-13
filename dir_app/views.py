from django.shortcuts import render, redirect
from .models import Creator, How_it_works, Explore, Client_reviews, Reviews, Blog, About_web
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    creator = Creator.objects.all()
    how_w = How_it_works.objects.all()
    explore = Explore.objects.all()
    client_reviews = Client_reviews.objects.all()
    reviews = Reviews.objects.all()
    blog = Blog.objects.all()
    about = About_web.objects.all()
    
    context = {
        'creator':creator,
        'how_w': how_w,
        'explore': explore,
        'client_reviews': client_reviews,
        'reviews': reviews,
        'blog': blog,
        'about': about,
    }
    return render(request, 'index.html', context)
    
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        
        if username and password: 
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
           
    return render(request, 'sign_in.html')
    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            print(request, "Passwords do not match.")
            return render(request, 'register.html')
        
        if User.objects.filter(username=username).exists():
            print(request, "Username is already taken.")
            return render(request, 'register.html')
        
        user = User.objects.create_user(username=username)
        user.set_password(password)
        user.save()
        
        print(request, "Registration successful. You can now login.")
        return redirect('index')
    

    return render(request, 'register.html')
    
    
def sign_out(request):
    logout(request)
    return redirect('index')
