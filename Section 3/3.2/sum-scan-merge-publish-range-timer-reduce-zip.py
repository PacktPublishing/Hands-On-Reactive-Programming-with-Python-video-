from rx import Observable
from random import randint
from functional import seq

result = seq(1,2,3).map(lambda x: x*2).filter(lambda x: x > 4).reduce(lambda x, y: x + y)

print ("Result: {}".format(result))






print('Find the sum of items in a data stream')
Observable.from_([1,2,3,4,5])\
           .sum()\
           .subscribe(lambda s: print(s))






Observable.from_([1,2,3,4,5])\
          .scan(lambda subtotal, i: subtotal+i)\
          .subscribe(lambda x: print(x))






obs1 = Observable.from_([1,2,3])
obs2 = Observable.from_([10,11,12])

Observable.merge(obs1, obs2)\
           .subscribe(lambda s:print(s))





three_emissions = Observable.range(1, 3)

three_random_ints = three_emissions.map(lambda i: randint(1, 100000))






three_random_ints = three_emissions.map(lambda i: randint(1, 100000)).publish().auto_connect(2)




res = Observable.timer(5000, scheduler=Scheduler.timeout)






letters = Observable.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon")

intervals = Observable.interval(1000)

Observable.zip(letters, intervals, lambda s, i: (s, i)) \
    .subscribe(lambda t: print(t))
