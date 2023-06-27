
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    print( total)


numbers =list(map(int,input("enter a number:").split()))
sum(numbers)



