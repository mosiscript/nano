from django.urls import path
from .views import (
    post_list,
    post_create,
    post_detail,
    post_update,
    post_delete,
)

app_name = 'posts'
urlpatterns = [
    # path('', views.post_home, name = 'posts'),
    path('', post_list, name = 'post_list'),
    path('create/', post_create, name = 'post_create'),
    # path('detail/<int:id>', post_detail, name = 'post_detail'),
    path('<int:id>/', post_detail, name = 'post_detail'),  # posts/id
    path('<int:id>/edit/', post_update, name = 'post_update'),
    path('<int:id>/delete/', post_delete, name = 'post_delete'),

]