from __future__ import annotations

import time

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)

from framework.http.openai_transport import (
    OpenAITransport,
)

from providers.base_provider import (
    BaseProvider,
)
from providers.abstract_sdk_provider import (
    AbstractSDKProvider,
)


class OpenAIProvider(
    AbstractSDKProvider
):

    def __init__(
        self,
        config,
    ):

        super().__init__(config)

        self.transport = (

            OpenAITransport(config)

        )

    @property
    def name(
        self,
    ):

        return "openai"

    def build_payload(
        self,
        request,
    ):

        return {

            "model":
                self.config.model,

            "messages": [

                {

                    "role": "user",

                    "content":
                        request.prompt,

                }

            ],

            "temperature":
                self.config.temperature,

            "max_tokens":
                self.config.max_tokens,

        }



    def extract_answer(
        self,
        response,
    ):

        return response[
            "choices"
        ][0][
            "message"
        ][
            "content"
        ]

    def extract_usage(
        self,
        response,
    ):

        return response[
            "usage"
        ]

    def health_check(
        self,
    ):

        return True

    def supported_models(
        self,
    ):

        return [

            self.config.model

        ]