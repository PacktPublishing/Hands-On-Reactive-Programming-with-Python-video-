from rx import Observable, Observer

def get_strings(observer):
   observer.on_next("Ram")
   observer.on_next("Mohan")
   observer.on_next("Shyam")
      observer.on_completed()

class PrintObserver(Observer):
   def on_next(self, value):
      print("Received {0}".format(value))
   def on_completed(self):
   print("Finished")
   def on_error(self, error):
      print("Error: {0}".format(error))

source = Observable.create(get_strings)
source.subscribe(PrintObserver())
