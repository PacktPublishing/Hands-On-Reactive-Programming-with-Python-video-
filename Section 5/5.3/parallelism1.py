import multiprocessing
import random
import time
from threading import current_thread

from rx import Observable
from rx.concurrency import ThreadPoolScheduler


def intense_calculation(value):
    # sleep for a random short duration between 0.5 to 2.0 seconds to simulate a long-running calculation
    time.sleep(random.randint(5, 20) * .1)
    return value

# calculate number of CPU's, then create a ThreadPoolScheduler with that number of threads
optimal_thread_count = multiprocessing.cpu_count() + 1
pool_scheduler = ThreadPoolScheduler(optimal_thread_count)


Observable.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon") \
    .flat_map(lambda s: Observable.just(s).subscribe_on(pool_scheduler).map(lambda s: intense_calculation(s))) \
    .subscribe(on_next=lambda s: print("PROCESS 1: {0} {1}".format(current_thread().name, s)),
               on_error=lambda e: print(e),
               on_completed=lambda: print("PROCESS 1 done!"))
