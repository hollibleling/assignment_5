from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from api.develope.pagination import CustomPagination
from api.develope.serializers import ClinicalSerializer

from app.develope.models import Clinical

class ClinicalViewSet(ListModelMixin, GenericViewSet):
    queryset = Clinical.objects.all()
    serializer_class =  ClinicalSerializer
    permission_classes = [AllowAny]
    pagination_class = CustomPagination

    def get_queryset(self):
        department = self.request.query_params.get('department', None)
        institution = self.request.query_params.get('institution', None)
        category = self.request.query_params.get('category', None)
        phase = self.request.query_params.get('phase', None)
        scope = self.request.query_params.get('scope', None)

        if department:
            lists = Clinical.objects.filter(department_id__department=department)
        
        elif institution:
            lists = Clinical.objects.filter(institution_id__institution=institution)

        elif category:
            lists = Clinical.objects.filter(category_id__category=category)

        elif phase:
            lists = Clinical.objects.filter(phase_id__phase=phase)

        elif scope:
            lists = Clinical.objects.filter(scope_id__scope=scope)
        
        else:
            lists = Clinical.objects.all()
        
        return lists.order_by('updated_at')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object(kwargs['name'])
        if instance is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ClinicalSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

