from __future__ import annotations

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)

from framework.parsers.base_parser import (
    BaseParser,
)


class ClaudeParser(BaseParser):

    def parse(
        self,
        request: ProviderRequest,
        raw_response: dict,
        provider: str,
        model: str,
        latency_ms: float,
    ) -> ProviderResponse:

        usage = raw_response["usage"]

        return ProviderResponse(

            provider=provider,

            model=model,

            prompt=request.prompt,

            answer=raw_response[
                "content"
            ][0][
                "text"
            ],

            response_time_ms=round(
                latency_ms,
                3,
            ),

            token_usage={

                "prompt_tokens":
                    usage["input_tokens"],

                "completion_tokens":
                    usage["output_tokens"],

                "total_tokens":
                    usage["input_tokens"]
                    + usage["output_tokens"],

            },

            raw_response=raw_response,

            metadata={},
        )