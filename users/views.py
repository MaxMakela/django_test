from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from typing import Optional
from django.views.generic import CreateView


class CreationUser(CreateView):
    """Render new user creation page."""
    form_class: Optional[UserCreationForm] = UserCreationForm
    template_name: str = 'registration/registration.html'
    # After successfully registration redirect to login URL
    success_url = reverse_lazy('login')
