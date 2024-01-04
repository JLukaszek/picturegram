from django.contrib.auth.views import TemplateView, FormView
from django.contrib.auth.forms import AuthenticationForm


class IndexPageView(FormView):
    form_class = AuthenticationForm
    template_name = 'posts/startpage.html'
