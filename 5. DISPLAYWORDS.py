def DISPLAYWORDS():
    with open('STORY.txt', 'r') as f:
        line = f.readline()

        while line:
            words = line.split()
            for word in words:
                if len(word) < 4:
                    print(word)
            line = f.readline()