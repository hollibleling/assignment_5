from django.utils import timezone
from datetime import datetime, timedelta

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.pagination import PageNumberPagination

from app.develope.models import *
from .serializers import DevelopeListSerializer
from api.develope.pagination import ListPagination


class DevelopeListViewSet(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = DevelopeList.objects.all()
    serializer_class = DevelopeListSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        updated = self.request.query_params.get('updated')
        number = self.request.query_params.get('number')
        title = self.request.query_params.get('title')

        date = timezone.now()
        searched_data = DevelopeList.objects.all()

        if updated:
            searched_data = DevelopeList.objects.filter(updated_at__range = [(date - timedelta(7)).strftime('%Y-%m-%d'), date.strftime('%Y-%m-%d')])
        if number:
            searched_data = DevelopeList.objects.filter(number = number)
        if title:
            searched_data = DevelopeList.objects.filter(name__icontains = title)
        
        return searched_data
