from rest_framework import serializers

from app.develope.models import *

class DevelopeListSerializer(serializers.ModelSerializer):
    number = serializers.CharField(max_length=128)
    name = serializers.CharField(max_length=512)
    subject = serializers.CharField(max_length=128)
    agency = serializers.CharField(max_length=64)
    target_count = serializers.IntegerField()
    period = serializers.CharField(max_length=16)
    kind = serializers.CharField(max_length=64)
    phase = serializers.CharField(max_length=64)
    scope = serializers.CharField(max_length=64)

    class Meta:
        model = DevelopeList
        fields = ['id', 'number', 'name', 'subject', 'agency', 'target_count', 'period', 'kind_id', 'phase_id', 'scope_id']
    
    def to_representation(self, instance):
        kind_id = instance.kind_id
        phase_id = instance.phase_id
        scope_id = instance.scope_id

        return {
            "과제명": instance.name,
            "과제번호": instance.number,
            "연구기간": instance.period,
            "연구범위": Scope.objects.get(id = scope_id).name,
            "연구종류": Kind.objects.get(id = kind_id).name,
            "연구책임기관": instance.agency,
            "임상시험단계(연구모형)": Phase.objects.get(id = phase_id).name,
            "전체목표연구대상자수": instance.target_count,
            "진료과": instance.subject
            }
