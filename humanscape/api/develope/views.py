from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny

from .serializers import ResearchDataSerializer
from app.develope.models import ResearchData

from datetime import datetime, timedelta


import csv




class ResearchDataViewSet(ListModelMixin, CreateModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = ResearchData.objects.all()
    serializer_class = ResearchDataSerializer
    permission_classes = [AllowAny]


    def get_queryset(self, updated, title, inst, research_id):
        returnData = ResearchData.objects.filter(title=title, institution=inst, research_id=research_id )
        if updated == '1':
            returnData.filter(updated_at__gte=datetime.now()-timedelta(days=7))
        return returnData

    def list(self, request, *args, **kwargs):
        updated = self.request.query_params.get('updated_only','0')
        title = self.request.query_params.get('title','')
        inst = self.request.query_params.get('inst','')
        research_id = self.request.query_params.get('id', '')
        queryset = self.get_queryset(updated, title, inst, research_id)
        page =self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer_class(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer_class(queryset, many=True)
        return Response(serializer.data)

    # def import_csv(self):
    #     with open('C:/Users/imyur/Documents/GitHub/assignment_5/data.csv','r')as f:
    #         dr = csv.DictReader(f)
