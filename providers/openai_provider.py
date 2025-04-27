from __future__ import annotations

from framework.adapters.openai_adapter import (
    OpenAIAdapter,
)

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.http.openai_transport import (
    OpenAITransport,
)

from providers.abstract_sdk_provider import (
    AbstractSDKProvider,
)


class OpenAIProvider(AbstractSDKProvider):
    """
    OpenAI implementation.

    Responsibilities:

    - Build OpenAI payload
    - Delegate execution to OpenAITransport
    - Delegate parsing to OpenAIAdapter

    Everything else is inherited from
    AbstractSDKProvider.
    """

    PROVIDER_NAME = "openai"

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        super().__init__(
            config=config,
            transport=OpenAITransport(config),
            adapter=OpenAIAdapter(),
        )

    def build_payload(
        self,
        request: ProviderRequest,
    ) -> dict:

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

        metadata = getattr(
            request,
            "metadata",
            None,
        )

        if metadata:

            if "top_p" in metadata:

                payload["top_p"] = metadata["top_p"]

            if "frequency_penalty" in metadata:

                payload["frequency_penalty"] = (

                    metadata["frequency_penalty"]

                )

            if "presence_penalty" in metadata:

                payload["presence_penalty"] = (

                    metadata["presence_penalty"]

                )

            if "stop" in metadata:

                payload["stop"] = metadata["stop"]

        return payload

    def health_check(
        self,
    ) -> bool:

        try:

            self.transport.execute(

                {

                    "model": self.config.model,

                    "messages": [

                        {

                            "role": "user",

                            "content": "ping",

                        }

                    ],

                    "max_tokens": 1,

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