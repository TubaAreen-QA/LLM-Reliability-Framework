from __future__ import annotations

from framework.http.claude_transport import (
    ClaudeTransport,
)

from framework.parsers.claude_parser import (
    ClaudeParser,
)

from providers.abstract_sdk_provider import (
    AbstractSDKProvider,
)


   


class ClaudeProvider(
    AbstractSDKProvider,
):
    PROVIDER_NAME = "claude"

    def __init__(
        self,
        config,
    ):

        super().__init__(
            config=config,
            transport=ClaudeTransport(config),
            parser=ClaudeParser(),
        )

  

    def build_payload(
        self,
        request,
    ):

        return {

            "model":
                self.config.model,

            "max_tokens":
                self.config.max_tokens,

            "messages":[

                {

                    "role":"user",

                    "content":
                        request.prompt,

                }

            ]

        }

    def health_check(self):

        return True

    def supported_models(self):

        return [

            self.config.model

        ]