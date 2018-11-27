from rx.testing import marbles

xs = rx.Observable.from_marbles('1-2-3-4-|')

ys = rx.Observable.from_marbles('-a-b-c-d-e|')

source = xs.combine_latest(ys, lambda x, y: x+y)

subscription = source.subscribe(
     lambda value: print("Next:", value),
     lambda error: print("Error:", error),
     lambda: print("Complete!"))
