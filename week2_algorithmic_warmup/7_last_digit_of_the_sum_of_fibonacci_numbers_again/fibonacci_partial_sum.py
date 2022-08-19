def fibonacci_partial_sum(from_, to):
    def fibonacci_sum(n):
        # function from the previous exercise
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

    if from_ == 0:
        return fibonacci_sum(to)
    return (fibonacci_sum(to) - fibonacci_sum(from_ - 1)) % 10


if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
