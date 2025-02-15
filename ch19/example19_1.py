import itertools
import time
# from threading import Thread, Event
from multiprocessing import Process, Event, synchronize

def spin(msg: str, done: synchronize.Event) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, end='', flush=True)
        if done.wait(.1):
            break
    blanks = ' ' * len(status) # type: ignore
    print(f'\r{blanks}\r', end="")

def slow() -> int:
    time.sleep(3)
    return 42

# def supervisor() -> int:
#     done = Event()
#     spinner = Thread(target=spin, args=('thinking!', done))
#     print(f'spinner object: {spinner}')
#     spinner.start()
#     result = slow()
#     done.set()
#     spinner.join()
#     return result
def supervisor() -> int:
    done = Event()
    spinner = Process(target=spin, args=('thinking!', done))
    print(f'spinner object: {spinner}')
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

if __name__ == '__main__':
    main()
