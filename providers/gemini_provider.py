from __future__ import annotations

from framework.adapters.gemini_adapter import (
    GeminiAdapter,
)

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.http.gemini_transport import (
    GeminiTransport,
)

from providers.abstract_sdk_provider import (
    AbstractSDKProvider,
)


class GeminiProvider(AbstractSDKProvider):
    """
    Google Gemini Provider.

    Responsibilities

    • Build Gemini payload
    • Delegate request execution to GeminiTransport
    • Delegate response conversion to GeminiAdapter

    Timing, retries, ProviderResponse creation,
    token accounting and latency measurement
    are inherited from AbstractSDKProvider.
    """

    PROVIDER_NAME = "gemini"

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        super().__init__(
            config=config,
            transport=GeminiTransport(config),
            adapter=GeminiAdapter(),
        )

    def build_payload(
        self,
        request: ProviderRequest,
    ) -> dict:

        payload = {

            "contents": [

                {

                    "parts": [

                        {

                            "text": request.prompt

                        }

                    ]

                }

            ],

            "generationConfig": {

                "temperature":
                    self.config.temperature,

                "maxOutputTokens":
                    self.config.max_tokens,

            },

        }

        metadata = getattr(
            request,
            "metadata",
            None,
        )

        if metadata:

            generation = payload[
                "generationConfig"
            ]

            if "top_p" in metadata:

                generation["topP"] = metadata["top_p"]

            if "top_k" in metadata:

                generation["topK"] = metadata["top_k"]

            if "stop_sequences" in metadata:

                generation["stopSequences"] = (

                    metadata["stop_sequences"]

                )

        return payload

    def health_check(
        self,
    ) -> bool:

        try:

            self.transport.execute(

                {

                    "contents": [

                        {

                            "parts": [

                                {

                                    "text": "ping"

                                }

                            ]

                        }

                    ],

                    "generationConfig": {

                        "maxOutputTokens": 1

                    },

                }

            )

            return True

        except Exception:

            return False

    def supported_models(
        self,
    ) -> list[str]:

        return [

            self.config.model,

        ]