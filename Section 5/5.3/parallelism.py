from rx import Observable

scheduler = ThreadPoolScheduler()

xs = Observable.range(1, 5).flat_map(lambda x: Observable.just(x, scheduler=scheduler), mapper)
