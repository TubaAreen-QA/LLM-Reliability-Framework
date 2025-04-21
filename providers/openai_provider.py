from __future__ import annotations

from framework.http.openai_transport import (
    OpenAITransport,
)

from framework.parsers.openai_parser import (
    OpenAIParser,
)

from providers.abstract_sdk_provider import (
    AbstractSDKProvider,
)






class OpenAIProvider(
    AbstractSDKProvider,
):
    PROVIDER_NAME = "openai"

    def __init__(
        self,
        config,
    ):

        super().__init__(
            config=config,
            transport=OpenAITransport(config),
            parser=OpenAIParser(),
        )

    @property
    def name(self):

        return "openai"

    def build_payload(
        self,
        request,
    ):

        return {

            "model":
                self.config.model,

            "messages":[

                {

                    "role":"user",

                    "content":
                        request.prompt,

                }

            ],

            "temperature":
                self.config.temperature,

            "max_tokens":
                self.config.max_tokens,

        }

    def health_check(self):

        return True

    def supported_models(self):

        return [

            self.config.model

        ]