### 입력받은 문자열에서 단어의 개수를 세는 문제
# 단어의 조건
# - ce, je, ne, me, te, se, le, la, de, que, si 로 시작
# - 띄어쓰기나 -를 단위로 단어 구분
# - 단어가 모음(a,e,i,o,u,h)으로 시작하는 경우, 앞 단어의 마지막 모음이 사라지고 '으로 대체된다.

start_word = ['ce', 'je', 'ne', 'me', 'te', 'se', 'le', 'la', 'de', 'que', 'si']
france = input()
flist = france.split(' ', '-')

'''
[풀이 설명]
- c\*, j\* 의 형식으로 원소를 구성해야 함
- split() 함수의 구분자를 여러 개 지정하려면 리스트의 형태를 넘겨주어야 함
- Counter 객체 사용
- maxsplit=1 : 최대 한 번만 분할 => ' 가 2번 이상 나와도 한 번을 기준으로만 split
'''