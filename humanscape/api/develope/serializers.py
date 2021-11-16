from rest_framework import serializers
from app.develope.models import ResearchData

class ResearchDataSerializer(serializers.Serializer):

    class Meta:
        model = ResearchData
        fields = ['research_id', 'title','department','institution','subjects_num','period','sort','stage','range' ]

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        instance = ResearchData.objects.create()
        return instance

    def update(self, instance, validated_data):
        return instance

    def to_representation(self, instance):
        return{
            '과제번호': instance.research_id,
            '과제명': instance.title,
            '진료과':  instance.department,
            '연구책임기관': instance.institution,
            '전체목표연구대상자수' : instance.subjects_num,
            '연구기간': instance.period,
            '연구종류': instance.sort,
            '임상시험단계(연구모형)': instance.stage,
            '연구범위': instance.range,
        }