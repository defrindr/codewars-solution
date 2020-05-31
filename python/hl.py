# higher and lower
# 


def high_and_low(num):
    a = list(map(int,num.split(" ")))
    a.sort()
    print "{} {}".format(a[len(a)-1],a[0])

high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")