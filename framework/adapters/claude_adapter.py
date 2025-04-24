from __future__ import annotations

from framework.adapters.base_adapter import (
    BaseAdapter,
)

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)


class ClaudeAdapter(BaseAdapter):

    def adapt(
        self,
        request: ProviderRequest,
        raw_response: dict,
        provider: str,
        model: str,
        latency_ms: float,
    ) -> ProviderResponse:

        usage = raw_response.get(
            "usage",
            {},
        )

        answer = ""

        content = raw_response.get(
            "content",
            [],
        )

        if content:

            answer = content[0].get(
                "text",
                "",
            )

        prompt_tokens = usage.get(
            "input_tokens",
            0,
        )

        completion_tokens = usage.get(
            "output_tokens",
            0,
        )

        return ProviderResponse(

            provider=provider,

            model=model,

            prompt=request.prompt,

            answer=answer,

            response_time_ms=round(
                latency_ms,
                3,
            ),

            token_usage={

                "prompt_tokens":
                    prompt_tokens,

                "completion_tokens":
                    completion_tokens,

                "total_tokens":

                    prompt_tokens

                    +

                    completion_tokens,

            },

            raw_response=raw_response,

            metadata={

                "stop_reason":

                    raw_response.get(
                        "stop_reason"
                    ),

            },

        )