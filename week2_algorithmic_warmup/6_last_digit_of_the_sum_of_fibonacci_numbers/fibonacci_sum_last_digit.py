def fibonacci_sum(n):
    # F 0 1 1 2 3  5  8 13 21 34 55 89
    # G 0 1 2 4 7 12 20 33 54 88
    # G[3] = 4 = 5 - 1 = F[5] - 1
    # G[4] = 7 = 8 - 1 = F[6] - 1 
    # G[n] = F[n + 2] - 1
    
    if n <= 1:
        return n
    
    pairs = []

    previous = 0
    current  = 1
    
    pairs.append((previous, current))

    for _ in range(n + 1):
        previous, current = current, (previous + current) % 10
        
        # identify if there's a loop
        if (previous, current) == (0, 1):
            return (pairs[(n + 1) % len(pairs)][1] - 1) % 10
            
        pairs.append((previous, current))

    return (current - 1) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
