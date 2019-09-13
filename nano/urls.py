from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from posts import views as post_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('contactus/', include('contactus.urls')),
    path('register/', include('enroll.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('posts/', include('posts.urls', namespace='posts')),
    # path('posts/', post_views.post_home),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
