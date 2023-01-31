---
layout: single
title: "Github Blog 제작 일지"
category: "Others"
tag: [blog]
author_profile: false
sidebar:
  nav: "docs"
---

### HANA-LOG 만드는 과정 기록

<img src="https://raw.githubusercontent.com/hanalog/hanalog.github.io/gh-pages/images/2022-03-28-blogsetting/hanalog_logo_sunrise.png" alt="hanalog_logo_sunrise" style="zoom:80%;" />

#### 1일차(2022-03-28)
- 블로그 생성
- 카테고리 및 태그 페이지 추가
- 카테고리 구상
- 검색 기능 추가 : 작성한 포스팅이 검색 결과에 나타나는 걸 원치 않는 경우에는 해당 포스팅의 search: false 로 지정
- 블로그 타이틀 지정

#### 2일차(2022-03-29)
- 로고 제작 및 추가
- 간단한 자기소개 키워드
- 깃허브 링크 연동

#### 3일차(2022-04-04)

- typora를 통한 이미지 자동 업로드 설정 완료!!!
  - 이미지 자동 업로드를 위해 typora를 구입했는데 계속 진행되지 않아서 며칠 동안 애를 먹었다. 
  - 원래는 typora에 사진을 드래그 시 "사용자 정의 폴더로 이미지 복사"를 통해서 깃허브와 연동된 데스크탑 폴더에 업로드 후 push를 통해서 업로드를 진행했는데 깃허브에는 잘 적용되어도 깃허브 블로그에는 반영되지 않아서 계속 끙끙거렸다. 하지만 오히려 더 좋은 방법을 찾았다.
  - 해결방법 : typora 환경설정 > 이미지 > 이미지 삽입 시 "이미지를 업로드"  설정 > 이미지 업로더는  "PicGo-Core" 설정 > Download > Open Config File 클릭 > Config 파일 수정(repo/token/path/branch 등)
  - 자세한 해결방법은 해당 [블로그 링크](https://donggod.tistory.com/139)에서 자세하게 참고할 수 있다.
  - 위 해결방법을 통해서 이미지 자동 업로드가 해결되었을 뿐만 아니라 로컬 저장소에 저장하지 않아도 된다는 장점이 있다. 물론 나는 저장 레포지토리가 데스크탑과 연동되어있어서 어차피 다시 데스크탑에 저장되지만 로컬 저장소에 저장하고 싶지 않은 분은 데스크탑과 연동되지 않은 이미지 레포지토리를 하나 생성해서 해당 레포지토리에 연결해도 좋을 것 같다.
  - 어쨌든 해당 사항을 해결하여 마음이 한결 가벼워졌다. 이제 편리하게 블로그 업로드를 할 수 있다!

#### 꿀팁
- ctrl+R : 블로그 코드 수정 후 사이트에서 반영 여부 확인 시 새로고침

[참고메뉴얼](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)  
[참고영상](https://www.youtube.com/playlist?list=PLIMb_GuNnFwfQBZQwD-vCZENL5YLDZekr)
