from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializers import ArticleSerializer
from articles.models import Article
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)

class ArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title','body','slug','date']
    pagination_class = LimitOffsetPagination


    def get_queryset(self,*args, **kwargs):
        query_list = Article.objects.all()
        query = self.request.GET.get("q")
        if query:
            query_list = query_list.filter(
                    Q(title__icontains=query)|
                    Q(slug__icontains=query)
                    ).distinct()
        return query_list

class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'slug'
