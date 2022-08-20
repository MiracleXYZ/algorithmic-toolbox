from sys import stdin


def optimal_value(capacity, weights, values):
    # write your code here
    if capacity == 0 or len(weights) == 0:
        return 0

    prices = [value / weight for value, weight in zip(values, weights)]
    m = prices.index(max(prices))
    amount = min(weights[m], capacity)
    value = prices[m] * amount
    del weights[m]
    del values[m]

    return value + optimal_value(capacity - amount, weights, values)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
