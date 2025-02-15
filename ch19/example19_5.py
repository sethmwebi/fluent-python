import asyncio
import itertools
import time
from threading import Thread, Event

async def spin(msg: str) -> None:
    for char in itertools.cycle(r'\|/-'):
        status = f'\r{char} {msg}'
        print(status, flush=True, end='')
        try:
            await asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    blanks = ' ' * len(status) # type: ignore
    print(f'\r{blanks}\r', end='')

def slow() -> int:
    time.sleep(3)
    return 42

def main() -> None:
    result = supervisor()
    print(f'Answer: {result}')

def supervisor() -> int:
    done = Event()
    spinner = Thread(target=spin, args=('thinking!', done))
    print('spinner object:', {spinner})
    spinner.start()
    result = slow()
    done.set()
    spinner.join()
    return result

if __name__ == "__main__":
    main()
