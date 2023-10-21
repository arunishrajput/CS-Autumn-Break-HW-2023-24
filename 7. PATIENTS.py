import pickle

def countrec():
    count = 0
    with open ('PATIENTS.dat', 'rb') as f:
        try:
            while True:
                record = pickle.load(f)
                if record[2] == 'COVID-19':
                    print(record)
                    count += 1
        except EOFError:
            print('Total no. of COVID-19 patients:', count)