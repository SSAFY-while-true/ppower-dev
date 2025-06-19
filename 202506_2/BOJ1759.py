# BOJ1759: 암호 만들기
password_len, char_num = map(int, input().split())
chars = sorted(input().split())
vowels = ['a', 'e', 'i', 'o', 'u']
outputs = []


def backtrack(current_password:list, start_idx:int, vowel_count:int, consonant_count:int):
    # 종료 조건
    if len(current_password) == password_len:
        if vowel_count >= 1 and consonant_count >= 2:
            new_password = ''.join(current_password)
            outputs.append(new_password)
        return
    
    # 재귀 호출
    for i in range(start_idx, char_num):
        # Choose
        char = chars[i]
        current_password.append(char)
        
        if char in vowels:
            new_vowel_count = vowel_count + 1
            new_consonant_count = consonant_count
        else:
            new_vowel_count = vowel_count
            new_consonant_count = consonant_count + 1
        
        # Explore
        backtrack(current_password, i + 1, new_vowel_count, new_consonant_count)

        # Unchoose
        current_password.pop()
    

backtrack([], 0, 0, 0)
for output in outputs:
    print(output)