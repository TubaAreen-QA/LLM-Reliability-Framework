from __future__ import annotations

import time

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)

from framework.exceptions.provider_error import (
    ProviderError,
)

from providers.base_provider import (
    BaseProvider,
)


class ProviderService:

    def execute(
        self,
        provider: BaseProvider,
        request: ProviderRequest,
    ) -> ProviderResponse:

        attempts = 0

        retries = getattr(
            provider,
            "retries",
            0,
        )

        last_exception = None

        while attempts <= retries:

            try:

                return provider.ask(
                    request
                )

            except Exception as ex:

                last_exception = ex

                attempts += 1

                if attempts <= retries:

                    time.sleep(1)

        raise ProviderError(
            str(last_exception)
        )