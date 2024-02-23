
def recursion(k):
    if k <= 0:
        result=0
        return result  
    else:
        result=k+recursion(k-1)
        return result
        
    
print("\n\nRecursion Example results -> ")
print(recursion(6))    