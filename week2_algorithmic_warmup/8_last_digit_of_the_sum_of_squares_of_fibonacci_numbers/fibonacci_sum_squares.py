def fibonacci_sum_squares(n):
    if n <= 1:
        return n
    
    pairs = []

    previous = 0
    current  = 1
    
    pairs.append((previous, current))

    for _ in range(n):
        previous, current = current, (previous + current) % 10
        
        # identify if there's a loop
        if (previous, current) == (0, 1):
            return (pairs[(n - 1) % len(pairs)][1] * pairs[n % len(pairs)][1]) % 10
            
        pairs.append((previous, current))

    return (previous * current) % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
