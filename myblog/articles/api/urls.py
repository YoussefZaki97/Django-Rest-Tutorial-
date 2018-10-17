from django.conf.urls import url
from . import views
from .views import (ArticleListAPIView, ArticleDetailAPIView)

app_name = "articles"

urlpatterns = [
    url(r'^$', ArticleListAPIView.as_view(), name = 'list' ),
    url(r'^(?P<slug>[\w-]+)/$', ArticleDetailAPIView.as_view(), name = 'detail'),
]
