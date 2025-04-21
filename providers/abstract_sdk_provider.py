from __future__ import annotations

import time
from abc import ABC
from abc import abstractmethod

from framework.contracts.provider_request import ProviderRequest
from framework.contracts.provider_response import ProviderResponse

from framework.http.provider_transport import (
    ProviderTransport,
)

from framework.parsers.base_parser import (
    BaseParser,
)

from providers.base_provider import BaseProvider

  


class AbstractSDKProvider(
    BaseProvider,
    ABC,
):

    def __init__(
        self,
        config,
        transport: ProviderTransport,
        parser: BaseParser,
    ):

        super().__init__(config)

        self.transport = transport

        self.parser = parser

    @abstractmethod
    def build_payload(
        self,
        request: ProviderRequest,
    ) -> dict:
        ...

    def ask(
        self,
        request: ProviderRequest,
    ) -> ProviderResponse:

        payload = self.build_payload(
            request
        )

        start = time.perf_counter()

        raw = self.transport.execute(
            payload
        )

        elapsed = (
            time.perf_counter()
            - start
        ) * 1000

        return self.parser.parse(
            request=request,
            raw_response=raw,
            provider=self.name,
            model=self.config.model,
            latency_ms=elapsed,
        )