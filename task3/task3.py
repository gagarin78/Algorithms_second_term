def max_revenue(n, a, b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    total = sum(ai * bi for ai, bi in zip(a, b))

    return total

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        n = int(f.readline().strip())
        a = list(map(int, f.readline().strip().split()))
        b = list(map(int, f.readline().strip().split()))

    result = max_revenue(n, a, b)

    with open('output.txt', 'w') as f:
        f.write(str(result))