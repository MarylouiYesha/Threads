import argparse
from queue import LifoQueue, PriorityQueue, Queue

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