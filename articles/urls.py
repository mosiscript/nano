from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name = 'articles'),
    path('article/send', views.send, name = 'article.send'),
    # path('article/send/store', views.send, name = 'article.send.store'),
    path('<int:article_id>', views.single, name = 'article'),
    path('<int:article_id>/edit', views.edit, name='article.edit'),

]
