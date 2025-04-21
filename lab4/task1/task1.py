def find_substring_occurrences(p, t):
    n = len(t)
    m = len(p)
    occurrences = []

    for i in range(n - m + 1):
        if t[i:i+m] == p:
            occurrences.append(i + 1)

    return len(occurrences), occurrences

with open('input.txt', 'r') as f:
    p = f.readline().strip()
    t = f.readline().strip()

count, positions = find_substring_occurrences(p, t)

with open('output.txt', 'w') as f:
    f.write(f"{count}\n")
    f.write(" ".join(map(str, positions)) + "\n")
