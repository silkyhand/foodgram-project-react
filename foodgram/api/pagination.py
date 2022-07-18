from django.conf import settings as s
from rest_framework.pagination import PageNumberPagination


class ProjectPagination(PageNumberPagination):
    page_size = s.PAGE_SIZE
