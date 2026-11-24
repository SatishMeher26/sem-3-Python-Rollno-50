
import gc
import sys
import time
import weakref
import tracemalloc


# Node class
class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

    def __del__(self):
        print(self.name, "destroyed")


# 1. Reference Counting
def exp1():
    print("\n1. REFERENCE COUNTING")

    a = Node("A")
    b = a

    print("Reference count:", sys.getrefcount(a))

    del a
    print("After deleting a:", sys.getrefcount(b))

    del b


# 2. Reference Cycle and Manual Collection
def exp2():
    print("\n2. REFERENCE CYCLE")

    gc.disable()

    x, y = Node("X"), Node("Y")
    x.other = y
    y.other = x

    del x, y

    print("Manual collection:", gc.collect())
    gc.enable()


# 3. Thresholds, Counts and Statistics
def exp3():
    print("\n3. GC THRESHOLDS AND STATISTICS")

    print("Threshold:", gc.get_threshold())
    print("Count:", gc.get_count())
    print("Statistics:", gc.get_stats())


# 4. Automatic Collection
def exp4():
    print("\n4. AUTOMATIC COLLECTION")

    events = []

    def callback(phase, info):
        if phase == "stop":
            events.append(info["generation"])

    gc.callbacks.append(callback)

    old = gc.get_threshold()
    gc.set_threshold(50, 5, 5)

    for i in range(100):
        a, b = [], []
        a.append(b)
        b.append(a)

    gc.set_threshold(*old)
    gc.callbacks.remove(callback)

    print("Automatic collections:", len(events))


# 5. Generations
def exp5():
    print("\n5. GENERATIONS")

    gc.collect()

    keeper = [Node("K")]
    keeper[0].other = keeper

    for i in range(3):
        gc.collect(i)
        print("Generation", i, "objects:",
              len(gc.get_objects(i)))

    keeper[0].other = None
    del keeper


# 6. Memory Measurement
def exp6():
    print("\n6. MEMORY MEASUREMENT")

    gc.collect()
    gc.disable()
    tracemalloc.start()

    for i in range(1000):
        a, b = {}, {}
        a["b"] = b
        b["a"] = a

    print("Memory before collection:",
          tracemalloc.get_traced_memory()[0] // 1024, "KB")

    print("Objects collected:", gc.collect())

    print("Memory after collection:",
          tracemalloc.get_traced_memory()[0] // 1024, "KB")

    tracemalloc.stop()
    gc.enable()


# 7. DEBUG_SAVEALL
def exp7():
    print("\n7. DEBUG SAVEALL")

    gc.collect()
    gc.set_debug(gc.DEBUG_SAVEALL)

    a, b = [], []
    a.append(b)
    b.append(a)

    del a, b
    gc.collect()

    print("Garbage objects:", len(gc.garbage))

    gc.set_debug(0)
    gc.garbage.clear()
    gc.collect()


# 8. Tracking and Weak References
def exp8():
    print("\n8. TRACKING AND WEAK REFERENCES")

    samples = [5, "hello", [1, 2], {}, (1, 2)]

    for obj in samples:
        print(obj, "Tracked:", gc.is_tracked(obj))

    n = Node("W")
    ref = weakref.ref(n)

    print("Weak reference alive:", ref() is not None)

    del n

    print("After deletion:", ref() is not None)


# 9. Freeze and Unfreeze
def exp9():
    print("\n9. FREEZE AND UNFREEZE")

    gc.collect()

    print("Before freeze:", gc.get_freeze_count())

    gc.freeze()

    print("After freeze:", gc.get_freeze_count())

    gc.unfreeze()

    print("After unfreeze:", gc.get_freeze_count())


# 10. Garbage Collection Timing
def exp10():
    print("\n10. GC TIMING")

    def work():
        data = []
        for i in range(100000):
            data.append([i])

    for status in [True, False]:

        gc.collect()

        if status:
            gc.enable()
            name = "GC Enabled"
        else:
            gc.disable()
            name = "GC Disabled"

        start = time.perf_counter()
        work()
        elapsed = time.perf_counter() - start

        print(name, ":", round(elapsed * 1000, 2), "ms")

    gc.enable()


# MAIN PROGRAM
if __name__ == "__main__":

    print("PYTHON VERSION:", sys.version)

    exp1()
    exp2()
    exp3()
    exp4()
    exp5()
    exp6()
    exp7()
    exp8()
    exp9()
    exp10()

    print("\nALL EXPERIMENTS COMPLETED!")
