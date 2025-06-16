from framework.bootstrap.provider_bootstrap import (
    ProviderBootstrap,
)

from framework.config.provider_loader import (
    ProviderLoader,
)

from framework.factory.provider_factory import (
    ProviderFactory,
)


def test_provider_factory_creates_provider():

    ProviderBootstrap.initialize()

    config = ProviderLoader(

        "config/providers.yaml",

    ).load(

        "fake",

    )

    provider = ProviderFactory.create(

        config,

    )

    assert provider is not None

    assert provider.PROVIDER_NAME == "fake"