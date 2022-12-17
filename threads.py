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