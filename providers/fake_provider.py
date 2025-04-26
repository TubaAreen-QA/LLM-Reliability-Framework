from __future__ import annotations

import json
from pathlib import Path

from framework.adapters.base_adapter import BaseAdapter
from framework.contracts.provider_config import ProviderConfig
from framework.contracts.provider_request import ProviderRequest
from framework.contracts.provider_response import ProviderResponse
from framework.http.provider_transport import ProviderTransport
from providers.abstract_sdk_provider import AbstractSDKProvider


class FakeTransport(ProviderTransport):
    """
    Transport used by the FakeProvider.

    Reads responses from a JSON file instead of calling
    an external API.
    """

    def __init__(
        self,
        data_file: str | Path,
    ) -> None:

        with open(
            data_file,
            encoding="utf-8",
        ) as fp:

            self._responses = json.load(fp)

    def execute(
        self,
        payload: dict,
    ) -> dict:

        prompt = payload["prompt"]

        return self._responses.get(
            prompt,
            {
                "answer": "Unknown prompt",
                "confidence": 0.0,
                "usage": {
                    "prompt_tokens": 0,
                    "completion_tokens": 0,
                    "total_tokens": 0,
                },
            },
        )


class FakeAdapter(BaseAdapter):

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

        return ProviderResponse(

            provider=provider,

            model=model,

            prompt=request.prompt,

            answer=raw_response.get(
                "answer",
                "",
            ),

            response_time_ms=round(
                latency_ms,
                3,
            ),

            token_usage={

                "prompt_tokens":
                    usage.get(
                        "prompt_tokens",
                        0,
                    ),

                "completion_tokens":
                    usage.get(
                        "completion_tokens",
                        0,
                    ),

                "total_tokens":
                    usage.get(
                        "total_tokens",
                        0,
                    ),

            },

            raw_response=raw_response,

            metadata={

                "confidence":

                    raw_response.get(
                        "confidence",
                        0.0,
                    )

            },

        )


class FakeProvider(AbstractSDKProvider):

    PROVIDER_NAME = "fake"

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        data_file = (

            Path(__file__).parent.parent

            / "data"

            / "fake_provider_responses.json"

        )

        super().__init__(

            config=config,

            transport=FakeTransport(
                data_file
            ),

            adapter=FakeAdapter(),

        )

    def build_payload(
        self,
        request: ProviderRequest,
    ) -> dict:

        return {

            "prompt": request.prompt

        }

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