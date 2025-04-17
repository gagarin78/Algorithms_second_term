def compute_z_function(s):
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def main():
    with open('lab4/taskZ/input.txt', 'r') as f:
        s = f.read().strip()
    z = compute_z_function(s)
    with open('lab4/taskZ/output.txt', 'w') as f:
        f.write(' '.join(map(str, z[1:])))

if __name__ == '__main__':
    main()