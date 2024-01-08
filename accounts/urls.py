from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.CurrentUserDetailView.as_view(), name='current_user_profile'),
    path('profile/update/', views.profile, name='profile_settings'),
    path('<int:pk>/', views.AccountDetailView.as_view(),
         name='profile_detail'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='registration/pw_reset_form.html'),
         name='pw_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/pw_reset_done.html'),
         name='pw_reset_done'),
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/pw_reset_confirm.html'),
         name='pw_reset_confirm'),
    path('reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='registration/pw_reset_complete.html'),
         name='pw_reset_complete'),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='registration/pw_change.html'),
         name='pw_change'),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='registration/pw_change_done.html'),
         name='pw_change_done'),
]
