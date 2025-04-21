from __future__ import annotations

import json
import time
from pathlib import Path

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)

from providers.base_provider import (
    BaseProvider,
)


    

class FakeProvider(BaseProvider):

    PROVIDER_NAME = "fake"

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        super().__init__(config)

        file = (

            Path(__file__).parent.parent

            / "data"

            / "fake_provider_responses.json"

        )

        with open(
            file,
            encoding="utf-8",
        ) as fp:

            self.responses = json.load(fp)

    @property
    def name(
        self,
    ) -> str:

        return "fake"

    def ask(
        self,
        request: ProviderRequest,
    ) -> ProviderResponse:

        start = time.perf_counter()

        response = self.responses.get(

            request.prompt,

            {

                "answer": "Unknown",

                "metadata": {},

            },

        )

        elapsed = (

            time.perf_counter()

            - start

        ) * 1000

        answer = response["answer"]

        prompt_tokens = len(
            request.prompt.split()
        )

        completion_tokens = len(
            answer.split()
        )

        return ProviderResponse(

            provider=self.name,

            model=self.config.model,

            prompt=request.prompt,

            answer=answer,

            response_time_ms=round(
                elapsed,
                3,
            ),

            token_usage={

                "prompt_tokens":
                    prompt_tokens,

                "completion_tokens":
                    completion_tokens,

                "total_tokens":
                    prompt_tokens
                    + completion_tokens,

            },

            raw_response=response,

            metadata=response.get(
                "metadata",
                {},
            ),

        )

    def health_check(
        self,
    ) -> bool:

        return True

    def supported_models(
        self,
    ) -> list[str]:

        return [

            self.config.model,

        ]