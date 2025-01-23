from providers.fake_provider import FakeProvider


class ProviderFactory:

    PROVIDERS = {

        "fake": FakeProvider

    }

    @classmethod
    def create(cls, provider_name):

        provider = cls.PROVIDERS.get(provider_name)

        if provider is None:

            raise ValueError(
                f"Unknown provider: {provider_name}"
            )

        return provider()