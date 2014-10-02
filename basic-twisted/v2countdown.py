
class Countdown(object):

    def __init__(self, counters):
        self.counter = 5
        self.counters = counters
        self.counters.append(self)

    def count(self):
        if self.counter == 0:
            self.counters.remove(self)
            if len(self.counters) == 0:
                reactor.stop()
            del self
        else:
            print self.counter, '...'
            self.counter -= 1
            reactor.callLater(1, self.count)

from twisted.internet import reactor

counters = []

_ = [Countdown(counters) for i in range(0, 3)]

for i in counters:
    reactor.callWhenRunning(i.count)

print 'Start!'
reactor.run()
print 'Stop!'