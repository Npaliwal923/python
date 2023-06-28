def HCF(a,b):
    if a>b:
        L = a
        S = b
    else:
        L = b
        S = a
    while(True):
        r = L%S
        if r==0:
            break
        else:
            L=S
            S=r
    print("HCF is ", S)

HCF(54,24)