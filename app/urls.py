from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.homepage, name='homepage'),
    re_path('like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
    re_path('profile/(\d+)', views.user_profile, name='profile'),
    re_path('new/profile', views.add_user_profile, name='add_profile'),
    re_path('search/', views.search_results, name='search_results'),
    re_path('comment/(?P<pk>\d+)',views.user_comments,name='comment'),
    re_path('follow/(?P<operation>.+)/(?P<id>\d+)',views.follow,name='follow'),
    re_path('upload/', views.upload_image, name='upload_image'),
    re_path('all/(?P<pk>\d+)', views.images, name='images'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)