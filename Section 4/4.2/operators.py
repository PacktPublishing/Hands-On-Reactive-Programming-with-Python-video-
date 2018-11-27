import csv
from rx import Observable

def mapper(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        return Observable.from_(reader)

Observable.from_(["filename.csv"]).map(mapper).concat_all().subscribe(print)



def to_file(filename):
    f = open(filename)
    return Observable.using(
        lambda: Disposable(lambda: f.close()),
        lambda d: Observable.just(f)
    )

def to_reader(f):
    return csv.reader(f)

def print_rows(reader):
    for row in reader:
        print(row)

Observable.from_(["filename.csv", "filename2.csv"]).flat_map(to_file).map(to_reader).subscribe(print_rows)
