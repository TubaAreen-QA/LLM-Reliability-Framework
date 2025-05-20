from __future__ import annotations

from framework.engine.evaluation_engine import (
    EvaluationEngine,
)

from framework.execution.task_queue import (
    TaskQueue,
)


class EvaluationExecutor:
    """
    Sequential executor.

    Future versions can replace the execution
    strategy with threads, asyncio or
    distributed workers without changing
    BenchmarkSuiteRunner.
    """

    def execute(
        self,
        queue: TaskQueue,
    ):

        results = []

        while not queue.empty():

            task = queue.get()

            engine = EvaluationEngine(

                provider_name=task.provider,

                validator_names=[],

                provider_file="providers.yaml",

                profile_name=task.profile,

                profile_file="profiles.yaml",

            )

            result = engine.evaluate(

                request=task.prompt,

                expected=task.expected,

            )

            results.append(
                result
            )

        return results