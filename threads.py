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