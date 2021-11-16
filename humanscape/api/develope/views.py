from rest_framework import pagination, serializers
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from datetime import datetime, timedelta

from .serializers import ResearchInformationSerializer
from app.develope.models import ResearchInformation
from api.pagination import CustomPagination

class ResearchInformationViewset(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset         = ResearchInformation.objects.all()
    serializer_class = ResearchInformationSerializer
    pagination_class = CustomPagination

    def list(self, request, *args, **kwargs):
        word = self.request.query_params.get('name', None)
        if word:
            queryset = self.get_queryset().filter(name__contains = word)
        else:
            queryset = self.get_queryset().filter(updated_at__range=[datetime.now()-timedelta(weeks=1), datetime.now()])

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)