from __future__ import annotations

import argparse

from framework.bootstrap.provider_bootstrap import (
    ProviderBootstrap,
)

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.engine.evaluation_engine import (
    EvaluationEngine,
)


class EvalForgeCLI:

    def __init__(self):

        self.parser = argparse.ArgumentParser(
            prog="evalforge"
        )

        self.parser.add_argument(
            "--provider",
            required=True,
        )

        self.parser.add_argument(
            "--prompt",
            required=True,
        )

        self.parser.add_argument(
            "--expected",
            default="",
        )

        self.parser.add_argument(
            "--validators",
            nargs="*",
            default=[],
        )

        self.parser.add_argument(
            "--profile",
            default="default",
        )

        self.parser.add_argument(
            "--provider-config",
            default="config/providers.yaml",
        )

        self.parser.add_argument(
            "--profile-config",
            default="config/profiles.yaml",
        )

    def run(self):

        args = self.parser.parse_args()

        ProviderBootstrap.initialize()

        engine = EvaluationEngine(

            provider_name=args.provider,

            validator_names=args.validators,

            provider_file=args.provider_config,

            profile_name=args.profile,

            profile_file=args.profile_config,

        )

        request = ProviderRequest(

            prompt=args.prompt,

        )

        result = engine.evaluate(

            request=request,

            expected=args.expected,

        )

        print(result)


def main():

    EvalForgeCLI().run()


if __name__ == "__main__":

    main()