from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Video
from .forms import SearchForm
from django.core.paginator import Paginator

@login_required
def home(request):
    form = SearchForm(request.GET or None)
    query = request.GET.get('query', '')
    
    if query:
        video_list = Video.objects.filter(title__icontains=query)
    else:
        video_list = Video.objects.all()

    paginator = Paginator(video_list, 1)  # Show 1 video per page

    page_number = request.GET.get('page')
    videos = paginator.get_page(page_number)
    
    return render(request, 'videos/home.html', {
        'videos': videos,
        'form': form,
    })

@login_required
def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    previous_video = Video.objects.filter(id__lt=video.id).order_by('-id').first()
    next_video = Video.objects.filter(id__gt=video.id).order_by('id').first()
    return render(request, 'videos/video_detail.html', {
        'video': video,
        'previous_video': previous_video,
        'next_video': next_video
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account_login')  # Redirect to the login page
    else:
        form = UserCreationForm()
    return render(request, 'videos/signup.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'videos/login.html', {'error': 'Invalid username or password'})
    return render(request, 'videos/login.html')

@login_required
def video_list(request):
    videos = Video.objects.all()
    context = {
        'videos': videos,
    }
    return render(request, 'videos/video_list.html', context)

@login_required
def profile(request):
    return render(request, 'videos/profile.html')  

def custom_logout(request):
    logout(request)
    return redirect('login')

def email_verification_sent(request):
    return render(request, 'videos/email_verification_sent.html')

def search_view(request):
    form = SearchForm(request.GET or None)
    query = request.GET.get('query', '')

    if query:
        video_list = Video.objects.filter(title__icontains=query)
    else:
        video_list = Video.objects.all()

    paginator = Paginator(video_list, 6)  # Show 6 video per page
    page_number = request.GET.get('page')
    videos = paginator.get_page(page_number)

    return render(request, 'videos/search.html', {
        'videos': videos,
        'form': form,
        'query':query,
    })
