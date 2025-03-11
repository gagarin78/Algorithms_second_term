def fractional_knapsack(n, W, p, w):
    items = [(p[i] / w[i], p[i], w[i]) for i in range(n)]

    items.sort(reverse=True, key=lambda x: x[0])

    total_value = 0.0

    for cost_per_weight, price, weight in items:
        if W >= weight:
            total_value += price
            W -= weight
        else:
            total_value += W * cost_per_weight
            break

    return total_value

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        n, W = map(int, f.readline().split())
        p = []
        w = []
        for _ in range(n):
            pi, wi = map(int, f.readline().split())
            p.append(pi)
            w.append(wi)

    result = fractional_knapsack(n, W, p, w)

    with open('output.txt', 'w') as f:
        f.write(f"{result:.4f}")