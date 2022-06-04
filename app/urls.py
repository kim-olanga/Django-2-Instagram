from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login/',views.loginPage,name='login'),
    path('signup/',views.signupPage,name='signup'),
    path('', views.index,name='index'),
    path('new-post/', views.newPost,name='new-post'),

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)