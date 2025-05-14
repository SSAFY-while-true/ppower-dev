num_word, num_alpha = map(int, input().split())
words = [input().strip() for _ in range(num_word)]

# 단어를 비트마스크로 변환
word_bits = []
for word in words:
    bit = 0
    for alpha in word:
        bit |= (1 << (ord(alpha) - ord('a')))
    word_bits.append(bit)

# num_alpha 개의 알파벳을 배울 때, 읽을 수 있는 word의 최대 갯수 계산
max_count = 0

# 기본적으로 모든 단어에 들어가는 'a', 'n', 't', 'i', 'c'는 반드시 알아야 함
if num_alpha < 5:
    print(0)  # 5개 미만이면 어떤 단어도 읽을 수 없음
    exit()

# 'a', 'n', 't', 'i', 'c'에 해당하는 비트 마스크
essential = 0
for c in 'antic':
    essential |= (1 << (ord(c) - ord('a')))

# 백트래킹으로 최적의 알파벳 조합 찾기
def backtrack(idx, k, learned):
    global max_count
    
    # num_alpha개의 글자를 모두 배웠으면 읽을 수 있는 단어 수 계산
    if k == num_alpha:
        count = 0
        for word_bit in word_bits:
            if (word_bit & learned) == word_bit:  # 모든 알파벳을 배웠는지 확인
                count += 1
        max_count = max(max_count, count)
        return
    
    # 더 이상 배울 알파벳이 없으면 종료
    if idx == 26:
        return
        
    # 현재 알파벳이 이미 필수 알파벳에 포함되어 있다면 스킵
    if (essential & (1 << idx)) != 0:
        backtrack(idx + 1, k, learned)
    else:
        # 현재 알파벳을 배우는 경우
        backtrack(idx + 1, k + 1, learned | (1 << idx))
        
        # 현재 알파벳을 배우지 않는 경우
        backtrack(idx + 1, k, learned)

# 필수 알파벳으로 시작
backtrack(0, 5, essential)

print(max_count)

