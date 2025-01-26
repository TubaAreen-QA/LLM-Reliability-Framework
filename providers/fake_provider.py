import json
import time
from pathlib import Path

from providers.base_provider import BaseProvider

from framework.models.provider_request import provider_request
from framework.models.provider_response import provider_Response


class FakeProvider(BaseProvider):

    def __init__(self):

        file = (
            Path(__file__).parent.parent
            / "data"
            / "fake_provider_responses.json"
        )

        with open(file, encoding="utf-8") as f:
            self.responses = json.load(f)

    def ask(
        self,
        request: provider_request
    ) -> provider_Response:

        start = time.perf_counter()

        data = self.responses.get(
            request.prompt,
            {
                "answer": "Unknown",
                "provider_confidence": 0.0
            }
        )

        elapsed = (
            time.perf_counter() - start
        ) * 1000

        answer = data["answer"]

        confidence = data["provider_confidence"]

        token_usage = {
            "prompt_tokens": len(request.prompt.split()),
            "completion_tokens": len(answer.split()),
            "total_tokens":
                len(request.prompt.split())
                + len(answer.split())
        }

        return provider_Response(
            provider=request.provider,
            model=request.model,
            prompt=request.prompt,
            answer=answer,
            response_time_ms=round(elapsed, 2),
            token_usage=token_usage,
            raw_response=data,
            provider_confidence=confidence
        )