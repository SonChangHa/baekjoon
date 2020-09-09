import sys
def put():
    return list(map(int, input().split()))
input = sys.stdin.readline

n1,k1,n2,k2 = put()

print(n1*k1 + n2*k2)
