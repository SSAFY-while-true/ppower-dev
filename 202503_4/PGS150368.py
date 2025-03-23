def solution(users, emoticons):
    from itertools import product
    
    discount_rates = [10, 20, 30, 40]
    perms = list(product(discount_rates, repeat=len(emoticons)))
    result_li = []
    
    for perm in perms:
        enroll = 0
        total_user_cost = 0
        """ 각 이모티콘에 할인율 적용 """
        temp_emoticons = emoticons.copy()

        for i in range(len(emoticons)):
            temp_emoticons[i] *= ((100 - perm[i]) / 100)
        
        for user in users:
            # user[0]: 임계 할인율
            # user[1]: 임계 비용
            user_cost = 0
            
            for i in range(len(emoticons)):
                if perm[i] >= user[0]:
                    user_cost += temp_emoticons[i]

            if user_cost >= user[1]:
                user_cost = 0
                enroll += 1
                
            total_user_cost += user_cost
        
        result_li.append([enroll, total_user_cost])
    
    result = max(result_li, key=lambda x: (x[0], x[1]))
    
    return result
