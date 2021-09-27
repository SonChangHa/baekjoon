import heapq
import sys


def put():
    return list(map(int, input().split()))


input = sys.stdin.readline


heap = []


for i in range(int(input())):
    t = int(input())
    if t != 0:
        heapq.heappush(heap, t)
    else:
        if not heap:
            print("0")
        else:
            print(heapq.heappop(heap))