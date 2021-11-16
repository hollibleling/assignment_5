# assignment_5
원티드x위코드 백엔드 프리온보딩 과제5
- 과제 출제 기업 정보
  - 기업명 : 휴먼스케이프
  
## Members
|이름   |Github                   |Blog|
|-------|-------------------------|--------------------|
|이태성 |[yotae07](https://github.com/yotae07)     | 추가   |
|임유선 |[YusunL](https://github.com/YusunL)   | 추가   |
|윤현묵 |[fall031-muk](https://github.com/fall031-muk) | https://velog.io/@fall031   |
|김정수 |[hollibleling](https://github.com/hollibleling) | https://velog.io/@hollibleling  |
|최현수 |[filola](https://github.com/filola) | https://velog.io/@chs_0303 |

## 과제 내용

- 임상정보를 수집하는 batch task
    - 참고: [https://www.data.go.kr/data/3074271/fileData.do#/API 목록/GETuddi%3Acfc19dda-6f75-4c57-86a8-bb9c8b103887](https://www.data.go.kr/data/3074271/fileData.do#/API%20%EB%AA%A9%EB%A1%9D/GETuddi%3Acfc19dda-6f75-4c57-86a8-bb9c8b103887)
- 수집한 임상정보에 대한 API
    - 특정 임상정보 읽기(키 값은 자유)
- 수집한 임상정보 리스트 API
    - 최근 일주일내에 업데이트(변경사항이 있는) 된 임상정보 리스트
        - pagination 기능

</aside>

### [필수 포함 사항]
- READ.ME 작성
    - 프로젝트 빌드, 자세한 실행 방법 명시
    - 구현 방법과 이유에 대한 간략한 설명
    - 완료된 시스템이 배포된 서버의 주소
    - Swagger나 Postman을 통한 API 테스트할때 필요한 상세 방법
    - 해당 과제를 진행하면서 회고 내용 블로그 포스팅
- Swagger나 Postman을 이용하여 API 테스트 가능하도록 구현

### [주요 고려 사항]
- **ORM 사용 필수**
- **데이터베이스는 SQLite로 구현**
- **secret key, api key 등을 레포지토리에 올리지 않도록 유의**
    - README.md 에 관련 설명 명시 필요
✔️ **API 상세설명**
---

- 임상 시험   
  
## 구현 기능
### 입금 기능
- 입금시 계좌번호, 거래 종류 선택, 금액, 적요를 받아 입금
- 입력된 계좌번호와 현재 유저의 account_number가 일치해야만 입금 가능
- 금액 중 음수(-)는 입력 불가능
- 계좌 계설을 안한 유저의 경우 에러 메세지 반환

### 출금 기능
- 입금 기능과 합쳐서 하나의 API로 기능 구현
- 마찬가지로 금액 중 음수(-)는 입력 불가능
- 계좌의 잔액보다 큰 금액을 출금 시도시 에러 메세지 반환

### 거래내역 조회 기능
- 기본적으로 전체 거래내역 조회 및 개별 거래내역 조회 가능
- Total 6개의 query params(period, start, end, year, month, kind)를 받아 4가지 필터 기능 구현
- period의 경우 전일, 금일, 3일 전, 일주일 전, 한달 전, 세달 전 부터 지금까지의 거래 내역을 조회 가능
- start, end 의 경우 원하는 거래내역의 시작일과 종료일을 정하여 거래 내역 조회 가능
- year, month는 특정한 년/월에 있었던 거래내역을 조회 가능
- kind는 예금, 출금을 구분하여 거래내역 조회 가능

## 기술 스택
- Back-End : python, django-rest-framework, sqlite3
- Tool     : Git, Github, slack, postman

## API

## 실행 방법(endpoint 호출방법)

### ENDPOINT

| Method | endpoint | Request Header | Request Body | Remark |
|:------:|-------------|-----|------|--------|
|POST|/user||name|회원가입 기능|
|POST|/token||name, password|로그인 기능|
|POST|/transaction|access_token|account_number, kind, amount, etc|입, 출금 기능|
|GET|/transaction/\<int\>|access_token||거래 내역 조회 기능(전체리스트/개별내역)|
|GET|/transaction?pariod=\<int\>&kind\<str\>|access_token||거래 내역 조회 기능(1,3,7,30,90일 별 + 입/출금)|
|GET|/transaction?start=\<str\>&end=\<str\>&kind\<str\>|access_token||거래 내역 조회 기능(기간설정 + 입/출금)|
|GET|/transaction?year=\<str\>&month=\<str\>&kind\<str\>|access_token||거래 내역 조회 기능(특정 년월 별 + 입/출금|



## API 명세(request/response)
  
  [Postman link](https://documenter.getpostman.com/view/17228945/UVC8CR6n)

## 폴더 구조
```
├── company
│   ├── __init__.py
│   ├── migrations           
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── pytest.ini
├── requirements.txt
├── README.md
├── test_app.py
└── wanted
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py


```

# Reference
이 프로젝트는 원티드x위코드 백엔드 프리온보딩 과제 일환으로 원티드랩에서 출제한 과제를 기반으로 만들었습니다.
