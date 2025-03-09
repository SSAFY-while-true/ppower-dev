def find_max_val_sum(items: list, max_weight: int) -> int:
    dp = [0] * (max_weight + 1)
    
    for weight, val in items:
        for i in range(max_weight, weight - 1, -1):
             dp[i] = max(dp[i], dp[i - weight] + val)
    
    return dp[max_weight]
    
    
if __name__ == '__main__':
    item_num, max_weight = map(int, input().split())
    items = []
    for _ in range(item_num):
        items.append(tuple(map(int, input().split())))      # (무게, 가치)
    print(find_max_val_sum(items, max_weight)) 
