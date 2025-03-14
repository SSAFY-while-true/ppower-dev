def solution(players, m, k):
    answer = 0
    servers = []
    for player in players:
        now_server = sum(x[0] for x in servers)
        if player >= (now_server + 1) * m:
            needed_server = player // m - now_server
            servers.append((needed_server, k))
            answer += needed_server
            
        new_servers = []
        for server in servers:
            new_server = (server[0], server[1] - 1)
            if new_server[1] > 0:
                new_servers.append(new_server)
        
        servers = new_servers
    
    return answer
