from rx import Observable
from csv import DictReader

file_stream = Observable.from_(DictReader(open('datafile.csv', 'r')))




file_stream = Observable.from_(DictReader(open('datafile.csv', 'r'))).map(lambda line: line.strip()) \
    .filter(lambda line: line != '') \
    .buffer_with_count(4)
