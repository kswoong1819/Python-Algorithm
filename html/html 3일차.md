# html 3일차

## 레이아웃과 고급 CSS 기능

### 다단 레이아웃

#### position

1. static (기본 값)

2. relative (상대 위치)

3. absolute (절대 위치)
   - 기준 : 부모(조상 요소)중에 static이 아닌것을 기준 !!
   - 본인의 위치를 지우고 이동.

4. fixed (절대 위치)

#### Float

- 일반적인 흐름에서 벗어나도록 하는 속성 중 하나

  - 반그시 clear (clear: both) 속성을 통해 초기화가 필요!!

- float를 사용하는 경우 block 사용을 뜻하며, display 값이 ~~~

- float 초보자들은 쓰지마라

  -- 문제점

  1. 부모요소 높이를 가지지 못한다

  -- 해결방안

  1. 의사(가상) 요소 선택자

- float-left, float-right 만 존재 mid 존재하지 않음

#### Layout

- tag 선택자만 활용하여 설명

- HTML/CSS 의 기본 특징
  1. 위에서 부터 아래로 순차적으로 나열
  2. display 속성을 통해 요소가 보이도록
  3. position 속성을 통해 위치 자체를 변경 (absolut 주의)
  4. float 속성을 통해 떠있도록 만듬

