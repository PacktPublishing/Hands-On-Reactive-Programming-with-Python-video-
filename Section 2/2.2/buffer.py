

/*code example of buufer operator*/
import rx
>>> from rx.core import Scheduler
>>> ryg = ['red', 'yellow', 'green']
>>> cbp = ['cyan', 'blue', 'purple']
>>> xs = rx.Observable.timer(10, 20).take(3).map(lambda i: ryg[i])
>>> ys = rx.Observable.timer(40, 30).take(3).map(lambda i: cbp[i])

/*here bufferoperator is used*/
>>> source = xs.concat(ys) \'=
...     .buffer_with_time_or_count(timespan=40,
...                                count=2,
...                                scheduler=Scheduler.timeout)
>>> subscription = source.subscribe(
...     lambda value: print("Next:", value),
...     lambda error: print("Error:", error),
...     lambda: print("Complete!")
Next: ['red', 'yellow']
Next: ['green']
Next: ['cyan', 'blue']
Next: ['purple']
Complete!