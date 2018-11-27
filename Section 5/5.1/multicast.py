res = source.multicast(observable)

res = source.multicast(subject_selector=lambda: Subject(), selector=lambda x: x)



res = source.publish()

res = source.publish(lambda x: x)



res = source.publish_value(42)

res = source.publish_value(42, lambda x: x.map(lambda y: y * y))



res = source.replay(buffer_size=3)

res = source.replay(buffer_size=3, window=500)

res = source.replay(None, 3, 500, scheduler)

res = source.replay(lambda x: x.take(6).repeat(), 3, 500, scheduler)
