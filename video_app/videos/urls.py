from django.contrib import admin
from django.urls import path, include
from videos import views as video_views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(video_views.home), name='home'),
    path('signup/', video_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='videos/login.html'), name='login'),
    path('videos/', login_required(video_views.video_list), name='video_list'),
    path('profile/', login_required(video_views.profile), name='profile'),
    path('accounts/', include('allauth.urls')),  # Include allauth URLs
    path('accounts/profile/', login_required(video_views.profile), name='profile'),
    path('watch/<int:video_id>/', login_required(video_views.video_detail), name='watch_video'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='videos/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='videos/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='videos/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='videos/password_reset_complete.html'), name='password_reset_complete'),
    path('video/<int:video_id>/', login_required(video_views.video_detail), name='video_detail'),
]
