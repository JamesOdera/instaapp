from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .views import PostListView, PostCreateView
from . import views

urlpatterns=[
    url(r'^$',PostListView.as_view(),name = 'index'),
    url(r'^post/new/',PostCreateView.as_view(),name = 'post-create'),
    url(r'^about/',views.about,name = 'about'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)