from django.views.generic import CreateView, View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Profile, CustomUser
from .forms import CustomUserCreationForm, UpdateProfileForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def profile(request):
    if request.method == "POST":
        profile_form = UpdateProfileForm(request.POST,
                                         request.FILES,
                                         instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request,
                             'Your profile informations have been updated.')
            return redirect('profile')
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)

    context = {'profile_form': profile_form}
    return render(request, 'accounts/profile.html', context)
