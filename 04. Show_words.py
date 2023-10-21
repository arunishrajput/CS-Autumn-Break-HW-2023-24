def Show_words():
    with open('NOTES.txt', 'r') as f:
        line = f.readline()

        while line:
            if len(line.split()) == 5:
                print(line[:-1])
            line = f.readline()