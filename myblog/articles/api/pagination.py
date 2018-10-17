from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)

class ArticleOffsetLimitPagination:
    default_limit = 2
    max_limit = 10

class ArticlePageNumberPagination:
    page_size = 2
