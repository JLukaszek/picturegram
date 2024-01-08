from django.views.generic import TemplateView
from django.contrib.auth.views import FormView
from django.contrib.auth.forms import AuthenticationForm


class IndexPageView(FormView):
    form_class = AuthenticationForm
    template_name = 'posts/startpage.html'


class AboutPageView(TemplateView):
    template_name = 'posts/about.html'
