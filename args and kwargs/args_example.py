def maxima(firstarg,*args):
    print("First argument :",firstarg)
    for arg in args:
        print("Next Argument from *args :",arg)

maxima('Hello','Welcome','to Coding Maxima','Platform')

def add(*numbers):
    sum = 0
    for number in numbers:
        sum+=number
    print("Sum :",sum)

add(55,10)
add(234,100,150,20)
add(1,2,3,4,5,6,7,8,9,10)

