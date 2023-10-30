def Sum3(L):
    sum = 0
    for i in L:
        if i%10 == 3:
            sum += i
    print ('Sum of integers ending with digit 3 =', sum)