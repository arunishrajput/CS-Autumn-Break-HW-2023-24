import pickle
def countrec():
    with open ('STUDENT.dat', 'rb') as f:
        count = 0
        try:
            while True:
                record = pickle.load(f)
                if record[2] > 75:
                    print(record)
                    count += 1
        except EOFError:
            print('number of students scoring above 75%:',count)