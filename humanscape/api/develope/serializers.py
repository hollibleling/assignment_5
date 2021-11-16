from rest_framework import serializers

from app.develope.models import ResearchInformation

class ResearchInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResearchInformation
        fields = ["name", "number", "period", "scope", "kind", "institute", "phase", "subject_number", "department"]

    def to_representation(self, instance):

        return {
            "과제명": instance.name,
            "과제번호": instance.number,
            "연구기간": instance.period,
            "연구범위": instance.scope,
            "연구종류": instance.kind,
            "연구책임기관": instance.institute,
            "임상시험단계(연구모형)": instance.phase,
            "전체목표연구대상자수": instance.subject_number,
            "진료과": instance.department
        }