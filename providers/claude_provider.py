from __future__ import annotations

from framework.adapters.claude_adapter import (
    ClaudeAdapter,
)

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.http.claude_transport import (
    ClaudeTransport,
)

from providers.abstract_sdk_provider import (
    AbstractSDKProvider,
)


class ClaudeProvider(AbstractSDKProvider):
    """
    Anthropic Claude Provider.

    Responsibilities

    • Build Claude request payload
    • Delegate execution to ClaudeTransport
    • Delegate parsing to ClaudeAdapter

    Everything else is handled by
    AbstractSDKProvider.
    """

    PROVIDER_NAME = "claude"

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        super().__init__(
            config=config,
            transport=ClaudeTransport(config),
            adapter=ClaudeAdapter(),
        )

    def build_payload(
        self,
        request: ProviderRequest,
    ) -> dict:

        payload = {

            "model":
                self.config.model,

            "messages": [

                {

                    "role": "user",

                    "content": request.prompt,

                }

            ],

            "max_tokens":
                self.config.max_tokens,

            "temperature":
                self.config.temperature,

        }

        metadata = getattr(
            request,
            "metadata",
            None,
        )

        if metadata:

            if "system" in metadata:

                payload["system"] = metadata["system"]

            if "stop_sequences" in metadata:

                payload["stop_sequences"] = (

                    metadata["stop_sequences"]

                )

        return payload

    def health_check(
        self,
    ) -> bool:

        try:

            self.transport.execute(

                {

                    "model":
                        self.config.model,

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