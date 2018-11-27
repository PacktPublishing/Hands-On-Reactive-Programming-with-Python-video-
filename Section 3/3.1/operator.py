from rx import Observable

source = Observable.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

lengths = source.map(lambda s: len(s))

filtered = lengths.filter(lambda i: i >= 5)

filtered.subscribe(lambda value: print("Received {0}".format(value)))



# Chaining

from rx import Observable

Observable.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon") \
    .map(lambda s: len(s)) \
    .filter(lambda i: i >= 5) \
    .subscribe(lambda value: print("Received {0}".format(value)))
