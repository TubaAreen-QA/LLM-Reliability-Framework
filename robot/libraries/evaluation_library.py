from __future__ import annotations

from framework.config.config_loader import (
    ConfigLoader,
)

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.engine.evaluation_engine import (
    EvaluationEngine,
)

from framework.factory.provider_factory import (
    ProviderFactory,
)


class EvaluationLibrary:

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(
        self,
        config_path: str = "config/framework.yaml",
    ) -> None:

        self._config = ConfigLoader(
            config_path
        ).load()

    def evaluate_prompt(
        self,
        prompt: str,
        expected,
    ):

        provider = ProviderFactory.create(

            self._config[
                "provider"
            ][
                "name"
            ]

        )

        request = ProviderRequest(

            provider=self._config[
                "provider"
            ][
                "name"
            ],

            model=self._config[
                "provider"
            ][
                "model"
            ],

            prompt=prompt,

        )

        engine = EvaluationEngine(

            provider=provider,

            validator_names=self._config[
                "validators"
            ],

        )

        return engine.evaluate(

            request=request,

            expected=expected,

        )