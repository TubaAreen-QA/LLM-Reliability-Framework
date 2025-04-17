from __future__ import annotations

from framework.adapters.base_adapter import (
    BaseAdapter,
)

from framework.contracts.normalized_response import (
    NormalizedResponse,
)


class OpenAIAdapter(BaseAdapter):

    def normalize(
        self,
        raw_response: dict,
    ) -> NormalizedResponse:

        usage = raw_response["usage"]

        return NormalizedResponse(

            answer=raw_response[
                "choices"
            ][0][
                "message"
            ][
                "content"
            ],

            prompt_tokens=usage[
                "prompt_tokens"
            ],

            completion_tokens=usage[
                "completion_tokens"
            ],

            total_tokens=usage[
                "total_tokens"
            ],

            finish_reason=raw_response[
                "choices"
            ][0][
                "finish_reason"
            ],

            model=raw_response.get(
                "model"
            ),
        )