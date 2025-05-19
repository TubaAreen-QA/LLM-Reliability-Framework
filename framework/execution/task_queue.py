from __future__ import annotations

from collections import deque

from framework.contracts.evaluation_task import (
    EvaluationTask,
)


class TaskQueue:

    def __init__(self):

        self._queue = deque()

    def put(
        self,
        task: EvaluationTask,
    ) -> None:

        self._queue.append(
            task
        )

    def get(
        self,
    ) -> EvaluationTask:

        return self._queue.popleft()

    def empty(
        self,
    ) -> bool:

        return len(
            self._queue
        ) == 0

    def size(
        self,
    ) -> int:

        return len(
            self._queue
        )