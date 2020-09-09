# :call_me_hand: 수어번역기 : 또 하나의 언어

- 팀명 : S:With (B105)

- 팀원 소개

  팀장 : 박세훈(딥러닝)

  팀원 : 김낙현(딥러닝), 김재은(FE), 류혜명(FE), 안성호(BE)

- 역할

  - Tech Leader - 김낙현
  - QA - 김재은
  - 개발자 - 안성호, 박세훈
  - 기획자 - 류혜명

## 주제

- 프로젝트명 : 수어번역기 - 또 하나의 언어
- 수어(영상)를 텍스트로 번역
- 사진(글, 물체)을 수어로 번역



## 기술스택

- Frontend

  Vue.js, Vuetify

- Backend

  Django

- Machine Learning

  Python, TensorFlow, OpenCV, YOLO



## 기능

- 주요 기능

  - 수어 -> 글

    1. 수어 영상을 찍기(데이터 셋 한정) >> 번역 + 스피커(읽어주기) + 신고

  - 글 -> 수어

  1. 글씨를 수어로 변환

     1-1. 글씨 작성 >> 수어

     1-2. 사진(글씨 + 물체) 찍기 >> 수어

       

    2. (보류) 음성을 수어로 변환(음성 -> 글 -> 수어)

- 세부 기능

  - 웹에서 글씨 위로 마우스 올리면 글씨에 대한 수어 보여주기
  - 회원관리
  - 건의 게시판
  - 수어 자신이 만들어서 올리기

## :apple: 개발규칙 

#### 공통

- 특수문자는 _ 만 허용한다.
- ex) Is_Select(클래스), get_Value(함수), is_Select(변수)

#### 클래스명

- 클래스명은 대문자의 명사로 시작한다.
- ex) IsSelect

#### 함수명

- 소문자의 동사로 시작한다.
- ex) getValue

#### 변수명

- 소문자로 시작하며 여러 단어로 이루어진 경우 각 단어의 첫글자를 대문자로 한다.(카멜표기법)
- ex) isSelect




## :star: Git 규칙

**branch**

``` 
master -> develop -> feature/fe(김재은, 류혜명) or feature/be(안성호)
```

**merge**

``` 
merge 하기 전 서로 코드 리뷰하기
merge 후 branch 지우기
```

**commit**

```
1 day 1 commit
커밋 메시지는 => 이슈번호 /(Add/Updata/Delete) 작업 내용 <= 의 구조로 작성
ex) S123301 /Add Login
이슈번호가 없을경우 None 으로 대체
```



