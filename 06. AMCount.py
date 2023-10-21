def AMCount():
    with open('STORY.txt', 'r') as f:
        a = m = 0
        for char in f.read():
            if char.lower() == 'a':
                a += 1
            elif char.lower() == 'm':
                m += 1
    print('a occured',a,'times','and m occured',m,'times')
