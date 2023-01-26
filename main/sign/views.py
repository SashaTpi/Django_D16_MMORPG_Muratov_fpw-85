from .models import BaseRegisterForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


class BaseRegisterView(CreateView):
    model = User
    template_name = 'signup.html'
    form_class = BaseRegisterForm
    success_url = reverse_lazy('login')


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')
