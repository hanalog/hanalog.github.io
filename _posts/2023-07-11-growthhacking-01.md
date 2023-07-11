---
layout: single
title: "[Analysis] 그로스 해킹 (1)"
category: "DataAnalysis"
tag: [analysis]
author_profile: false
sidebar:
  nav: "docs"
toc: true
toc_label: "Contents"
toc_icon: "list-ul"
classes : wide
---

# 그로스 해킹 1 :

그로스 해킹이란, 그로스 해킹의 전제조건

## 1. 그로스 해킹이란?

그로스 해킹의 목적은 데이터에서 찾아낸 인사이트를 바탕으로 제품이나 서비스를 지속적으로 개선해 나가기 위해서다.

### 1.1. 그로스 해킹 핵심

- **크로스 펑셔널 팀 (Cross-Functional Team)**
  - 여러 직군 간 협업이 필수적
  - 기능 기반 조직이 아닌 목적 기반 조직의 협업
- **린 스타트업 (Lean Startup)**
  - IMVU의 공동 창업자 에릭 리스가 제안한 개념
  - 학습 비용을 최소화하고 성공 가능성 높이는 제품 개발 프로세스
  - 제품 개발 → 지표 측정 → 학습 및 개선
  - 아무도 원하지 않는 제품을 오랜 기간 만드는 것은 실패의 지름길
- **최소 기능 제품 (Minimum Viable Product, MVP)**
  - 린 스타트업에서 강조하는 요소
  - 가설을 검증할 수 있는 최소한의 기능이 포함된 제품
  - 서비스 개선은 기능 추가가 아니다!
  - **최소한의 기능으로 사용자에게 가치를 전달**할 수 있는 제품이 성공한다!
- **AARRR**
  - 그로스 해킹 기반의 대표적인 지표 관리 방법론
  - 스타트업의 성장을 위해 고객 유치, 활성화, 리텐션, 수익화, 추천 범주에 따라 지표 모니터링

### 1.2. 그로스 해킹이란!

- **크로스 펑셔널**한 직군의 멤버들이 모여서
- 최소 기능 제품으로 **실험**하고
- **핵심 지표**(AARRR)를 중심으로 학습하고
- 이를 빠르게 **반복**하면서
- 제품이나 서비스를 **성장**시키는 것

## 2. 그로스 해킹의 전제조건

개발하고자 하는 제품이 수요가 없는 제품이라면 어떤 그로스 해킹 방법론을 적용해도 제품은 성공할 수 없다. 따라서, 우리가 만든 제품이 그로스 해킹을 할 만큼 가치가 있는지 먼저 확인해야 한다.

### 2.1. 제품-시장 적합성 (Product-Market Fit)

- 우리가 생각한 문제가 실존하는가? 사업화 할 만큼의 가치가 있는가?
- 우리가 개발한 제품이 그 문제를 정말 해결하는가?
- 제품을 만드는 과정에서 세운 가설이 무엇인가? 그 가설이 검증되었는가?

### 2.2. PMF 확인을 위한 정량적 지표 3가지

설치 수, 가입자 수, 액티브 유저 수는 적합성 및 제품 성공 확률을 설명해주지 않는다. 단순히 마케팅 예산을 늘리면 일시적으로 늘어날 수 있는 부분이기 때문이다. 따라서 아래의 3가지 지표를 통해 그로스 실험을 진행해도 될지 판단하고, 충분하지 않다고 판단되면 위 3가지 질문을 다시 한 번 점검해봐야 한다.

#### (1) 리텐션 (Retention Rate)

- 특징
  - 사용자들이 특정 서비스에 남아서 얼마나 꾸준히 활동하는지 보여주는 지표
  - 일반적으로 시간이 지남에 따라 자연스럽게 감소
  - 핵심 기간은 서비스 사용 시작 직후 수일 이내
  - 서비스가 속한 카테고리의 영향을 많이 받기 때문에 절대적인 기준은 없음
    - 매일 보는 웹툰 앱 리텐션 수치 > 가끔 가는 여행 예약 앱 리텐션 수치
- 적합성 만족
  - 일정 기간 이후 기울기가 완만해지면서 안정적으로 유지되는가?
  - 기울기가 완만해지는 지점 높이가 높은가?

#### (2) 전환율 (Conversion Rate)

- 특징
  - 한 단계에서 다음 단계로 넘어가는 사용자의 비율
  - 서비스의 **핵심 사용 경로에 대한 전환율 지표** 확인
    - 앱 다운 → 회원 가입  → 본인 인증 → 상품 페이지 조회 → 구매하기 클릭 → 결제완료
  - 사용성, UI/UX 의 영향을 많이 받는 지표기도 함
  - 단계가 거듭될 수록 이탈이 늘어나기에 전환 퍼널은 역삼각형 형태
- 방법
  - 목표 이벤트 지정 → 목표로 향하는 경로/단계 구체화 → 각 경로 진입 대비 다음 경로 진입 비율 계산
- 적합성 만족
  - 모바일 앱 트래킹 서비스나 리서치 회사에서 발표하는 정기적인 리포트의 기댓값 참고
    - 예) 어도비 디지털 인덱스
  - 상품 카테고리에 따라 전환율 차이 있음
    - 선물/건강 관련 상품 > 전자기기
  - 유입 트래픽 출처에 따라 전환율 차이 있음
    - 친구 추천 링크 클릭 > 광고 클릭
  - 다양한 변수에 영향을 받기 때문에 수치 자체보다 시간의 흐름에 따른 변화 추이 확인

#### (3) 순수 추천 지수 (Net Promoter Score, NPS)

- 특징
  - 비교적 간단하게 서비스 성공 여부 예측 가능한 지표
  - 제품에 대한 열성 Fan 지표
  - Passives 그룹은 경쟁 제품이 나오면 이탈 가능성 높으며, NPS 계산에서 제외
  - -1 ≤ NPS ≤ 1
- 방법
  - “이 서비스를 주변 지인에게 얼마나 추천하고 싶은가?” 질문에 0-10점 선택지에서 답변
  - 3개 그룹으로 구분
    - 9-10점 → 적극적 추천 그룹 (Promoters)
    - 7-8점 → 소극적 추천 그룹 (Passives)
    - 0-6점 → 비추천 그룹 (Detractors)
  - **NPS = (Promoters - Detractors) / 전체 응답자**
- 적합성 만족
  - 전반적으로 NPS가 양수라면 양호
    - 일반적으로 0-6점 그룹보다 9-10점 그룹이 더 많은 것 자체가 굉장히 어려움

### 2.3. PMF 를 만족하지 못한다면

#### (1) 해서는 안 된다!

- 브레인스토밍
- 새로운 기능 추가
- 잔존율, 전환율 개선을 위한 실험
  - 잔존율과 전환율은 제품-시장 적합성을 찾고 난 이후 결과로 나타나는 지표에 불과
  - 잔존율과 전환율은 확인하는 수단일 뿐 목적이 될 수 없음

#### (2) 해야 한다!

- **정성적 데이터 수집 : 사용자 직접 만나 1:1 인터뷰**
  - 미래가 아닌, **과거와 현재**에 초점을 맞춰 질문할 것
  - 가정이 아닌, **경험**을 물어볼 것
  - 결과가 아닌, **과정**을 깊이 살펴볼 것
  - 기억이 아닌, **습관을 통해 드러난 구체적 경험**을 확인할 것
  - 일반화된 진술이 아닌, **개인의 경험**이 드러날 수 있도록 질문 / 답변할 것
  - 편향된 믿음을 확인하는 과정이 아닌, **순수한 호기심**으로 접근할 것
  - 참고 서적 : `사용자 인터뷰(지앤선, 2015)`, `야생의 고객(김영사, 2015)`, `질문이 답을 바꾼다(어크로스, 2012)`
- **정량적 데이터 활용 : 사용자 행동 데이터 분석**
  - 서비스 로그
    - 트랜잭션의 결과를 기록하는 로그
    - 가입 / 예약 / 결제 등 하나의 트랜잭션이 완료되면 남는 로그
  - 행동 로그
    - 사용자가 트랜잭션에 이르기까지 서비스에서 하는 액션 하나하나에 대한 로그
    - 특정 상품 클릭, 검색, 배너 스와이프 등
    - 카테고리, 상품명, 가격, 이벤트 대상 여부, 평점 등의 이벤트 속성
    - 가입일, 누적 구매건수, 성별, 쿠폰 여부, 쿠폰 만료일 등의 사용자 속성
    - 이벤트 스키마 설계서 작성 필수
    - 이벤트 로그 적재 시 아마존 레드시프트, 구글 빅쿼리 등의 클라우드 DB 적합
    - 참고 포스팅 : [모바일 앱 로그 분석](https://brunch.co.kr/@leoyang99/15)
- 최종적으로 다음과 같이 정리
  - 의도한 대로 사용자가 서비스를 사용하는가?
  - 사용자의 숨겨진 니즈가 있는가?
  - 실제 제품 사용하는 맥락이 우리의 생각과 동일한가?



## REFERENCES

- [서적] 그로스 해킹 (위키북스, 2021)