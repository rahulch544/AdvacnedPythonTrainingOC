import threading
import time

class box(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self) # calling parent class constructor
        self.name=name
    def run(self):
        for v in range(5):
            time.sleep(1)
        print("This is {} thread".format(self.name))
        
obj1=box("Thread-1")
obj2=box("Thread-2")
obj1.start()
obj2.start()

# obj1.join()
# obj2.join()
# for v in range(5):
#     time.sleep(1)
print("Exit from mainThread")