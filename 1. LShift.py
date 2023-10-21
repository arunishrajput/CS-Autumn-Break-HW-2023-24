def LShift(Arr,n):
    shift = n % len(Arr)
    Shifted_List = Arr[shift:] + Arr[:shift]
    print(Shifted_List)