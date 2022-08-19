def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n
    
    pairs = []

    previous = 0
    current  = 1
    
    pairs.append((previous, current))

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
        
        # identify if there's a loop
        if (previous, current) == (0, 1):
            return pairs[(n - 1) % len(pairs)][1]
            
        pairs.append((previous, current))

    return current


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))
