from __future__ import annotations

import time
from abc import ABC
from abc import abstractmethod
from typing import Any

from framework.contracts.provider_request import ProviderRequest
from framework.contracts.provider_response import ProviderResponse

from providers.base_provider import BaseProvider


class AbstractSDKProvider(
    BaseProvider,
    ABC,
):

    @abstractmethod
    def build_payload(
        self,
        request: ProviderRequest,
    ) -> dict[str, Any]:
        ...

    @abstractmethod
    def extract_answer(
        self,
        response: dict[str, Any],
    ) -> str:
        ...

    @abstractmethod
    def extract_usage(
        self,
        response: dict[str, Any],
    ) -> dict[str, int]:
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
            time.perf_counter() - start
        ) * 1000

        return ProviderResponse(

            provider=self.name,

            model=self.config.model,

            prompt=request.prompt,

            answer=self.extract_answer(
                raw
            ),

            response_time_ms=round(
                elapsed,
                3,
            ),

            token_usage=self.extract_usage(
                raw
            ),

            raw_response=raw,

            metadata={},
        )