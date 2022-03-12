segments = list()
points = list()
m = []
for i in range(int(input())):
    segments.append([int(i) for i in input().split()])
def PointCover(segments, points):
    min_end = segments[0][1]
    for i in segments:
        if i[1] < min_end:
            min_end = i[1]
    points.append(min_end)
    for i in segments:
        if i[0] <= min_end <= i[1]:
            m.append(i)
    for i in m:
        segments.remove(i)
    m.clear()
    if len(segments) > 0:
        PointCover(segments, points)
PointCover(segments, points)
print(len(points))
for i in points:
    print(i, end=' ')