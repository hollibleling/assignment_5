from django.db.models.fields import NullBooleanField
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status

from app.develope.models import ResearchInformation

class ResearchInformationTestCase(APITestCase):
    def setUp(self):
        ResearchInformation.objects.create(
            id=1,
            name = "조직구증식증 임상연구 네트워크 구축 및 운영(HLH)",
            number = "C130010",
            period = "3년",
            scope = "국내다기관",
            kind = "관찰연구",
            institute = "서울아산병원",
            phase = "코호트",
            subject_number = 120,
            department = "Pediatrics"
        )

        ResearchInformation.objects.create(
            id=2,
            name = "대한민국 쇼그렌 증후군 코호트 구축",
            number = "C130011",
            period = "6년",
            scope = "국내다기관",
            kind = "관찰연구",
            institute = "가톨릭대 서울성모병원",
            phase ="코호트",
            subject_number = 500,
            department ="Rheumatology"
        )

    def tearDown(self):
        ResearchInformation.objects.all().delete()

    def test_list_research_data(self):
        response = self.client.get('/list', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "과제명": "조직구증식증 임상연구 네트워크 구축 및 운영(HLH)",
                    "과제번호": "C130010",
                    "연구기간": "3년",
                    "연구범위": "국내다기관",
                    "연구종류": "관찰연구",
                    "연구책임기관": "서울아산병원",
                    "임상시험단계(연구모형)": "코호트",
                    "전체목표연구대상자수": 120,
                    "진료과": "Pediatrics"
                },
                {
                    "과제명": "대한민국 쇼그렌 증후군 코호트 구축",
                    "과제번호": "C130011",
                    "연구기간": "6년",
                    "연구범위": "국내다기관",
                    "연구종류": "관찰연구",
                    "연구책임기관": "가톨릭대 서울성모병원",
                    "임상시험단계(연구모형)": "코호트",
                    "전체목표연구대상자수": 500,
                    "진료과": "Rheumatology"
                }   
            ]
        }
        self.assertEqual(response.json(), expected_data)

    def test_search_research_data(self):
        response = self.client.get('/trials?name=조직구증식증', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "과제명": "조직구증식증 임상연구 네트워크 구축 및 운영(HLH)",
                    "과제번호": "C130010",
                    "연구기간": "3년",
                    "연구범위": "국내다기관",
                    "연구종류": "관찰연구",
                    "연구책임기관": "서울아산병원",
                    "임상시험단계(연구모형)": "코호트",
                    "전체목표연구대상자수": 120,
                    "진료과": "Pediatrics"
                }   
            ]
        }
        self.assertEqual(response.json(), expected_data)

    def test_search_research_data_no_result(self):
        response = self.client.get('/trials?name=거식증', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_data = {
            "count": 0,
            "next": None,
            "previous": None,
            "results": []
        }
        self.assertEqual(response.json(), expected_data)