def optimal_summands(n):
    summands = []
    # write your code here
    next_int = 0

    while n > 0:
        next_int = next_int + 1
        if next_int + (next_int + 1) > n:
            summands.append(n)
            break
        summands.append(next_int)
        n = n - next_int

    return summands


if __name__ == "__main__":
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
