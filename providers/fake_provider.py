from framework.models.provider_request import ProviderRequest
from framework.models.provider_response import ProviderResponse


class FakeProvider:

    RESPONSES = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "Who wrote Hamlet?": "William Shakespeare",
        "What color is the sky?": "Blue"
    }

    def ask(self, request: ProviderRequest) -> ProviderResponse:

        answer = self.RESPONSES.get(request.prompt, "Unknown")

        return ProviderResponse(
            provider=request.provider,
            model=request.model,
            prompt=request.prompt,
            answer=answer,
            response_time_ms=120,
            token_usage={
                "input": 10,
                "output": 5,
                "total": 15
            },
            raw_response={}
        )