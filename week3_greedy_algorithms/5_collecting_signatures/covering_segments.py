from sys import stdin
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    points = []

    # write your code here
    while len(segments) > 0:
        min_end = min([segment.end for segment in segments])
        points.append(min_end)

        segments_new = []
        for segment in segments:
            is_to_remove = segment.start <= min_end <= segment.end
            if not is_to_remove:
                segments_new.append(segment)
        segments = segments_new

    return points


if __name__ == "__main__":
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
