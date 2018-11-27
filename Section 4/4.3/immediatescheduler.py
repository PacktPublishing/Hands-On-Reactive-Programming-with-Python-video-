def test():
    rx.Observable.from_iterable([1,2,3], scheduler=rx.concurrency.immediate_scheduler) \
        .subscribe(lambda x : print(x))
    print("after subscribe")

rx.Observable.range(0, 3, scheduler=rx.concurrency.immediate_scheduler) \
    .do_action(lambda _ : test()) \
    .subscribe()
