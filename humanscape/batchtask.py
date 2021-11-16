import urllib.request
import json
import django
import os
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humanscape.settings')
django.setup()

from app.develope.models import ResearchInformation

def BatchTask():
    print("====================================")
    print("Success")
    print(datetime.now())
    encodingKey = "SfO9P5fMenC%2BsllZjDwBGoPlKepb7sGa%2BGHv2hnt%2Bdhe76QQ3ntEnIH3hajnGkjJTC6CqqNLvEWd9xWh7QE49A%3D%3D"
    decodingKey = "SfO9P5fMenC+sllZjDwBGoPlKepb7sGa+GHv2hnt+dhe76QQ3ntEnIH3hajnGkjJTC6CqqNLvEWd9xWh7QE49A=="

    url = "https://api.odcloud.kr/api/3074271/v1/uddi:cfc19dda-6f75-4c57-86a8-bb9c8b103887?page=1&perPage=1000&serviceKey=" + encodingKey

    response = urllib.request.urlopen(url)

    json_str = response.read().decode("utf-8")
    json_object = json.loads(json_str)
    data = json_object['data']

    for i in range(len(data)):
        research = ResearchInformation.objects.all()
        if not research.filter(number=data[i]['과제번호']).exists():
            if not data[i]['전체목표연구대상자수'] =='':
                subject_number = int(data[i]['전체목표연구대상자수'])
            else: subject_number = None
            ResearchInformation.objects.create(
                name = data[i]['과제명'],
                number = data[i]['과제번호'],
                period = data[i]['연구기간'],
                scope = data[i]['연구범위'],
                kind = data[i]['연구종류'],
                institute = data[i]['연구책임기관'],
                phase = data[i]['임상시험단계(연구모형)'],
                subject_number = subject_number,
                department = data[i]['진료과']
            )
        
        else:
            try:
                research = research.get(number=data[i]['과제번호'])
            except ResearchInformation.DoesNotExist:

                if not data[i]['전체목표연구대상자수'] == '':
                    subject_number = int(data[i]['전체목표연구대상자수'])
                else: subject_number = None

                if not research.name == data[i]['과제명']:
                    research.name = data[i]['과제명']
                    research.save()
                if not research.period == data[i]['연구기간']:
                    research.period = data[i]['연구기간']
                    research.save()
                if not research.scope == data[i]['연구범위']:
                    research.scaop = data[i]['연구범위']
                    research.save()
                if not research.kind == data[i]['연구종류']:
                    research.kind = data[i]['연구종류']
                    research.save()
                if not research.institute == data[i]['연구책임기관']:
                    research.institute = data[i]['연구책임기관']
                    research.save()
                if not research.phase == data[i]['임상시험단계(연구모형)']:
                    research.phase = data[i]['임상시험단계(연구모형)']
                    research.save()
                if not research.subject_number == subject_number:
                    research.subject_number = subject_number
                    research.save()
                if not research.department == data[i]['진료과']:
                    research.department = data[i]['진료과']
                    research.save()
                    