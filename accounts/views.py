from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from .models import Profile, CustomUser
from .forms import CustomUserCreationForm, UpdateProfileForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(UpdateView):
    model = Profile
    form_class = UpdateProfileForm
    template_name = 'accounts/profile.html'
    fields = ['city', 'hobby', 'age', 'profile_pic']
    success_url = reverse_lazy('profile')

