import argparse
import threading
from queue import LifoQueue, PriorityQueue, Queue
from random import randint
from time import sleep
from random import choice, randint


#define
QUEUE_TYPES = {
    "fifo": Queue,
    "lifo": LifoQueue,
    "heap": PriorityQueue
}

#define arguement
def main(args):
    buffer = QUEUE_TYPES[args.queue]()

#define parse
def parse_args():
    parser = argparse.ArgumentParser()
    #producers_3
    parser.add_argument("-q", "--queue", choices=QUEUE_TYPES, default="fifo")
    #consumer_2
    parser.add_argument("-p", "--producers", type=int, default=3)
    #producer_speed_1
    parser.add_argument("-ps", "--producer-speed", type=int, default=1)
    #consumer_speed_1
    parser.add_argument("-cs", "--consumer-speed", type=int, default=1)
    return parser.parse_args()

#arguement
if __name__ == "__main__":
    try:
        main(parse_args())
    except KeyboardInterrupt:
        pass

#define the products

PRODUCTS = (
    ":balloon:",
    ":cookie:",
    ":crystal_ball:",
    ":diving_mask:",
    ":flashlight:",
    ":gem:",
    ":gift:",
    ":kite:",
    ":party_popper:",
    ":postal_horn:",
    ":ribbon:",
    ":rocket:",
    ":teddy_bear:",
    ":thread:",
    ":yo-yo:",
)

#Priority Queue

@dataclass(order=True)
class Product:
    priority: int
    label: str = field(compare=False)

    def __str__(self):
        return self.label

class Priority(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

PRIORITIZED_PRODUCTS = (
    Product(Priority.HIGH, ":1st_place_medal:"),
    Product(Priority.MEDIUM, ":2nd_place_medal:"),
    Product(Priority.LOW, ":3rd_place_medal:"),
)

#effects
class Worker(threading.Thread):
    def __init__(self, speed, buffer):
        super().__init__(daemon=True)
        self.speed = speed
        self.buffer = buffer
        self.product = None
        self.working = False
        self.progress = 0
    
    @property
    def state(self):
        if self.working:
            return f"{self.product} ({self.progress}%)"
        return ":zzz: Idle"

    def simulate_idle(self):
        self.product = None
        self.working = False
        self.progress = 0
        sleep(randint(1, 3))

    def simulate_work(self):
        self.working = True
        self.progress = 0
        delay = randint(1, 1 + 15 // self.speed)
        for _ in range(100):
            sleep(delay / 100)
            self.progress += 1

#queue producer
class Producer(Worker):
    def __init__(self, speed, buffer, products):
        super().__init__(speed, buffer)
        self.products = products

    def run(self):
        while True:
            self.product = choice(self.products)
            self.simulate_work()
            self.buffer.put(self.product)
            self.simulate_idle()

#queue consemer
class Consumer(Worker):
    def run(self):
        while True:
            self.product = self.buffer.get()
            self.simulate_work()
            self.buffer.task_done()
            self.simulate_idle()

#thread
class Worker(threading.Thread):
      
        @property
        def state(self):
            if self.working:
                return f"{self.product} ({self.progress}%)"
                return ":zzz: Idle"

        def simulate_idle(self):
           self.product = None
           self.working = False
           self.progress = 0
           sleep(randint(1, 3))
           
        def simulate_work(self):
            self.working = True
            self.progress = 0
            delay = randint(1, 1 + 15 // self.speed)
            for _ in range(100):
                sleep(delay / 100)
                self.progress += 1