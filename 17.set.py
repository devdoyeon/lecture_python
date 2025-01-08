"""
set
파이썬의 자료형 종류
시퀀스 타입 (sequence type): 저장된 값의 순서 정보가 있고, 중복된 값을 허용한다. ex) list, tuple, range, str
매핑 타입 (mapping type): 순서 정보가 포함되는 것이 본질은 아니나, 파이썬 3.7 이상부터는 dict 도 순서 정보를 유지한다.
셋 타입 (set type): 저장된 값의 순서 정보가 없고, 중복된 값을 허용하지 않는다. 수학의 집합과 비슷하다. ex) set, frozenset

특징
서로 다른 해시 가능 객체의 순서 없는 컬렉션
일반적인 용도는 멤버십 검사, 시퀀스에서 중복 제거와 교집합, 합집합, 차집합, 대칭 차집합과 같은 수학 연산을 계산하는 것
집합은 x in set, len(set), for x in set 을 지원
집합은 인덱싱, 슬라이싱 또는 기타 시퀀스와 유사한 동작을 지원하지 않는다.
두 가지 내장형: set은 mutable 객체이고, frozenset은 immutable 객체이다
내용을 add() 나 remove() 와 같은 메서드를 사용하여 변경할 수 있다.
딕셔너리 키 또는 다른 집합의 원소로 사용할 수 없다.
frozenset 형은 불변이고 해시 가능
만들어진 후에는 내용을 바꿀 수 없다. 따라서 딕셔너리 키 또는 다른 집합의 원소로 사용할 수 있다.

add(elem) : 원소 elem 을 집합에 추가한다.
remove(elem) :원소 elem 을 집합에서 제거한다. elem 가 집합에 포함되어 있지 않으면 KeyError 를 일으킨다.
discard(elem) : 원소 elem 이 집합에 포함되어 있으면 제거한다.
pop() : 집합으로부터 임의의 원소를 제거해 돌려준다. 집합이 비어있는 경우 KeyError 를 일으킨다.
clear() : 집합의 모든 원소를 제거한다.

1. 합집합(|): 두 집합의 전체 요소들의 모음.
2. 교집합(&): 두 집합의 공통 요소들의 모음.
3. 차집합(-): 왼쪽 집합의 요소에서 오른쪽 집합의 요소를 제거
4. 대칭 차집합(^): 합집합 - 교집합
5. 부분집합(<=): 왼쪽집합이 오른쪽집합의 부분집합인지의 여부를 조사.
6. 진성 부분집합(<): 부분집합이면서 추가로 요소가 더 존재하는지를 확인.
"""

set_1 = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6}
print(type(set_1), set_1)  # <class 'set'> {1, 2, 3, 4, 5, 6}

set_1.add(7)  # 집합에 요소를 추가
print(type(set_1), set_1)  # <class 'set'> {1, 2, 3, 4, 5, 6, 7}

set_1.update({8, 9})  # 업데이트
print(type(set_1), set_1)  # <class 'set'> {1, 2, 3, 4, 5, 6, 7, 8, 9 }

set_1.pop()  # 첫 요소 제거
print(type(set_1), set_1)  # <class 'set'> {2, 3, 4, 5, 6, 7, 8, 9}

set_1.remove(9)  # 요소 제거
print(type(set_1), set_1)  # <class 'set'> {2, 3, 4, 5, 6, 7, 8}

set_1.discard(4)  # 요소 제거
print(type(set_1), set_1)  # <class 'set'> {2, 3, 5, 6, 7, 8}

set_1.discard(9)  # discard는 없는 요소를 제거해도 에러가 나지 않는다.
print(type(set_1), set_1)  # <class 'set'> {2, 3, 5, 6, 7, 8}

# 집합 (합집합, 교집합, 차집합, 대칭차집합)
aa = {1, 2, 3, 4, 5}
bb = {5, 6, 7, 8, 9}

print(type(aa), type(bb))  # <class 'set'> <class 'set'>

# 합집합
print(aa | bb)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(aa.union(bb))  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 교집합
print(aa & bb)  # {5}
print(aa.intersection(bb))  # {5}

# 차집합
print(aa - bb)  # {1, 2, 3, 4}
print(aa.difference(bb))  # {1, 2, 3, 4}

# 대칭 차집합
# 둘 중 한 집합에 속하지만 둘 모두에 속하지 않는 것
# 합집합 - 교집합
print(aa ^ bb)  # {1, 2, 3, 4, 6, 7, 8, 9}
print(aa.symmetric_difference(bb))  # {1, 2, 3, 4, 6, 7, 8, 9}
