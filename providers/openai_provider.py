from __future__ import annotations

import time

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)

from framework.http.openai_transport import (
    OpenAITransport,
)

from providers.base_provider import (
    BaseProvider,
)


class OpenAIProvider(
    BaseProvider
):

    def __init__(
        self,
        config,
    ):

        super().__init__(config)

        self.transport = (

            OpenAITransport(config)

        )

    @property
    def name(
        self,
    ):

        return "openai"

    def ask(
        self,
        request: ProviderRequest,
    ) -> ProviderResponse:

        payload = {

            "model": self.config.model,

            "messages": [

                {

                    "role": "user",

                    "content": request.prompt,

                }

            ],

            "temperature":
                self.config.temperature,

            "max_tokens":
                self.config.max_tokens,

        }

        start = time.perf_counter()

        raw = self.transport.execute(
            payload
        )

        elapsed = (

            time.perf_counter()

            - start

        ) * 1000

        return ProviderResponse(

            provider=self.name,

            model=self.config.model,

            prompt=request.prompt,

            answer=raw["choices"][0]["message"]["content"],

            response_time_ms=round(
                elapsed,
                3,
            ),

            token_usage=raw["usage"],

            raw_response=raw,

            metadata={},
        )

    def health_check(
        self,
    ):

        return True

    def supported_models(
        self,
    ):

        return [

            self.config.model

        ]