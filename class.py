"""
COUNTER has a natural value, 0 at start time.
it can be either incremented or decremented by 1 at a time
Decrementing a null counter has no concequences

step 1)
Define the corrosponding python class
step 2)
test with:
create a counter, print it
increment it 10 times
decrement it 10 times

Some counters may have a maximum value, given at 
Creation time For much counters, 
incrementing them when they are at their maximum value
sets counter back to zero
Decrement when min (0) -----> to its max 
(=> "cycdic" counter)


"""

class Counter:
    def __init__ (self):
        self.value = 0

    def increment(self):
        self.value += 1

    def decrement(self):
        if self.value > 0:
            self.value -= 1

counter = Counter()


print(counter.value)

for _ in range(10):
    counter.increment()

print(counter.value)  


for _ in range(10):
    counter.decrement()

print(counter.value)