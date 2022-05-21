# 엔카 1인 신조 차량 수집기

엔카에서 1인 신조 차량 필터를 제공하지 않아, 엔카 API 를 활용해서 차량의 보험이력을 크롤링해서 1인 신조 차량 목록을 구하는 프로젝트입니다.

### Requirements

* Python 3.8
* pytest
* Pycharm Community Edition

### Quickstart

```shell
$ git clone https://github.com/DongJinNam/encar-collector.git
$ cd ./encar-collector
$ python -m venv venv
$ source venv/activate
$ python -m pip install -r requirements.txt
```

### Process
* 엔카 차량 목록 API 호출
* 보험이력 조회 및 1인 신조차량 여부 체크
* 엑셀 파일 저장

### Files
* test_hyundai.py : 현대 차종별 1인 신조 차량 목록 조회
* test_kia.py : 기아 차종별 1인 신조 차량 목록 조회
* test_samsung.py : 르노 차종별 1인 신조 차량 목록 조회
* test_chevrolet.py : 쉐보레 차종별 1인 신조 차량 목록 조회

### Car Filters

해당 프로젝트에서 조회할 수 있는 차종 필터는 아래와 같습니다.
조회할 때 통풍시트 기본으로 조회합니다.

**현대**
* 그랜저
* 쏘나타
* 아반떼
* 싼타페
* 투싼

**기아**
* K7
* K5
* K3
* 레이 (통풍시트 X)
* 모닝 (통풍시트 X)
* 스포티지
* 쏘렌토

**르노삼성**
* SM6
* QM6

**쉐보레**
* 쉐보레