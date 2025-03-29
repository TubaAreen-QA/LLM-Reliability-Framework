from __future__ import annotations

import time


class RetryPolicy:

    def __init__(
        self,
        retries: int,
        delay: float = 1.0,
    ) -> None:

        self.retries = retries
        self.delay = delay

    def execute(
        self,
        operation,
    ):

        attempt = 0

        while True:

            try:

                return operation()

            except Exception:

                attempt += 1

                if attempt > self.retries:
                    raise

                time.sleep(
                    self.delay
                )