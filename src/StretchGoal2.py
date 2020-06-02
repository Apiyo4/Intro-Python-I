"""Multiples of 3 or 5
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
"""
def solution(number):
    arr = []
    mults = []
    for i in range(0, number):
        arr.append(i)
    for i in arr:
        if i%3==0 and i%5==0:
            mults.append(i)
        elif i%3 == 0 and i%5!=0:
            mults.append(i)
        elif i%5 == 0 and i%3!=0:
            mults.append(i)
    ans = f2(*mults)
    print(ans)

def f2(*args):
    sum =0
    for i in args:
        sum += i
    return sum
    
solution(1000)