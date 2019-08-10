import os
import threading

from tqdm import tqdm

from tqdm_multithread import TqdmMultiThread


class TqdmMultiThreadFactory:
    def __init__(self):
        self.texts = {}
        self.lock = threading.Lock()

    def create(self, id, total):
        return TqdmMultiThread(self.texts, id, total, self.lock)
