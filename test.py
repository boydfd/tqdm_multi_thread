import threading
from concurrent.futures import ThreadPoolExecutor
import time

from tqdm_multithread_factory import TqdmMultiThreadFactory


def demo(factory, position, total):
    with factory.create(position, total) as progress:
        for _ in range(0, total, 5):
            progress.update(5)
            time.sleep(0.001 * (position % 5 + 1))


with ThreadPoolExecutor(max_workers=20) as executor:
    tasks = range(100)
    lock = threading.Lock()
    multi_thread_factory = TqdmMultiThreadFactory()
    for i, url in enumerate(tasks, 1):
        executor.submit(demo, multi_thread_factory, i, 100)
