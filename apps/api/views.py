from rest_framework import viewsets

from .serializers import CategorySerializer, EntrySerializer
from blog.models import Category, Entry


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer