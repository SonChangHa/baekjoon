import sys
import heapq
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline


heap = []

for i in range(int(input())):
    value = int(input())
    if value != 0:
        heapq.heappush(heap, -value)
    else:
        if not heap:
            print("0")
        else:
            print(-heapq.heappop(heap))
