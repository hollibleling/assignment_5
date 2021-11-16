from django.core.exceptions import ValidationError
from django.db.models import fields
from app.develope.models import *
from rest_framework import serializers

class ClinicalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Clinical
        fields = ['id', 'number', 'name', 'target_number', 'term', 'department_id', 'institution_id', 'category_id', 'phase_id', 'scope_id']

    def validate_category_id(self, value):
        try:
            if Category.objects.get(id=value).category not in [Category.OBSERVATIONAL, Category.INTERVENTIONAL]:
                return ValidationError("Category Error")
            
            return value
        except Category.DoesNotExist:
            return ValidationError("Category Error")

    def to_representation(self, instance):
        return{
            '과제번호': instance.number,
            '과제명': instance.name,
            '진료과':  instance.department.department,
            '연구책임기관': instance.institution.institution,
            '전체목표연구대상자수' : instance.target_number,
            '연구기간': instance.term,
            '연구종류': instance.category.category,
            '임상시험단계(연구모형)': instance.phase.phase,
            '연구범위': instance.scope.scope,
        }