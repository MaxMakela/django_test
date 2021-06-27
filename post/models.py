from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    text = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Get title field as object string interpretation."""
        return self.title

    def get_absolute_url(self):
        """Get absolute post URL."""
        return reverse('post', kwargs={'pk': self.pk})
