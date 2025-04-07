from __future__ import annotations

from framework.http.claude_transport import (
    ClaudeTransport,
)

from providers.abstract_sdk_provider import (
    AbstractSDKProvider,
)


class ClaudeProvider(
    AbstractSDKProvider,
):

    def __init__(
        self,
        config,
    ):

        super().__init__(config)

        self.transport = (
            ClaudeTransport(
                config
            )
        )

    @property
    def name(self):

        return "claude"

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

    def extract_answer(
        self,
        response,
    ):

        return response[
            "content"
        ][0][
            "text"
        ]

    def extract_usage(
        self,
        response,
    ):

        return {

            "prompt_tokens":

                response[
                    "usage"
                ][
                    "input_tokens"
                ],

            "completion_tokens":

                response[
                    "usage"
                ][
                    "output_tokens"
                ],

            "total_tokens":

                response[
                    "usage"
                ][
                    "input_tokens"
                ]

                +

                response[
                    "usage"
                ][
                    "output_tokens"
                ]

        }

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