# html 2일차 

## CSS

---

- CSS 기본 사용법

  h1{font-size:14px;}

- CSS Selector

  ```
  #sect1 > ul > li:nth-child(1)
    # : id 선택 (문서 1개만 !!)
    li:nth-child(1) : li 중에 첫번째
  ```

  1. 기초 선택자

  2. 고급 선택자

     CSS 상속 : 상속을 통해 부모 요소릐 속성을 모두 자식에게 상속한다.

     - 상속 되는것 : text 관련 요소
     - 상속 되지 않는것 : Box 관련 요소, position 관련요소

  3. 의사클래스 (시험 비중 x)

- CSS 적용 우선순위

  CSS 우선순위를 아래와 같이 그룹을 지어 볼 수 있다.

  - 중요도

  - 우선순위

    인라인 / id 선택자 / class 선택자 / 요소 선택자

  - 소스 선언 순서

  ```
  Quiz
  . : class
  # : id
  (요소선택자 < class < id)
  answer
  1 = green (요소선택자)
  2 = blue ()
  3 = skyblue (정의된 순서가 밑에 있을 수록)
  4 = skyblue
  6 = (important 적용)
  7 = 
  ```

### 기초  CSS

1. 크기 단위

   ```
   em vs rem
   기본 px : 16 px
   em : 배수 (1.5em = 상속 받은 px * 1.5 = 36px)
   rem : root em (1.5rem = 기본 * 1.5 = 24px)
   ```

2. CSS 문서표현

   - 텍스트

     변형서체 (<b>, <i>  사용 안함 !!)

     (강조는 <strong>, <em> --> 기울기등 나머지는 css활용)

### Box model

1. margin, padding
2. border

### display 속성

1. display: block

   - 줄 바꿈이 일어나는 요소

2. display: inline

   - 줄 바꿈이 일어나지 않는 행의 일부 요소
   - width, height, margin 속성 적용 안됨 !!

3. display: inline-block

   - Block과 inline 레벨 요소의 특징을 모두 갖는다.

   - Block 처럼 width, height, margin 속성을 모두 지정할 수 있다.