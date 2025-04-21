def solution(h1, m1, s1, h2, m2, s2):
    count = 0
    minute_count, hour_count = 0, 0
    
    # 시간을 초단위로 변경
    time1 = h1 * 3600 + m1 * 60 + s1
    time2 = h2 * 3600 + m2 * 60 + s2
    
    # 시작 시간이 정각일 때는 모든 침이 겹침
    if time1 == 0 or time1 == 60 * 60 * 12:
        count += 1
    
    
    # 1초 단위로 매 회 체크
    # 현재와 1초 후를 비교해 침이 추월했으면 카운트 증가
    for i in range(time1, time2):
        # 현재 침의 각도 계산
        current_second_angle = (i * 6) % 360
        current_minute_angle = (i * 0.1) % 360
        current_hour_angle = (i * 0.0083) % 360
        next_second_angle = ((i + 1) * 6) % 360
        next_minute_angle = ((i + 1) * 0.1) % 360
        next_hour_angle = ((i + 1) * 0.0083) % 360
        
        if current_second_angle < current_hour_angle and next_second_angle >= next_hour_angle:
            hour_count += 1
        
        if current_second_angle < current_minute_angle and next_second_angle >= next_minute_angle:
            minute_count += 1
        
        if next_second_angle == next_minute_angle == next_hour_angle:
            count -= 1
    
    count += minute_count + hour_count
    return count