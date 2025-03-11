def min_refills(d, m, stops):
    stops = [0] + stops + [d]
    n = len(stops)

    current_position = 0
    refills = 0

    for i in range(1, n):
        if stops[i] - stops[current_position] > m:
            if i == current_position + 1:
                return -1
            refills += 1
            current_position = i - 1

    if stops[-1] - stops[current_position] > m:
        return -1

    return refills

if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        d = int(f.readline().strip())
        m = int(f.readline().strip())
        n = int(f.readline().strip())
        stops = list(map(int, f.readline().strip().split()))

    result = min_refills(d, m, stops)

    with open('output.txt', 'w') as f:
        f.write(str(result))