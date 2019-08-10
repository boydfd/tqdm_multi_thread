import io
import sys

from tqdm import tqdm


class TqdmMultiThread(io.StringIO):
    def __init__(self, texts, id, total=100, lock=None):
        super().__init__()
        self.id = id
        self.lock = lock
        text = "progress #{}".format(id)
        with self.lock:
            self.texts = texts
            self.texts[id] = ''
            self.down()
        self.tqdm = tqdm(
            total=total,
            position=id,
            desc=text,
            file=self
        )

    def update(self, *params):
        self.tqdm.update(*params)

    def write(self, buf):
        self.with_lock_call(self._write, buf)

    def _write(self, buf):
        buf = self.strip(buf)
        if buf:
            self.texts[self.id] = buf

    @classmethod
    def strip(cls, buf):
        return buf.strip('\r\n\t\x1b[1A')

    def flush(self):
        self.with_lock_call(self._flush)

    def _flush(self):
        self.top()

        for key in sorted(self.texts):
            sys.stdout.write(self.texts[key])
            self.down()

    def up(self):
        self.print('\x1b[1A')

    def down(self):
        self.print('\n')

    def with_lock_call(self, func, *params):
        if self.lock:
            with self.lock:
                func(*params)
        else:
            func(*params)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.tqdm.close()
        with self.lock:
            self.top()
            self.print(self.texts[self.id])
            self.bottom()
            del self.texts[self.id]

    def print(self, text):
        sys.stdout.write(text)
        sys.stdout.flush()

    def bottom(self):
        for i in range(self.get_length()):
            self.down()

    def top(self):
        for i in range(self.get_length()):
            self.up()

    def get_length(self):
        return len(self.texts)
