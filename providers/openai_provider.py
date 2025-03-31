from __future__ import annotations

import time

from openai import OpenAI

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


class OpenAIProvider(BaseProvider):

    @property
    def name(self) -> str:

        return "openai"

    def ask(
        self,
        request: ProviderRequest,
    ) -> ProviderResponse:

        client = OpenAI(
            api_key=self.config.api_key,
        )

        start = time.perf_counter()

        completion = client.chat.completions.create(

            model=self.config.model,

            messages=[
                {
                    "role": "user",
                    "content": request.prompt,
                }
            ],

            temperature=self.config.temperature,

            max_tokens=self.config.max_tokens,
        )

        elapsed = (
            time.perf_counter() - start
        ) * 1000

        answer = completion.choices[
            0
        ].message.content

        usage = completion.usage

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
                    usage.prompt_tokens,

                "completion_tokens":
                    usage.completion_tokens,

                "total_tokens":
                    usage.total_tokens,

            },

            raw_response=completion.model_dump(),

            metadata={},
        )

    def health_check(
        self,
    ) -> bool:

        return True

    def supported_models(
        self,
    ) -> list[str]:

        return [
            self.config.model
        ]