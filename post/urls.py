from django.urls import path
from .views import (
    Home,
    PostDetails,
    PostAdding,
    PostUpdating,
    PostDeleting,
)

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('post/<int:pk>', PostDetails.as_view(), name="post"),
    path('new_post/', PostAdding.as_view(), name="new_post"),
    path('post/edit/<int:pk>', PostUpdating.as_view(), name="update_post"),
    path('post/delete/<int:pk>', PostDeleting.as_view(), name="delete_post"),
]
