'''
Date: 2026-03-13 00:05:18
'''
from threading import Thread
from multiprocessing import Process, cpu_count
import time
import os


class InputReader(Thread):
    def run(self):
        self.line_of_text = input("Enter a line of text: ")


class MuchCPU(Process):
    def run(self):
        print(f"the process pid: {os.getpid()} is running")
        for i in range(200000000):
            pass


def thread_example():
    print("Enter some text and press enter: ")
    thread = InputReader()
    thread.start()
    count = result = 1
    while thread.is_alive():
        result = count*2
        count += 1
    print(f"calculated squares up to {count} * {count} = {result}")
    print(f"while you typed '{thread.line_of_text}'")


def process_example():
    start = time.time()
    procs = [MuchCPU() for _ in range(cpu_count())]
    print(f"the core count is {cpu_count()}")
    for p in procs:
        p.start()
    for p in procs:
        p.join()
    end = time.time()
    print(f"Process example took {end-start} seconds")

def conflict_example():
    print("This is a simple conflict example.")

if __name__ == "__main__":
    # thread_example()
    process_example()
    conflict_example()