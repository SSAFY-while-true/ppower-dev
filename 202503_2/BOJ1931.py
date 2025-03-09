def find_max_possible_meetings(meetings: list):
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0 
    last_end_time = 0

    for start, end in meetings:
        if start >= last_end_time:
            count += 1
            last_end_time = end
    
    return count

if __name__ == '__main__':
    meeting_num = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(meeting_num)]
    
    print(find_max_possible_meetings(meetings))
