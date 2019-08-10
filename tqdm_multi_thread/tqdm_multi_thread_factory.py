import threading

from tqdm_multi_thread import TqdmMultiThread


class TqdmMultiThreadFactory:
    def __init__(self):
        self.texts = {}
        self.lock = threading.Lock()

    def create(self, id, total):
        return TqdmMultiThread(self.texts, id, total, self.lock)
