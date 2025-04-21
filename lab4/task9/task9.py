def solve():
    with open('lab4/task9/input.txt', 'r') as f:
        s = f.read().strip()
    
    n = len(s)
    if n == 0:
        with open('lab4/task9/output.txt', 'w') as f:
            f.write("")
        return
    
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    parent = [(-1, -1, "")] * (n + 1)
    
    for i in range(1, n + 1):
        candidate_len = dp[i-1] + 1
        if candidate_len < dp[i]:
            dp[i] = candidate_len
            parent[i] = (i-1, 1, s[i-1])
        
        for l in range(1, i // 2 + 1):
            if i - l < 0:
                continue
            substring = s[i-l:i]
            max_repeats = 1
            j = i - l
            while j - l >= 0 and s[j-l:j] == substring:
                j -= l
                max_repeats += 1
            total_length = i - j
            if total_length == l * max_repeats:
                encoded_part = substring
                if max_repeats > 1:
                    encoded_part += "*" + str(max_repeats)
                candidate_len = dp[j] + len(encoded_part)
                if candidate_len < dp[i]:
                    dp[i] = candidate_len
                    parent[i] = (j, max_repeats, substring)
    
    parts = []
    i = n
    while i > 0:
        start, cnt, substr = parent[i]
        if cnt == 1:
            parts.append(substr)
        else:
            parts.append(f"{substr}*{cnt}")
        i = start
    parts.reverse()
    result = '+'.join(parts)
    
    with open('lab4/task9/output.txt', 'w') as f:
        f.write(result)

solve()