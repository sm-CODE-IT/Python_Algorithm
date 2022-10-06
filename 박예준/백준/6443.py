### sol1. itertools 라이브러리 이용 - 메모리 초과로 실패
from itertools import permutations  # 순열, 조합을 사용하기 위한 패키지

n = int(input())
for i in range(n):
    word = input()
    word_list = list(word)
    # word_anagram = [''.join(i) for i in list(combinations(word_list, repeat=len(word)))]
    word_anagram = [''.join(i) for i in list(permutations(word_list, len(word)))]
    for ana in word_anagram:
        print(ana)



### sol2. 백 트래킹 이용
def solution(str_len, anagram_str):
    if str_len == 0:
        visited.add(anagram_str)
        return

    for i in range(26):    # 모든 알파벳에 대해 순회한다.
        if alpha[i] >= 1:
            alpha[i] -= 1
            solution(str_len-1, anagram_str+chr(i+97))   # 재귀방식으로 문자열 더해나가기
            alpha[i] += 1



n2 = int(input())
for i in range(n2):
    visited = set()   # 각 알파벳의 개수가 0이 되는 순간 방문했음을 의미
    alpha = [0 for _ in range(26)]
    word = input()

    for i in word:
        alpha[ord(i)-97] += 1
    solution(len(word), '')    # 입력받은 문자열의 길이와 빈 문자열을 인자로 넘겨준다.
    for s in sorted(list(visited)):
        print(s)