import sys
sys.setrecursionlimit(100000)
    
     
def ackermann_function(m, n,memo):
    if m < 0 or n < 0:
        return "Від'ємне число"
    if not (m, n) in memo:
        if m == 0:
            res = n + 1
        if m>0 and n==0:
            res = ackermann_function(m-1,1,memo)
        if m>0 and n>0:
            res = ackermann_function(m-1,ackermann_function(m,n-1,memo),memo)
        memo[(m, n)] = res
    return memo[(m, n)]
     

memo = {}
print(str(ackermann_function(3,7,memo)))