from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('profile', views.profile, name='profile'),
    path('like', views.like, name='like'),
    path('like-post',views.like_post,name='like_post'),
    path('search',views.search,name='search'),
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)