from __future__ import annotations

from anthropic import Anthropic

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.http.provider_transport import (
    ProviderTransport,
)


class ClaudeTransport(
    ProviderTransport,
):

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        self.client = Anthropic(
            api_key=config.api_key,
        )

        self.config = config

    def execute(
        self,
        payload: dict,
    ) -> dict:

        response = self.client.messages.create(
            **payload
        )

        return response.model_dump()