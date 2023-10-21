import pickle
def CreateFile():
    with open('Book.dat', 'ab') as f:
        BookNo = int(input('Enter book number: '))
        Book_Name = input('Enter book name: ')
        Author = input('Enter author name: ')
        Price = int(input('Enter price: '))
        record = [BookNo, Book_Name, Author, Price]
        pickle.dump(record, f)
        print('Record saved!')

import pickle
def CountRec(Author):
    with open('Book.dat', 'rb') as f:
        count = 0
        try:
            while True:
                record = pickle.load(f)
                if record[2] == Author:
                    count += 1
        except EOFError:
            return count