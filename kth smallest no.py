# kth-smallest-element
n,k=map(int,input().split())
i=list(map(int,input().split()))
i.sort()
print(i[k-1])
