import urllib.request
import json
import django
import os
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'humanscape.settings')
django.setup()

from app.develope.models import Clinical, Scope, Institution, Category, Phase, Department
from my_settings import encodingKey

def BatchTask():
    print("====================================")
    print("Success")
    print(datetime.now())

    key = encodingKey
    url = "https://api.odcloud.kr/api/3074271/v1/uddi:cfc19dda-6f75-4c57-86a8-bb9c8b103887?page=1&perPage=1000&serviceKey=" + key

    response    = urllib.request.urlopen(url)
    json_str    = response.read().decode("utf-8")
    json_object = json.loads(json_str)
    data        = json_object['data']

    print(data)
    for i in range(len(data)):
        research = Clinical.objects.all()
        if not research.filter(number=data[i]['과제번호']).exists():
            if not data[i]['전체목표연구대상자수'] =='':
                subject_number = int(data[i]['전체목표연구대상자수'])
            else: subject_number = None
            
            scope       = Scope.objects.get_or_create(scope=data[i]['연구범위'])
            category    = Category.objects.get_or_create(category=data[i]['연구종류'])
            institution = Institution.objects.get_or_create(institution=data[i]['연구책임기관'])
            phase       = Phase.objects.get_or_create(phase=data[i]['임상시험단계(연구모형)'])
            department  = Department.objects.get_or_create(department=data[i]['진료과'])
            
            Clinical.objects.create(
                number         = data[i]['과제번호'],
                name           = data[i]['과제명'],
                target_number  = subject_number,
                term           = data[i]['연구기간'],
                scope_id       = scope[0].id,
                category_id    = category[0].id,
                institution_id = institution[0].id,
                phase_id       = phase[0].id,
                department_id  = department[0].id
            )
        
        else:
            try:
                research = research.get(number=data[i]['과제번호'])

                if not data[i]['전체목표연구대상자수'] == '':
                    subject_number = int(data[i]['전체목표연구대상자수'])
                else: subject_number = None

                if not research.name == data[i]['과제명']:
                    research.name = data[i]['과제명']
                    research.save()
                
                if not research.term == data[i]['연구기간']:
                    research.term = data[i]['연구기간']
                    research.save()
                
                if not research.subject_number == subject_number:
                    research.subject_number = subject_number
                    research.save()
                
                if not research.category.category == data[i]['연구종류']:
                    category = Category.objects.get_or_create(category=data[i]['연구종류'])
                    research.category_id = category[0].id
                    research.save()
                
                if not research.scope.scope == data[i]['연구범위']:
                    scope = Scope.objects.get_or_create(scope=data[i]['연구범위'])
                    research.scaop_id = scope[0].id
                    research.save()
                
                if not research.institute.institute == data[i]['연구책임기관']:
                    institution = Institution.objects.get_or_create(institution=data[i]['연구책임기관'])
                    research.institution_id = institution[0].id
                    research.save()
                
                if not research.phase.phase == data[i]['임상시험단계(연구모형)']:
                    phase = Phase.objects.get_or_create(phase=data[i]['임상시험단계(연구모형)'])
                    research.phase = phase[0].id
                    research.save()
                
                if not research.department.department == data[i]['진료과']:
                    department  = Department.objects.get_or_create(department=data[i]['진료과'])
                    research.department = department[0].id
                    research.save()
                    
            except Clinical.DoesNotExist:
                return None