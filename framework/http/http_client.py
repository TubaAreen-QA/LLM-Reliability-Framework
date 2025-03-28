from __future__ import annotations

from typing import Any

import requests

from framework.http.base_client import (
    BaseHttpClient,
)


class HttpClient(BaseHttpClient):

    def post(
        self,
        url: str,
        headers: dict[str, str],
        payload: dict[str, Any],
        timeout: int,
    ) -> dict[str, Any]:

        response = requests.post(
            url=url,
            headers=headers,
            json=payload,
            timeout=timeout,
        )

        response.raise_for_status()

        return response.json()