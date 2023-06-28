def LCM(a,b):
    if a>b:
        larger = a
        samller = b
    elif b>a:
        larger = b
        samller = a
    i = larger
    while(True):
        if (i % samller == 0 ):
            print(i)
            break 
        else:
            i=i+larger
LCM(2,3)
LCM(5,7)