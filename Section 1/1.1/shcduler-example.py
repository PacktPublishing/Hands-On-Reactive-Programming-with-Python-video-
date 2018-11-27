import time
import threading
import rx
from rx.concurrency.scheduler import Scheduler

tm1=time.time()
lock=threading.Lock()

def log(s):
  tm2=time.time()
  with lock:
    print '%ds: %s on %s' % (round(tm2-tm1), s, threading.currentThread().name)

def work(x):
  log('processing '+str(x))
  time.sleep(1)

def finish(x):
  log('finished '+str(x))

log('started')

rx.Observable.range(1, 3) \
  # observe on method for on which thread to observe
  .observe_on(Scheduler.timeout) \
  .do_action(work) \
  .subscribe(finish)

log('finished ALL')
time.sleep(5) # wait to complete
