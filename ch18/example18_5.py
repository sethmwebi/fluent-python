import contextlib
import sys

@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write # type: ignore
    yield 'JABBERWOCKY'
    sys.stdout.write = original_write
