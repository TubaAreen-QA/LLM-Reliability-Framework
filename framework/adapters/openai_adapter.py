from __future__ import annotations

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)

from framework.adapters.base_adapter import (
    BaseAdapter,
)


class OpenAIAdapter(BaseAdapter):

    def adapt(
        self,
        request,
        raw,
        provider,
        model,
        latency_ms,
    ) -> ProviderResponse:

        usage = raw["usage"]

        return ProviderResponse(

            provider=provider,

            model=model,

            prompt=request.prompt,

            answer=raw["choices"][0]["message"]["content"],

            response_time_ms=round(
                latency_ms,
                3,
            ),

            token_usage={

                "prompt_tokens":
                    usage["prompt_tokens"],

                "completion_tokens":
                    usage["completion_tokens"],

                "total_tokens":
                    usage["total_tokens"],

            },

            raw_response=raw,

            metadata={

                "finish_reason":

                    raw["choices"][0]["finish_reason"]

            },

        )