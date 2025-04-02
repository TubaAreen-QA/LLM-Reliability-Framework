from __future__ import annotations

from typing import Any

from openai import OpenAI

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.http.provider_transport import (
    ProviderTransport,
)


class OpenAITransport(
    ProviderTransport
):

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        self.client = OpenAI(
            api_key=config.api_key,
            base_url=config.base_url,
        )

        self.config = config

    def execute(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:

        response = (

            self.client.chat.completions.create(

                **payload

            )

        )

        return response.model_dump()