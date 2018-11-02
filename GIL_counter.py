import threading
import sys
import time

numSecondsToRun = 2

class CounterThread(threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
      self._counter = 0
      self._endTime = time.time() + numSecondsToRun

   def run(self):
      # Simulate a computation on the CPU
      while(time.time() < self._endTime):
         self._counter += 1

if __name__ == "__main__":
   if len(sys.argv) < 2:
      print("Usage:  python counter 5")
      sys.exit(5)

   numThreads = int(sys.argv[1])
   print("Spawning %i counting threads for %i seconds..." % (numThreads, numSecondsToRun))

   threads = []
   for i in range(0,numThreads):
      t = CounterThread()
      t.start()
      threads.append(t)

   totalCounted = 0
   for t in threads:
      t.join()
      totalCounted += t._counter
   print("Total amount counted was {:.2f} millions".format(totalCounted/1e6))
   print("Average count per thread {:.2f} millions".format(totalCounted/1e6/numThreads))
