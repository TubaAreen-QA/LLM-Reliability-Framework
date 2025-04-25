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


class GeminiAdapter(BaseAdapter):

    def adapt(
        self,
        request: ProviderRequest,
        raw_response: dict,
        provider: str,
        model: str,
        latency_ms: float,
    ) -> ProviderResponse:

        candidates = raw_response.get(
            "candidates",
            [],
        )

        answer = ""

        if candidates:

            parts = candidates[0][
                "content"
            ][
                "parts"
            ]

            answer = "".join(

                part.get(
                    "text",
                    "",
                )

                for part

                in parts

            )

        usage = raw_response.get(
            "usageMetadata",
            {},
        )

        prompt_tokens = usage.get(
            "promptTokenCount",
            0,
        )

        completion_tokens = usage.get(
            "candidatesTokenCount",
            0,
        )

        total_tokens = usage.get(
            "totalTokenCount",
            prompt_tokens
            + completion_tokens,
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
                    total_tokens,

            },

            raw_response=raw_response,

            metadata={

                "finish_reason":

                    candidates[0].get(
                        "finishReason"
                    )

                    if candidates

                    else None,

            },

        )