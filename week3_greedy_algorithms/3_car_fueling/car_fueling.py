from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    if tank >= distance:
        return 0
    if not stops or stops[0] > tank:
        return -1
    last_stop = 0
    while stops and stops[0] <= tank:
        last_stop = stops.pop(0)
    stops = [stop - last_stop for stop in stops]

    next_min_refills = min_refills(distance - last_stop, tank, stops)
    if next_min_refills == -1:
        return -1
    return 1 + next_min_refills


if __name__ == "__main__":
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
