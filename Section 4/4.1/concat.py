from rx import Observable

observable = Observable.from_([1, 2])
other_observable = Observable.from_([3, 4])
Observable.concat(observable, other_observable) \
  .subscribe(on_next=lambda n: print(n))


# O/P
# (1, 'LITE Industrial', 'Southwest', '729 Ravine Way', 'Irving', 'TX', 75014)
# (3, 'Re-Barre Construction', 'Southwest', '9043 Windy Dr', 'Irving', 'TX', 75032)
# (5, 'Marsh Lane Metal Works', 'Southeast', '9143 Marsh Ln', 'Avondale', 'LA', 79782)
