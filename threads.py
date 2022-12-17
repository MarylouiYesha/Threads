import argparse
import threading
from queue import LifoQueue, PriorityQueue, Queue
from random import randint
from time import sleep


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

#effects
class Worker(threading.Thread):
    def __init__(self, speed, buffer):
        super().__init__(daemon=True)
        self.speed = speed
        self.buffer = buffer
        self.product = None
        self.working = False
        self.progress = 0

#thread
class Worker(threading.Thread):