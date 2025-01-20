from collections import deque
import time
import threading


class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)


def place_order(arr):
    for i in range(len(arr)):
        print(f"Placing order {i+1}.{arr[i]}")
        food_order.enqueue(arr[i])
        time.sleep(0.5)


def serve_order():
    time.sleep(1)
    while True:
        if food_order.is_empty():
            break
        order = food_order.dequeue()
        print(f"Serving {order}")
        time.sleep(2)


if __name__ == "__main__":
    orders = ["pizza", "samosa", "pasta", "biryani", "burger"]
    food_order = Queue()

    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("All orders served.")
