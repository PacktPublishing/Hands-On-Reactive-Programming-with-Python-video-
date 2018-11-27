from rx import Observable

obs1 = Observable.from_([1,2,3])
obs2 = Observable.from_([10,11,12])

Observable.merge(obs1, obs2)\
           .subscribe(lambda s:print(s))
