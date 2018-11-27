from threading import current_thread
from rx import Observable
from rx.concurrency import ThreadPoolScheduler

pool_scheduler = ThreadPoolScheduler(optimal_thread_count)
Observable.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon") \
    .map(lambda s: intense_calculation(s)) \
    .subscribe_on(pool_scheduler) \
    .subscribe(on_next=lambda s: print("PROCESS 1: {0} {1}".format(current_thread().name, s)),
               on_error=lambda e: print(e),
               on_completed=lambda: print("PROCESS 1 done!"))
