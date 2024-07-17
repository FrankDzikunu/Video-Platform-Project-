from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Video  # Adjust the import path as per your project structure
from django.core.paginator import Paginator
# views.py
from django.contrib.auth import logout


@login_required
def home(request):
    video_list = Video.objects.all()
    paginator = Paginator(video_list, 1)  # Show 1 video per page

    page_number = request.GET.get('page')
    videos = paginator.get_page(page_number)
    return render(request, 'videos/home.html', {'videos': videos})

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
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'videos/signup.html', {'form': form})

@login_required
def video_list(request):
    # You can replace this with actual video retrieval logic
    return render(request, 'videos/video_list.html')

@login_required
def profile(request):
    return render(request, 'videos/profile.html')  # Replace 'profile.html' with your actual template


def custom_logout(request):
    logout(request)
    return redirect('login')

