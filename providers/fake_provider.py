import json
import time
from pathlib import Path

from providers.base_provider import BaseProvider

from framework.models.provider_request import provider_request
from framework.models.provider_response import provider_Response
from __future__ import annotations

class FakeProvider(BaseProvider):

    def __init__(self) -> None:

        self._responses = self._load()

    @property
    def name(self) -> str:

        return "fake"

    def ask(
        self,
        request: provider_request
    ) -> provider_Response:

        start = time.perf_counter()

        response = self._responses.get(
            request.prompt,
            {
                "answer": "Unknown",
                "metadata": {}
            }
        )

        elapsed = (
            time.perf_counter() - start
        ) * 1000

        answer = response["answer"]

        prompt_tokens = len(
            request.prompt.split()
        )

        completion_tokens = len(
            answer.split()
        )

        return provider_Response(
            provider=self.name,
            model=request.model,
            prompt=request.prompt,
            answer=answer,
            response_time_ms=round(elapsed, 3),
            token_usage={
                "prompt_tokens": prompt_tokens,
                "completion_tokens": completion_tokens,
                "total_tokens": (
                    prompt_tokens +
                    completion_tokens
                )
            },
            raw_response=response,
            metadata=response.get(
                "metadata",
                {}
            )
        )

    def health_check(self) -> bool:

        return True

    def supported_models(self) -> list[str]:

        return [
            "fake-gpt"
        ]

    @staticmethod
    def _load() -> dict:

        file = (
            Path(__file__).parent.parent
            / "data"
            / "fake_provider_responses.json"
        )

        with open(
            file,
            encoding="utf-8"
        ) as fp:

            return json.load(fp)