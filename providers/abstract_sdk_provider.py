from __future__ import annotations

import time
from abc import abstractmethod

from framework.adapters.base_adapter import BaseAdapter

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)

from framework.http.provider_transport import (
    ProviderTransport,
)

from providers.base_provider import BaseProvider


class AbstractSDKProvider(BaseProvider):
    """
    Template implementation for SDK based providers.

    Workflow

        build_payload()

              ↓

        transport.execute()

              ↓

        adapter.adapt()

              ↓

        ProviderResponse
    """

    def __init__(
        self,
        config,
        transport: ProviderTransport,
        adapter: BaseAdapter,
    ):

        super().__init__(config)

        self.transport = transport

        self.adapter = adapter

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

        raw_response = self.transport.execute(
            payload
        )

        latency = (

            time.perf_counter()

            - start

        ) * 1000

        return self.adapter.adapt(

            request=request,

            raw_response=raw_response,

            provider=self.name,

            model=self.config.model,

            latency_ms=latency,

        )